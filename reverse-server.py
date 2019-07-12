import socket

class Server():
    def __init__(self):
        print("Server initialized...")

    def listenExec(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", 444))
        print("Listening...")
        s.listen(1)
        conn, addr = s.accept()
        print("Connection Established!")
        while 1:
            try:
                cmd = str(input("$ >"))
                conn.send(bytearray(cmd, "utf-8"))
                recv = conn.recv(102400).decode("utf-8")
                print(recv)
            except socket.error:
                break
        conn.close()
        exit(1)
server = Server()
server.listenExec()
