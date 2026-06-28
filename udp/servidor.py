# Importa a biblioteca de sockets
from socket import *

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
    message, clientAddress = serverSocket.recvfrom(2048)

    # Exibe a mensagem recebida
    print(f"\nMensagem recebida: {message.decode()}")

    # Exibe o endereço do cliente
    print(f"Cliente: {clientAddress}")

    # Converte a mensagem para maiúsculas
    modifiedMessage = message.decode().upper()

    # Exibe a resposta enviada
    print(f"Resposta enviada: {modifiedMessage}")

    # Envia a resposta ao cliente
    serverSocket.sendto(
        modifiedMessage.encode(),
        clientAddress
    )