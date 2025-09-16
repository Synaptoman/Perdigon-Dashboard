import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8080))
DIRECTORY = "build/web"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at http:// ✅ Next Steps

1. Save this as `server.py` in your project folder.
2. Create a `requirements.txt` (can be empty or include `http.server` if needed).
3. Zip the folder containing:
   - `server.py`
   - `requirements.txt`
   - `build/web/` folder

Then deploy it to Azure App Service via the portal.

---

Would you like me to generate this zip file for you or help with the Azure portal upload steps?