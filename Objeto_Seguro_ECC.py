from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
import base64
import logging

logging.basicConfig(level=logging.DEBUG, format="\n%(asctime)s - %(message)s")

#  Fase 1: Definimos la clase


class ObjetoSeguro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__private_key = None
        self.__public_key = None
        self.pub_key = None
        self.gen_llaves()
#        self.__private_key = generate_eth_key()
#        self.__private_key_hex = self.__private_key.to_hex()
        #  print(self.__private_key_hex)

    #  Decorador que hace que una función actúe como una propiedad

    def gen_llaves(self):
        self.priv_key = generate_eth_key()
        self.__private_key = self.priv_key.to_hex()
        self.__public_key = self.priv_key.public_key.to_hex()

    def llave_publica(self):
        return self.__public_key

    def decodificar64(self, msj: bytes):
        c64_decode_message = base64.b64decode(msj).decode("utf-8")
        return c64_decode_message

    def codificar64(self, msj: str) -> bytes:
        c64_encode_message = base64.b64encode(msj).encode("utf-8")
        return c64_encode_message

    def saludar(self, msj: str):
#        print("Hola mi nombre es " + name)
        print("Edwin dice" + msj)

    def responder(self, msj: str):
        resp = msj + "MensajeRespuesta"
        print(resp)
        resp_cif = self.cifrar_msj(self.pub_key, resp)
        return resp_cif

    def cifrar_msj(self, pub_key: str, msj: str) -> bytes:
        msj_codif = self.codificar64(msj)
        msj_cif = encrypt(pub_key, msj_codif)
        return msj_cif

    def descifrar_msj(self, msj: bytes):
        msj_decif = decrypt(self.__private_key, msj)
        msj_deco = self.decodificar64(msj_decif)
        return msj_deco

    def almacenar_msj(self, msj: str):
        python_project = open("archivo.txt", "a")
        python_project.write(msj + '\n')
        python_project.close()
        return msj

    def esperar_respuesta(self, msj: bytes):
        msj_dc = self.descifrar_msj(msj)
        msj_de = self.codificar64(msj_dc)
        guardar = self.almacenar_msj(msj_de)
        return guardar











