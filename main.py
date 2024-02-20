import socket  as sck

server_socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 0))

server_addr = server_socket.getsockname()
print(f"(System Info) Server Runing At: {server_addr}")

server_socket.listen(5)
print("(Server Waiting) Well, I'll wait until someone calls me :s")

client_socket, client_addr = server_socket.accept()
print("(Server Gets Connection) Finally!, someone called me :D")

client_socket.close()
server_socket.close()