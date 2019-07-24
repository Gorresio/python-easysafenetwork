

def connect(host, port, symmetricKey):
    sockVanilla = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockVanilla.connect((host, port))
    sock = EasySafeSocket(sockVanilla, symmetricKey)
    return sock

