

def server(host, port, symmetricKey):
    sockVanilla = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockVanilla.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockVanilla.bind((host, port))
    sockVanilla.listen(5)
    while True:
        sockClientVanilla, source = sockVanilla.accept()
        sock = EasySafeSocket(sockClientVanilla, symmetricKey)
        threading.Thread(target=OnConnection, args=(sock, source[0], source[1])).start()

