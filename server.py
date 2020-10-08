import socket
import threading

HOST = ''
PORT = 12321

clients = []

def client_handle(conn, addr):
  with conn:
        print(f'Conectado a {addr}')
        print(" ")
        while True:
            data = conn.recv(1024)
            if not data: break
            print(f"Mensagem recebida de {addr}: {data.decode('utf-8')}")
            for client in clients:
                if addr != client["addr"]:
                    client["conn"].sendall(data) # envia de volta para o cliente a mesma mensagem que ele enviou

# with: no final da execução vai chamar o close
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind: cria o vínculo
    s.bind((HOST, PORT))
    # listen: quantas conexões pendentes existe no socket
    s.listen(5)  # até 5 em espera, se chegar outra (a sexta) é rejeitada
    
    while True:
        try:
            print(f"Aguardando novas conexões...")
            conn, addr = s.accept()
            clients.append({"connection": conn, "address": addr})

            thread = threading.Thread(target=client_handle, args=(conn, addr,)) # "," é pra saber que é o fim da tupla
            thread.start()
        except KeyboardInterrupt:
            print("Encerrando servidor.")
            s.close()
            break  