import socket

HOST = ''
PORT = 12321

# with: no final da execução vai chamar o close
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind: cria o vínculo
    s.bind((HOST, PORT))
    # listen: quantas conexões pendentes existe no socket
    s.listen(5)  # até 5 em espera, se chegar outra (a sexta) é rejeitada
    print(f"Aguardando novas conexões...")
    conn, addr = s.accept()

    with conn:
        print(f'Conectado a {addr}')
        while True:
            data = conn.recv(1024)
            if not data: break
            if len(data) > 0:
                print(f"Mensagem recebida: {data.decode('utf-8')}")
            conn.sendall(data)
