import http.server
import socketserver
import webbrowser
import os

# Sample data for the table (You can modify this)
data = [
    ["Name", "Age", "Country"],
    ["Alice", "25", "USA"],
    ["Bob", "30", "UK"],
    ["Charlie", "28", "Canada"],
    ["David", "35", "Germany"]
]

# Generate dynamic HTML table
table_rows = "".join(
    "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
    for row in data
)

# Generate dynamic HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic HTML Table</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            text-align: center;
        }}
        table {{
            width: 50%;
            margin: auto;
            border-collapse: collapse;
        }}
        th, td {{
            border: 1px solid black;
            padding: 10px;
            text-align: center;
        }}
        th {{
            background-color: lightblue;
        }}
    </style>
</head>
<body>
    <h1>Dynamic HTML Table 📊</h1>
    <table>
        {table_rows}
    </table>
</body>
</html>
"""

# Save the generated HTML file
file_name = "table.html"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(html_content)

# Automatically open in a web browser
PORT = 8090
webbrowser.open("http://localhost:{PORT}")

# Serve the HTML file using Python's built-in HTTP server
os.chdir(os.path.dirname(os.path.abspath(file_name)))  # Set directory to the file location
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
