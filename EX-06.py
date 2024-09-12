#6 - Desenvolva um programa que leia um número e diga ao usuario se é par ou impar, logo após o programa deve perguntar ao usuário se deseja inserir um novo número ou encerrar o programa. Se o usuário optar por continuar o programa deve repetir o processo, caso contrário, deve encerrar.

while True:
    # Solicita que o usuário insira um número inteiro
    numero = int(input("Digite um número inteiro: "))

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
    
    # Pergunta ao usuário se deseja continuar
    continuar = input("Deseja inserir um novo número? (s para sim, n para não): ").lower()

    # Verifica se o usuário quer encerrar o programa
    if continuar.upper() != 'S':
        print("Encerrando o programa...")
        break
