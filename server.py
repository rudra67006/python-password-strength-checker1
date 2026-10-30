
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from html import escape
from pathlib import Path
import os

# Locate the project folders
BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

# Read the HTML page
with open(TEMPLATE_DIR / "index.html", "r", encoding="utf-8") as file:
    page = file.read()

class PasswordChecker(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/style.css":
            try:
                with open(STATIC_DIR / "style.css", "rb") as file:
                    css = file.read()

                self.send_response(200)
                self.send_header("Content-Type", "text/css; charset=utf-8")
                self.send_header("Content-Length", str(len(css)))
                self.end_headers()
                self.wfile.write(css)

            except FileNotFoundError:
                self.send_error(404, "CSS file not found")

        elif self.path == "/":
            self.send_page("")

        else:
            self.send_error(404, "Page not found")

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        form = parse_qs(body)
        password = form.get("password", [""])[0]

        # Check the five requirements
        has_length = len(password) >= 8
        has_uppercase = False
        has_lowercase = False
        has_number = False
        has_special = False

        special_characters = "!@#$%^&*()-_+=<>?/[]{}"

        for character in password:
            if character.isupper():
                has_uppercase = True

            if character.islower():
                has_lowercase = True

            if character.isdigit():
                has_number = True

            if character in special_characters:
                has_special = True

        # Collect improvement suggestions
        suggestions = []

        if not has_length:
            suggestions.append("Use at least 8 characters.")

        if not has_uppercase:
            suggestions.append("Add an uppercase letter (A-Z).")

        if not has_lowercase:
            suggestions.append("Add a lowercase letter (a-z).")

        if not has_number:
            suggestions.append("Add a number (0-9).")

        if not has_special:
            suggestions.append("Add a special character such as @ or !.")

        # Display the result
        if not suggestions:
            result = """
            <section class="result strong">
                <h2>Password Strength: STRONG</h2>
                <p>All five requirements passed!</p>
            </section>
            """
        else:
            items = "".join(
                "<li>" + escape(item) + "</li>"
                for item in suggestions
            )

            result = """
            <section class="result weak">
                <h2>Password Strength: WEAK</h2>
                <h3>Suggestions to improve your password</h3>
                <ul>""" + items + """</ul>
            </section>
            """

        self.send_page(result)

    def send_page(self, result):
        content = page.replace("{{RESULT}}", result)
        encoded = content.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


host = "0.0.0.0"
port = int(os.environ.get("PORT", 8000))

server = HTTPServer((host, port), PhishingHandler)
print("Password Strength Checker is running!")
print("Open http://localhost:8000 in Chrome")

server.serve_forever()
