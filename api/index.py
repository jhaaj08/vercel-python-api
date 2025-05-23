from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Load JSON file
            file_path = os.path.join(os.path.dirname(__file__), "marks.json")
            with open(file_path, "r") as f:
                raw_data = json.load(f)

            # Convert list of dicts → lookup dictionary
            marks_data = {entry["name"]: entry["marks"] for entry in raw_data}

            # Parse query params
            query = parse_qs(self.path.split("?")[1] if "?" in self.path else "")
            names = query.get("name", [])
            marks = [marks_data.get(name, 0) for name in names]

            # Send response
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"marks": marks}).encode())

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())