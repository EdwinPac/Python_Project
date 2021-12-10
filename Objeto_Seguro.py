from OpenSSL import SSL

class DH_Endpoint:
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key % self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r ** self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c)+key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message


message = "This is a ver secret message"

s_public = 197
s_private = 199

m_public = 151
m_private = 157

#  Sadat = DH_Endpoint(s_public, m_public, s_private)
#  Michael = DH_Endpoint(s_public, m_public, m_private)

#  print(Sadat.generate_partial_key())
#  print(Michael.generate_partial_key())
#  print(Sadat.generate_full_key(Michael.generate_partial_key()))
#  print(Sadat.encrypt_message(message))
#  print(Michael.generate_full_key(Sadat.generate_partial_key()))
#  print(Michael.decrypt_message(Sadat.encrypt_message(message)))

Edwin = DH_Endpoint(111, 151, 191)
Karen = DH_Endpoint(111, 151, 199)


print(Edwin.generate_partial_key())
print(Edwin.generate_full_key(Karen.generate_partial_key()))
print(Karen.generate_partial_key())
print(Karen.generate_full_key(Edwin.generate_partial_key()))
print(Edwin.encrypt_message("Edwin dice: Hola bebe"))
print(Karen.decrypt_message(Edwin.encrypt_message("Edwin dice: Hola bebe")))
print(Karen.encrypt_message("Karen dice: ¿Cómo estas?"))
print(Edwin.decrypt_message(Karen.encrypt_message("Karen dice: ¿Cómo estas?")))