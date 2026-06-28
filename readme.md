# Redes TCP e UDP em Python

Projeto didático com exemplos de comunicação cliente-servidor usando sockets em Python. A aplicação demonstra duas abordagens de rede:

- TCP, com conexão orientada a fluxo de dados.
- UDP, com envio de datagramas sem estabelecimento de conexão.

Em ambos os casos, o servidor recebe uma mensagem do cliente, converte o texto para maiúsculas e devolve a resposta.

## O que é este projeto

Este repositório contém dois exemplos independentes de comunicação em rede:

- `tcp/` mostra um cliente e um servidor usando TCP.
- `udp/` mostra um cliente e um servidor usando UDP.

O objetivo é servir como base de estudo para entender a diferença prática entre os dois protocolos e a estrutura mínima de uma aplicação cliente-servidor.

## Tecnologias utilizadas

- Python 3
- Biblioteca padrão `socket`
- Protocolos TCP e UDP

Não há dependências externas ou necessidade de instalar pacotes adicionais.

## Estrutura do projeto

```text
readme.md
tcp/
	cliente.py
	servidor.py
udp/
	cliente.py
	servidor.py
```

## Como executar

### Pré-requisito

Ter o Python 3 instalado e disponível no terminal.

### 1. Executar o exemplo TCP

Abra dois terminais na pasta do projeto.

No primeiro terminal, inicie o servidor:

```bash
python tcp/servidor.py
```

No segundo terminal, execute o cliente:

```bash
python tcp/cliente.py
```

Digite uma mensagem quando solicitado. O servidor retornará o texto em maiúsculas.

### 2. Executar o exemplo UDP

Abra dois terminais na pasta do projeto.

No primeiro terminal, inicie o servidor:

```bash
python udp/servidor.py
```

No segundo terminal, execute o cliente:

```bash
python udp/cliente.py
```

Digite uma mensagem quando solicitado. O servidor retornará o texto em maiúsculas.

## Observações

- Os exemplos usam a porta `12000`.
- O endereço configurado é `localhost`, então cliente e servidor devem ser executados na mesma máquina.
- Se a porta estiver em uso, altere o valor em ambos os arquivos correspondentes antes de executar.

## Aprendizado esperado

Ao executar este projeto, você verá na prática:

- a abertura e o fechamento de conexões TCP;
- o envio e recebimento de datagramas UDP;
- a diferença entre comunicação orientada a conexão e sem conexão.
