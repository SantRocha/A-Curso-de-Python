#5 - Escreva um programa que leia um número inteiro que representa a quantidade de números seguintes que o programa deve ler. Após ler esses números, o programa deve calcular e mostrar a soma apenas dos números pares inseridos.

# Solicita que o usuário insira a quantidade de números a serem lidos
quantidade = int(input("Digite a quantidade de números que deseja inserir: "))

# Inicializa a variável para armazenar a soma dos números pares
soma_pares = 0

# Usa um loop para ler os números inseridos pelo usuário
for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1}º número: "))
    
    # Verifica se o número é par
    if numero % 2 == 0:
        soma_pares += numero

# Exibe o resultado da soma dos números pares
print(f"A soma dos números pares é: {soma_pares}")
