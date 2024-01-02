
# Python Framework for High Level Socket with Symmetric Encryption (AES256)

**easysafenetwork** is a simple library/framework for develop network applications with TCP protocol in a simple way.

Feature:
- High level socket method (implementation of *sendall* and *recvall*)
- AES256 encryption of payload
- Simple customization


### - Basic Use of easysafenetwork

**Functions**

| Method | Description |
|--------|-------------|
|sock = connect(host, port, symmetricKey)|Initialize client connection and return EasySafeSocket object|
|server(host, port, symmetricKey)|Initialize server multi-threading|


**EasySafeSocket Class**

| Method | Description |
|--------|-------------|
|write(data)|Send data (sendall). You don't send empty data|
|data = read()|Receive data (recvall made with chunk). If it return an empty string, it means that key is wrong.|
|close()|Close socket|


**Server Application**
For develop server applications, you must insert code to execute for each connection incoming into the function *OnConnection(sock, clientHost, clientPort)* and compile script with *./build_static_server <python script> <host> <port> <symmetric key>*.
For custom and complex dynamics, you can integrate source code of easysafenetwork into the application manually.


**Examples**


Compile easysafenetwork module for client
```
./build_client_module    # Output in ./build/easysafenetwork.pyc
```


client.py
```
import sys
from easysafenetwork import *

sock = connect("127.0.0.1", 2357, "SecretSymmetricKey")
sock.write("Hello!")
data = sock.read()
if data == "":
    sys.exit("Bad key")
sock.close()
print("Server has sent: " + data)
```

server.py
```
import sys

def OnConnection(sock, clientHost, clientPort):
    print("Connection from " + clientHost + ":" + str(clientPort))
    data = sock.read()
    if data == "":
        print(clientHost + ":" + str(clientPort) + " has a bad key.")
        return
    print(clientHost + ":" + str(clientPort) + " has sent: \"" + data + "\"")
    sock.write("Hi!")
    sock.close()
    print("Closed " + clientHost + ":" + str(clientPort))
```


Compile server.py with:
```
./build_static_server server.py 0.0.0.0 2357 SecretSymmetricKey
```
Output in ./build/server.pyc



### - Structure

The source code is structured in a modular way and *sh* scripts are used to assemble the library and/or applications.

This choice to manage the structure of the sources in an unorthodox way is given by the need to be able to easily modify the library and be able to manage the general application in a completely free way

There are no custom exceptions management: exceptions are handled for the respective standard libraries.

### - Note

easysafenetwork is a free software licensed by Zero Clause BSD.

Copy of Zero Clause BSD license is present into source file.

If you notice any violations by myself or by third parties, please contact me.

The use of easysafenetwork is at your own risk: read the license.

Stefano Gorresio

Email: stefano.gorresio@gmail.com

