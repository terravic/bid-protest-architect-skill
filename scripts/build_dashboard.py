#!/usr/bin/env python3
"""
Standalone Dashboard Builder & Live SSE Server (build_dashboard.py)

Compiles empirical procurement audit data from any user-supplied directory or
file list into a standalone interactive HTML dashboard (`dashboard.html`)
adhering strictly to DESIGN.md, with native host OS theme detection and
optional HTTP + Server-Sent Events (SSE) live streaming.
"""

import os
import sys
import json
import time
import platform
import argparse
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Dict, Any, List, Optional

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.bid_protest_analyzer import BidProtestAnalyzer
from scripts.search_diagnostics import run_diagnostics, LocalCorpusEngine, build_dynamic_queries, clean_text

TEMPLATE_PATH = os.path.join(ROOT_DIR, "resources", "templates", "dashboard_template.html")


def detect_host_system_theme() -> str:
    """Queries native OS dark/light preference as headless webview fallback (DESIGN.md §3)."""
    sys_name = platform.system().lower()
    try:
        if sys_name == "darwin":
            res = subprocess.run(
                ["defaults", "read", "-g", "AppleInterfaceStyle"],
                capture_output=True,
                text=True,
                timeout=2,
            )
            return "dark" if "dark" in res.stdout.lower() else "light"

        if sys_name == "windows":
            import winreg  # type: ignore

            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize",
            )
            val, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            return "light" if int(val) == 1 else "dark"

        # Linux: check GTK_THEME, gsettings, and kdeglobals
        gtk_env = os.environ.get("GTK_THEME", "").lower()
        if "dark" in gtk_env:
            return "dark"

        for cmd in (
            ["gsettings", "get", "org.gnome.desktop.interface", "color-scheme"],
            ["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"],
        ):
            try:
                res = subprocess.run(cmd, capture_output=True, text=True, timeout=2)
                if res.returncode == 0 and "dark" in res.stdout.lower():
                    return "dark"
            except Exception:
                pass

        kde_cfg = os.path.expanduser("~/.config/kdeglobals")
        if os.path.isfile(kde_cfg):
            with open(kde_cfg, "r", encoding="utf-8", errors="ignore") as f:
                if "dark" in f.read().lower():
                    return "dark"
    except Exception:
        pass
    return "light"


