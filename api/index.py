from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json
import os

# Read marks data from JSON file
marks_file_path = os.path.join(os.path.dirname(__file__), "marks.json")
with open(marks_file_path, "r") as f:
    marks_data = json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(self.path.split("?")[1] if "?" in self.path else "")
        names = query.get("name", [])
        marks = [marks_data.get(name, 0) for name in names]

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        self.wfile.write(json.dumps({"marks": marks}).encode())