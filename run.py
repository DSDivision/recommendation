import uvicorn
import http.server
import socketserver
import threading
import os

# Make sure that code elsewhere reflects these values
BACK_PORT = 8000
BACK_IP = ""    # Empty means 'localhost'
FRONT_PORT = 8080
FRONT_IP = ""

def runBack():
    uvicorn.run("src.back.main:app", host=BACK_IP, port=BACK_PORT, log_level="info")

def runFront():
    os.chdir('src/front/')
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer((FRONT_IP, FRONT_PORT), handler) as httpd:
        print("Server started at: " + FRONT_IP + str(FRONT_PORT))
        httpd.serve_forever()


if __name__ == "__main__":
    t1 = threading.Thread(target=runBack)
    t2 = threading.Thread(target=runFront)
    t1.start()
    t2.start()
