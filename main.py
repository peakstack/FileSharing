from socket import *
import threading
import sys


class Connection:

    def connect(self):
        self.socket_server.connect((self.host, self.port))

    def start_receiving(self):
        self.socket_client.bind((self.host, self.port))
        self.socket_client.listen(5)

    def send_packet(self):
        pass

    def send_file(self, filename):
        with open(filename, "rb") as f:
            print("sending file...")
            data = f.read()
            data_sent = self.socket_server.sendall(data)
            if data_sent:
                self.socket_client.close()

    def stop_receiving(self):
        self.socket_client.close()

    def receive(self):
        while True:
            (connection, address) = self.socket_client.accept()
            print("[+] Client connected: ", address)

            f = open("123.txt", "wb")
            while True:
                data = connection.recv(4096)
                if not data:
                    break
                f.write(data)
            f.close()
            print("[+] Download complete!")
            connection.close()

    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.socket_server = socket(AF_INET, SOCK_STREAM)
        self.socket_client = socket(AF_INET, SOCK_STREAM)


def main():
    connection = Connection("127.0.0.1", 24245)
    connection.connect()
    connection.send_file("main.py")

    #server_thread = threading.Thread()
    #server_thread.daemon = True
    #server_thread.start()


if __name__ == "__main__":
    main()
