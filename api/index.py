# api/index.py
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json

marks_data = {
    "X": 10,
    "Y": 20,
    "Z": 30,
    "A": 15
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(self.path.split("?")[1] if "?" in self.path else "")
        names = query.get("name", [])
        marks = [marks_data.get(name, 0) for name in names]

        # Set headers
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        response = json.dumps({"marks": marks})
        self.wfile.write(response.encode())