"""Local REST interface for the IBM course's modified job listings.

The course example uses case-sensitive substring matching. This implementation
keeps that behavior for /data and also offers a boundary-aware comparison.
"""
import json
import re
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.parse import parse_qs, urlparse


def matches(records, field, term, mode='course'):
    pattern = re.escape(term)
    flags = 0
    if mode == 'bounded':
        pattern = r'(?<![\w+#])' + pattern + r'(?![\w+#])'
        flags = re.IGNORECASE
    expression = re.compile(pattern, flags)
    return [record for record in records
            if expression.search(str(record.get(field, '')))]


@contextmanager
def serve_jobs(records):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            query = urlparse(self.path)
            if query.path not in ('/data', '/data/all'):
                self.send_error(404)
                return
            parameters = parse_qs(query.query)
            mode = parameters.pop('mode', ['course'])[0]
            result = records
            for field, values in parameters.items():
                if field not in records[0]:
                    self.send_error(400, 'Unknown dataset field')
                    return
                result = matches(result, field, values[0], mode)
            body = json.dumps(result, ensure_ascii=False).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *_):
            pass

    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f'http://127.0.0.1:{server.server_port}'
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)
