

import socket
import threading



class EasySafeSocket:


    def __init__(self, sock, symmetricKey, timeout=10):
        self.sock = sock
        self.sock.settimeout(timeout)
        self.cipher = AESCipher(symmetricKey)

    
    def write(self, data):
        self.sock.sendall(self.cipher.encrypt(data))


    def read(self):
        payload = ""
        while True:
            chunk = self.sock.recv(65535)
            payload += chunk
            if len(chunk) < 65535:
                break
        return self.cipher.decrypt(payload)


    def close(self):
        self.sock.close()


