import socket

host = "localhost"
port = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen()

print("aguardando msg")

conn, ender = s.accept()

print("Connectado em ", ender)

while True:
    data = conn.recv(1024)
    if not data:
        print("fechando a conexao")
        conn.close()
        break
    else:
        conn.sendall(data)








