import socket
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(message)s'
)


class Client:
    def __init__(self, host: str, port: str):
        self.host = host
        self.port = port

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))

            for i in range(1, 16):
                logging.debug("Enviando msj al server")
                print(i)
                s.sendall(str(i).encode('utf8'))
                logging.debug("Cliente dice")
                res = s.recv(1024)
                print(res)
            s.shutdown(socket.SHUT_RDWR)
            s.close()


my_client = Client(host="127.0.0.1", port=12345)
my_client.run()

