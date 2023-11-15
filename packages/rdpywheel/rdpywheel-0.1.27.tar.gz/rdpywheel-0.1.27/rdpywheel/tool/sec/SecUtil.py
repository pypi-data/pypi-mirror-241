import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA


class SecUtil:

    @staticmethod
    def visa_encrypt(public_key: str, content: str):
        rsakey = RSA.importKey(public_key)
        cipher = Cipher_pksc1_v1_5.new(rsakey)
        encrypt_text = cipher.encrypt(content.encode())
        cipher_text = base64.b64encode(encrypt_text)
        return cipher_text.decode()
