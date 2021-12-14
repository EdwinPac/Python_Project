import logging
import socket

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(message)s'
)


class Server:
    def __init__(self, host: str, port: str):
        self.host = host
        self.port = port

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            self.listen_client(conn, addr)

    def listen_client(self, conn, addr):
        with conn:
            print('Conectado a:', addr)
            while True:
                for i in range(15, 30):
                    msj = conn.recv(1024)
                    logging.debug("El cliente manda")
                    print(msj)
                    logging.debug("EL servidor envia")
                    print(i)
                    conn.send(str(i).encode('utf8'))
                msj = conn.recv(1024)
                if not msj:
                    break


my_server = Server(host="127.0.0.1", port=12345)
my_server.run()