def compute_dashboard_payload(
    data_dir: Optional[str] = "synthetic_data",
    file_paths: Optional[List[str]] = None,
    grounds_json: Optional[str] = None,
    index_json: Optional[str] = None,
    in_memory_docs: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Runs the complete indexing, 8-ground audit, deadline, and retrieval pipeline."""
    analyzer = BidProtestAnalyzer(
        data_dir=None if in_memory_docs else data_dir,
        file_paths=file_paths,
        grounds_override_path=grounds_json,
        index_override_path=index_json,
    )
    if in_memory_docs is not None:
        analyzer.indexer.load_from_memory(in_memory_docs)
        analyzer.corpus_files = analyzer.indexer.documents
        analyzer.procurement_index = analyzer.indexer.extract_evaluation_matrix()
    else:
        analyzer.load_corpus()

    grounds = analyzer.run_investigation()
    deadlines = analyzer.get_deadlines()

    if in_memory_docs is not None:
        engine = LocalCorpusEngine(data_dir=None)
        engine.documents = {k: v for k, v in in_memory_docs.items() if not k.lower().endswith(".json")}
        engine.clean_docs = {k: clean_text(v) for k, v in engine.documents.items()}
        queries = build_dynamic_queries(engine)
        total = max(len(queries), 1)
        details = []
        n_hits = u_hits = o_hits = 0
        for q in queries:
            tdocs = q["target_docs"]
            tphrase = clean_text(q["target_phrase"])
            rn = engine.search(q["naive_query"], top_k=2)
            ru = engine.search(q["ui_query"], top_k=2)
            ro = engine.search(q["optimized_query"], top_k=2)
            hn = any(r[0] in tdocs and tphrase in engine.clean_docs.get(r[0], "") for r in rn[:1])
            hu = any(r[0] in tdocs and tphrase in engine.clean_docs.get(r[0], "") for r in ru)
            ho = any(r[0] in tdocs and tphrase in engine.clean_docs.get(r[0], "") for r in ro)
            if hn: n_hits += 1
            if hu: u_hits += 1
            if ho: o_hits += 1
            details.append({
                "query_id": q["id"],
                "category": q["category"],
                "target_docs": tdocs,
                "optimized_query": q["optimized_query"],
                "hit_naive": hn,
                "hit_ui": hu,
                "hit_opt": ho,
            })
        diagnostics = {
            "naive": {"hits": n_hits, "total": len(queries), "accuracy": round((n_hits / total) * 100, 1)},
            "ui_direct": {"hits": u_hits, "total": len(queries), "accuracy": round((u_hits / total) * 100, 1)},
            "optimized": {"hits": o_hits, "total": len(queries), "accuracy": round((o_hits / total) * 100, 1)},
            "details": details,
        }
    else:
        diagnostics = run_diagnostics(data_dir or "", file_paths=file_paths)

    return {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "system_theme": detect_host_system_theme(),
        "procurement_index": analyzer.procurement_index,
        "grounds": [g.to_dict() for g in grounds],
        "taxonomy_audit": analyzer.taxonomy_audit,
        "deadlines": deadlines,
        "search_diagnostics": diagnostics,
    }


def build_dashboard_html(
    output_path: str = "dashboard.html",
    data_dir: Optional[str] = "synthetic_data",
    file_paths: Optional[List[str]] = None,
    grounds_json: Optional[str] = None,
    index_json: Optional[str] = None,
) -> str:
    """Renders standalone dashboard.html with embedded empirical audit payload."""
    if not os.path.isfile(TEMPLATE_PATH):
        raise FileNotFoundError(f"Dashboard template missing at {TEMPLATE_PATH}")

    payload = compute_dashboard_payload(
        data_dir=data_dir,
        file_paths=file_paths,
        grounds_json=grounds_json,
        index_json=index_json,
    )

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template_html = f.read()

    serialized = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    final_html = template_html.replace("__DASHBOARD_DATA_JSON__", serialized)

    abs_out = os.path.abspath(output_path)
    os.makedirs(os.path.dirname(abs_out), exist_ok=True)
    with open(abs_out, "w", encoding="utf-8") as f:
        f.write(final_html)

    return abs_out


def serve_dashboard(
    dashboard_path: str,
    data_dir: Optional[str],
    file_paths: Optional[List[str]],
    grounds_json: Optional[str],
    index_json: Optional[str],
    port: int = 8765,
) -> None:
    """Serves dashboard.html over HTTP with live SSE (/events) and /api/analyze."""

    def snapshot_mtime() -> float:
        latest = 0.0
        if data_dir and os.path.exists(data_dir):
            if os.path.isfile(data_dir):
                latest = max(latest, os.path.getmtime(data_dir))
            else:
                for root, _, files in os.walk(data_dir):
                    for fn in files:
                        latest = max(latest, os.path.getmtime(os.path.join(root, fn)))
        for fp in file_paths or []:
            if os.path.exists(fp):
                latest = max(latest, os.path.getmtime(fp))
        return latest

    class DashboardRequestHandler(BaseHTTPRequestHandler):
        def log_message(self, fmt: str, *args: Any) -> None:
            return

        def do_GET(self) -> None:
            if self.path == "/" or self.path.startswith("/dashboard.html") or self.path.startswith("/?"):
                build_dashboard_html(dashboard_path, data_dir, file_paths, grounds_json, index_json)
                with open(dashboard_path, "rb") as f:
                    body = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return

            if self.path.startswith("/events"):
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Cache-Control", "no-cache")
                self.send_header("Connection", "keep-alive")
                self.end_headers()
                last_seen = snapshot_mtime()
                try:
                    while True:
                        time.sleep(1.5)
                        cur = snapshot_mtime()
                        if cur > last_seen:
                            last_seen = cur
                            payload = compute_dashboard_payload(data_dir, file_paths, grounds_json, index_json)
                            msg = f"event: audit_update\ndata: {json.dumps(payload)}\n\n"
                            self.wfile.write(msg.encode("utf-8"))
                            self.wfile.flush()
                        else:
                            self.wfile.write(b": keepalive\n\n")
                            self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError):
                    return

            self.send_response(404)
            self.end_headers()

        def do_POST(self) -> None:
            if self.path == "/api/analyze":
                length = int(self.headers.get("Content-Length", "0"))
                raw = self.rfile.read(length).decode("utf-8", errors="replace")
                req = json.loads(raw)
                docs_list = req.get("documents", [])
                docs_map = {d["filename"]: d["content"] for d in docs_list if "filename" in d and "content" in d}
                payload = compute_dashboard_payload(in_memory_docs=docs_map)
                out = json.dumps(payload).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(out)))
                self.end_headers()
                self.wfile.write(out)
                return

            self.send_response(404)
            self.end_headers()

    server = ThreadingHTTPServer(("127.0.0.1", port), DashboardRequestHandler)
    print(f"Serving live Bid Protest Dashboard at http://127.0.0.1:{port}/dashboard.html?sse=1")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Build standalone interactive Bid Protest Audit Dashboard")
    parser.add_argument("--data", default="synthetic_data", help="Directory or file path to procurement corpus")
    parser.add_argument("--files", nargs="*", default=[], help="Additional explicit procurement files (.md/.txt/.docx/.pdf/.csv/.html/.json)")
    parser.add_argument("--grounds-json", default=None, help="Optional JSON file with agent-validated protest grounds")
    parser.add_argument("--index-json", default=None, help="Optional JSON file overriding procurement metadata")
    parser.add_argument("--output", default="dashboard.html", help="Output path for standalone dashboard.html")
    parser.add_argument("--serve", action="store_true", help="Serve dashboard over HTTP with live SSE streaming")
    parser.add_argument("--port", type=int, default=8765, help="Port for --serve mode")

    args = parser.parse_args()
    out = build_dashboard_html(
        output_path=args.output,
        data_dir=args.data,
        file_paths=args.files,
        grounds_json=args.grounds_json,
        index_json=args.index_json,
    )
    print(f"Standalone interactive dashboard generated: {out}")

    if args.serve:
        serve_dashboard(out, args.data, args.files, args.grounds_json, args.index_json, args.port)


if __name__ == "__main__":
    main()
