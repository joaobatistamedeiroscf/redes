# Importa todas as funções e constantes da biblioteca socket
from socket import *

# Define o endereço IP do servidor
# 127.0.0.1 representa o próprio computador (localhost)
serverName = 'localhost'

# Define a porta utilizada pelo servidor
serverPort = 12000

# Cria um socket UDP
# AF_INET = utiliza endereços IPv4
# SOCK_DGRAM = utiliza o protocolo UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Solicita ao usuário uma mensagem para enviar ao servidor
message = input("Digite uma mensagem em letras minúsculas: ")

# Envia a mensagem ao servidor
# encode() converte a string para bytes
clientSocket.sendto(
    message.encode(),
    (serverName, serverPort)
)

# Aguarda a resposta enviada pelo servidor
# modifiedMessage recebe a mensagem retornada
# serverAddress recebe o endereço do servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Exibe a resposta recebida do servidor
print("Resposta do servidor:", modifiedMessage.decode())

# Fecha o socket do cliente
clientSocket.close()