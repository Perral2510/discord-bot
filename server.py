import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

    def log_message(self, format, *args):
        return # Tắt log HTTP rác

def run_dummy_server():
    port = int(os.getenv("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    print(f"Dummy port listening on 0.0.0.0:{port}")
    server.serve_forever()

def start_keep_alive():
    thread = threading.Thread(target=run_dummy_server, daemon=True)
    thread.start()