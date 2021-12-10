from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
from base64 import b85encode, b85decode
import logging

logging.basicConfig(level=logging.DEBUG, format="\n%(asctime)s - %(message)s")


class ObjetoSeguro:
    def __init__(self):
        self.__private_key = generate_eth_key()
        self.__private_key_hex = self.__private_key.to_hex()
        print(self.__private_key_hex)

    #  Decorador que hace que una función actúe como una propiedad
    @property
    def key_pub(self) -> str:
        return self.__private_key.public_key.to_hex()

    def __base85_decode(self, message: str) -> bytes:
        message_to_bytes = message.encode("utf-8")
        b85_decode_message = b85decode(message_to_bytes)
        return b85_decode_message

    @staticmethod
    def saludar(plain_text: str, publickey: str) -> str:
        plain_text_to_bytes = plain_text.encode("utf-8")
        message_cypher = encrypt(publickey, plain_text_to_bytes)
        b85_cypher = b85encode(message_cypher).decode("utf-8")
        return b85_cypher

    def responder(self, message_encrypted: str) -> str:
        message_encrypted_decode = self.__base85_decode(message_encrypted)
        message_decrypted = decrypt(self.__private_key_hex, message_encrypted_decode)
        message_decrypted_string = message_decrypted.decode("utf-8")
        return message_decrypted_string


logging.debug("**********Generando Llaves Públicas**********")
edwin = ObjetoSeguro()
pubkey_ed = edwin.key_pub
print("Llave pública de Edwin en Hexadecimal\n", pubkey_ed)
karen = ObjetoSeguro()
pubkey_ka = karen.key_pub
print("Llave pública de Karen en Hexadecimal\n", pubkey_ed)
msj_ed = "Hola mi nombre es Edwin, ¿Cómo estás?"


logging.debug("**********Cifrando un mensaje********** ")
msj_cif = edwin.saludar(msj_ed, pubkey_ka)
print("Cifrando Mensaje")
print("Mensaje Cifrado", msj_cif)


logging.debug("**********Descifrando Mensaje**********")
msj_dcif = karen.responder(msj_cif)
print("El mensaje es:", msj_dcif)

