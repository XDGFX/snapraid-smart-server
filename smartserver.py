import subprocess
import threading
import time
from datetime import datetime

# How frequently to run (in seconds)
interval = 60 * 60 * 12  # Run every 12 hours

def startWebserver():
    import http.server
    import socketserver

    PORT = 8888
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("Serving on port", PORT)
        httpd.serve_forever()


def updateData():
    timestamp = "Last updated at: " + \
        datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n\n"

    # Run snapraid smart status command
    data = timestamp + subprocess.run(['snapraid', 'smart', '-v'],
                      stdout=subprocess.PIPE).stdout.decode("utf-8")

    data = data.strip()

    # Read index-master.html and write edited file to index.html
    with open("index-master.html", "r") as f:
        html = f.read().replace('%s', data)
    with open("index.html", "w") as f:
        f.write(html)


# Main code

# Define and start webserver
http_thread = threading.Thread(target=startWebserver)
http_thread.start()

# Update drive data on loop
while 1:
    updateData()
    time.sleep(interval)
