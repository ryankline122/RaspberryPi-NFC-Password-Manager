import socket

class AuthService:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

    def send_uid(self, uid: str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(uid.encode('utf-8'))
            print(f"Sent '{uid}' to the server")
            print("Waiting for server response...")

            data = s.recv(1024)
            print(f"Message from server: {data}")
