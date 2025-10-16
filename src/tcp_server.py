# tcp_server.py
import socket

class TCPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.conn = None
        self.addr = None
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(1)
        print(f"[TCP] Listening on {host}:{port}")

    def accept_connection(self):
        self.conn, self.addr = self.server.accept()
        print(f"[TCP] Connection accepted from {self.addr}")

    def receive(self):
        data = self.conn.recv(4096).decode("utf-8")
        return data

    def send(self, message):
        self.conn.sendall(message.encode("utf-8"))
