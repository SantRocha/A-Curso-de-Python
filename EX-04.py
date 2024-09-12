#4 - Desenvolva um programa que leia três números fornecidos pelo usuário e determine qual é o maior e qual é o menor entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
# Verifica qual número é o maior
if num1 > num2 and num1 > num3:
    print(f'O maior número é {num1}')
if num2 > num1 and num2 > num3:
    print(f'O maior número é {num2}')
else:
    print(f'O maior número é {num3}')

# Verifica qual número é o menor
if num1 < num2 and num1 < num3:
    print(f"O menor número é {num1}")
elif num2 < num1 and num2 < num3:
    print(f"O menor número é {num2}")
else:
    print(f"O menor número é {num3}")