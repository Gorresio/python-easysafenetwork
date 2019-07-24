#
# Thanks some people on internet for class AESCipher. :)
# The original code of this class is unknown for me.
#


from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]


class AESCipher:


    def __init__(self, key):
        self.key = sha256(key.encode('utf-8')).digest()


    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(raw)


    def decrypt(self, enc):
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))

