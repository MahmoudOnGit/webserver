import socket 
import threading
import os

def Client_connect(Socket):
    data = b""
    while b"\r\n\r\n" not in data:
        data += Socket.recv(1024)

    request = data.decode("utf-8")
    request_line = request.split("\r\n")[0]

    try:
        parts = request_line.split(" ")
        method = parts[0]
        path = parts[1]
        version = parts[2]
        
    except:
        Socket.send("HTTP/1.0 400 Bad Request\r\n\r\n".encode())
        Socket.close()
        return

    print(method, path, version)
    if ".." in path:
        Socket.send("HTTP/1.0 400 Bad Request\r\n\r\n".encode())
        Socket.close()
        return
    
    print("PATH:", path)
    
    if "/" in path[1:] and not (path.startswith("/main") or path.startswith("/media") or path.startswith("/support") or path.startswith("/about-us")):
        Socket.send("HTTP/1.0 403 Forbidden\r\n\r\n".encode())
        Socket.close()
        return

    file_path = "./static" + path

    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            content = f.read()
        status = "HTTP/1.0 200 OK\r\n"
        headers = "Content-Type: text/html\r\n" + "Content-Length: " + str(len(content)) + "\r\n"

        Socket.send((status + headers + "\r\n").encode())
        Socket.send(content)
        Socket.close()
    else:
        status = "HTTP/1.0 404 Not Found\r\n\r\n"
        Socket.send(status.encode())
        Socket.close()
        



def Server_launch():
    Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Server.bind(("0.0.0.0", 8088))
    Server.listen(5)

    while True:
        client, address = Server.accept()
        print(f"Connection accepted from {address}")
        thread = threading.Thread(target=Client_connect, args=(client,))
        thread.start()

Server_launch()