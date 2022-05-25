import uvicorn
import http.server
import socketserver
import threading
import os
import random

R_PORT = random.randint(8001, 9000)     # :D

# Make sure that code elsewhere reflects these values
BACK_PORT = 8000
BACK_IP = "0.0.0.0"    # SET THIS TO DEVICE IP, THEN SAME TO src/front/includes/script.js
FRONT_PORT = R_PORT
FRONT_IP = "0.0.0.0"

def runBack():
    uvicorn.run("src.back.main:app", host=BACK_IP, port=BACK_PORT, log_level="info")

def runFront():
    os.chdir('src/front/')
    handler = http.server.SimpleHTTPRequestHandler

    # Allow running on in use addresses. Circumvents error of improper closing of threads
    # Set this to true if you want to use a single port. Creates UB
    socketserver.TCPServer.allow_reuse_address = False
    with socketserver.TCPServer((FRONT_IP, FRONT_PORT), handler) as httpd:
        print("Server started at: " + FRONT_IP + str(FRONT_PORT))
        httpd.serve_forever()


if __name__ == "__main__":
    t1 = threading.Thread(target=runBack)
    t2 = threading.Thread(target=runFront)
    t1.start()
    t2.start()
