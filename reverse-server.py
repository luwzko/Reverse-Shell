import socket
import struct

def send_msg(socks, msg):
    msg = struct.pack(">I", len(msg)) + msg
    socks.sendall(msg)
def recv_msg(socks):
    raw_msg = recvall(socks, 4)
    if not raw_msg:
        return None
    msglen = struct.unpack(">I", raw_msg)[0]
    return recvall(socks, msglen)
def recvall(sock,n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def listenExec():
    global conn
    global addr
    print("Server Initialized")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 4444))
    print("Listening...")
    s.listen(1)
    conn, addr = s.accept()
    print("Connection Established!")
    while 1:
        try:
            cmd = input("\n$ ")
            if cmd == "quit":
                exit(0)
            else: pass
            send_msg(conn,bytearray(cmd, "utf-8"))
            recv = recv_msg(conn)
            print(recv, end="\n")
        except socket.error:
                conn.close()
        except TypeError:
            pass
        except AttributeError:
            pass
listenExec()
