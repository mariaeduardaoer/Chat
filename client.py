import socket
import threading

HOST = 'localhost' # servidor que quero conectar
PORT = 12321

def handle_received_message(sock):
    while True:
        data = sock.recv(1024)
        print(" ")
        print(f'Received {data.decode("utf-8")}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # faz a conexão
    
    thread = threading.Thread(target=handle_received_message, args=(s,))
    thread.start()

    while True:
        try:
            mensagem = input('Digite uma mensagem a ser enviada ao servidor: ')
            s.sendall(mensagem.encode('utf-8')) # manda o array de bytes da string
        except KeyboardInterrupt:
            print(" ")
            print('Encerrando cliente')
            s.close()
            break