from Objeto_Seguro_ECC import ObjetoSeguro
from Objeto_Seguro_ECC import encrypt, decrypt, generate_eth_key


#  Fase 2: Generación de objetos.
Edwin = ObjetoSeguro()
Karen = ObjetoSeguro()

#  Fase 3: Utilización de los objetos.
key_ed = Edwin.gen_llaves
key_ka = Karen.gen_llaves

msj_ed = input(str("Edwin dice: "))


m_c_e = Edwin.saludar(msj_ed, key_ka)
Edwin.guardar_msj(msj_ed)
print("Mensaje cifrado: ", m_c_e)
Karen.responder(m_c_e)
msj_ka = input(str("karen dice: "))
m_c_k = Karen.saludar(msj_ka, key_ed)
Karen.guardar_msj(msj_ka)
print("Mensaje cifrado: ", m_c_k)

#  Edwin.responder(Karen.responder(m_c_e))
#  Edwin.guardar_msj(msj_ed)









