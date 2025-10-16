# tcp_client.py
import socket

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        print(f"[TCP] Connected to {host}:{port}")

    def send(self, message):
        self.client.sendall(message.encode("utf-8"))

    def receive(self):
        data = self.client.recv(4096).decode("utf-8")
        return data
