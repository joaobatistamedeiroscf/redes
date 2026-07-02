# Importa a biblioteca de sockets
from socket import *
import time

# Porta utilizada pelo servidor
serverPort = 12000

# Cria um socket UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Associa o socket à porta
serverSocket.bind(('', serverPort))

# Mensagem de inicialização
print("Servidor pronto para receber mensagens.")

# Mantém o servidor em execução
while True:
    # Recebe mensagem e endereço do cliente
    data, clientAddress = serverSocket.recvfrom(2048)
    
    # Separa mensagem e timestamp do cliente
    data_parts = data.decode().split('|')
    message = data_parts[0]
    client_send_time = float(data_parts[1])

    # Exibe a mensagem recebida
    print(f"\nMensagem recebida: {message}")
    # Exibe o endereço do cliente
    print(f"Cliente: {clientAddress}")

    # Converte a mensagem para maiúsculas
    modifiedMessage = message.upper()

    # Registra o tempo de resposta
    server_response_time = time.time()

    # Calcula tamanho da mensagem original em bytes
    msg_size = len(message.encode('utf-8'))

    # Exibe a resposta enviada
    print(f"Resposta enviada: {modifiedMessage}")

    # Monta resposta rica com todas as informações
    response = f"{modifiedMessage}|{clientAddress}|{client_send_time}|{server_response_time}|{msg_size}"

    # Envia a resposta ao cliente
    serverSocket.sendto(
        response.encode(),
        clientAddress
    )