import socket

HOST = 'localhost' # servidor que quero conectar
PORT = 12321

mensagem = input('Digite uma mensagem a ser enviada ao servidor: ')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(mensagem.encode('utf-8')) # manda o array de bytes da string
    data = s.recv(1024)
    print(f'Recebido {data.decode("utf-8")}')

