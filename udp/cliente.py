# Importa todas as funções e constantes da biblioteca socket
from socket import *
import time
from datetime import datetime

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

# Registra o tempo de envio
send_time = time.time()

# Envia a mensagem + timestamp ao servidor
data_to_send = f"{message}|{send_time}"
clientSocket.sendto(
    data_to_send.encode(),
    (serverName, serverPort)
)

# Aguarda a resposta enviada pelo servidor
# modifiedMessage recebe a mensagem retornada
# serverAddress recebe o endereço do servidor
response, serverAddress = clientSocket.recvfrom(2048)

# Registra o tempo de recebimento
receive_time = time.time()

# Processa a resposta estruturada
parts = response.decode().split('|')
modified_message = parts[0]
client_addr = parts[1]
client_send_ts = float(parts[2])
server_resp_ts = float(parts[3])
msg_size = int(parts[4])

rtt = receive_time - send_time

# Função para formatar o tempo de forma legível
def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%d-%m-%y %H:%M:%S.%f")

# Exibe a resposta recebida do servidor
print("\n=== Resposta do Servidor ===")
print("Mensagem processada:", modified_message)
print("Endereço do cliente:", client_addr)
print(f"Tempo envio (cliente): {format_time(client_send_ts)}")
print(f"Tempo resposta (servidor): {format_time(server_resp_ts)}")
print(f"Intervalo (RTT): {rtt:.6f} segundos")
print(f"Tamanho da mensagem: {msg_size} bytes ({msg_size * 8} bits)")

# Fecha o socket do cliente
clientSocket.close()