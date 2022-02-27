import socket

target_host = "data.pr4e.org"
port = 80

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((target_host, port))
cmd = "GET /romeo.txt HTTP/1.0\r\nHost:%s\r\n\r\n" % target_host
mysock.send(cmd.encode())

while True:
    data = mysock.recv(512)
    if (len(data) <1):
        break
    print(data.decode())
mysock.close()
