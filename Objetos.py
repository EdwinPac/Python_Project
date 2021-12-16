from Objeto_Seguro_ECC import ObjetoSeguro
import binascii


if __name__ == '__main__':
    edwin = ObjetoSeguro("Edwin")
    karen = ObjetoSeguro('Karen')

    karen.pub_key = edwin.llave_publica()
    edwin.pub_key = karen.llave_publica()

    msj_ed = "Hola Karen! Soy Edwin, ¿Cómo estás?. "
    print("Saludo:", msj_ed)
    msj_cif = edwin.cifrar_msj(edwin.pub_key, msj_ed)
    print("Saludo cifrado de Edwin:")
    #edwin.saludar(binascii.hexlify(msj_cif))
    #edwin.almacenar_msj(msj_ed)

    #print("Descifrar saludo")
    #msj_des = karen.descifrar_msj(msj_cif)
    #print("Saludo descifrado:", msj_des)
    #msj_dec = karen.decodificar64(msj_des)
    #print("Mensaje decodificado:", msj_dec)

    #print("Responder saludo")

    #msj_resp_cif = karen.responder(msj_dec)
    #print("Mensaje respuesta cifrada:", binascii.hexlify(msj_resp_cif))
    #edwin.esperar_respuesta(msj_resp_cif)
    #print("Descifrar respuesta")
    #resp_desci = edwin.descifrar_msj(msj_resp_cif)
    #print("Respuesta descifrada:", resp_desci)
    #resp_deco = edwin.decodificar64(resp_desci)
    #print("Respuesta decodificada:", resp_deco)


