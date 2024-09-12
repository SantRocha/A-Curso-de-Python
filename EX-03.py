#Crie um programa que leia um número inteiro fornecido pelo usuário e determine se ele é par ou ímpar.

# Solicita que o usuário insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

