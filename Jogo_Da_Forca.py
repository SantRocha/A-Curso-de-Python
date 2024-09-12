"""
7 - Crie o jogo da forca que funciona da seguinte forma:
 O programa deve selecionar uma palavra secreta que o jogador deve adivinhar.
 A palavra deve ser exibida ao jogador com todas as letras ocultas por (_).
 Cada letra adivinhada corretamente deve substituir o underscore correspondente na palavra exibida.
 O programa deve contar quantas tentativas o jogador ainda possui.
 O jogo termina quando o jogador adivinha todas as letras da palavra secreta ou quando o número máximo de tentativas erradas é alcançado (derrota)."""
 
import palavra_secreta  # Importa o módulo que contém a lista de palavras
import random    # Importa o módulo random para seleção aleatória

# Seleciona uma palavra aleatória da lista 'palavra' no módulo 'palavra_secreta'
pala = palavra_secreta.palavra[random.randrange(len(palavra_secreta.palavra))]

# Inicializa um conjunto vazio para armazenar as letras já tentadas pelo jogador
letra_digitada = set()

# Define o número inicial de erros permitidos
erro = 5

# Loop principal que continua enquanto o número de erros for maior que 0
while erro > 0:
    # Exibe a palavra, mostrando as letras adivinhadas e sublinhados para as não adivinhadas
    print(' '.join([letra if letra in letra_digitada else '_ ' for letra in pala]))
    
    # Solicita que o jogador insira uma letra
    tentativa = input('Digite uma letra: ')
    
    # Verifica se a entrada do jogador é válida (apenas uma letra e que seja alfabética)
    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Por favor, digite apenas uma letra alfabética.")  # Mensagem de erro para entradas inválidas
        continue  # Volta ao início do loop para solicitar nova entrada
    
    # Verifica se a letra já foi tentada antes
    if tentativa in letra_digitada:
        print("Você já tentou essa letra. Tente outra.")  # Avisa o jogador que a letra já foi usada
        continue  # Volta ao início do loop para solicitar nova entrada
    
    # Adiciona a letra tentada ao conjunto de letras já digitadas
    letra_digitada.add(tentativa)
    
    # Verifica se a letra está na palavra escolhida
    if tentativa in pala:
        print(f'\nA letra {tentativa} existe na palavra!')  # Mensagem de sucesso para a tentativa correta
        
        # Verifica se todas as letras da palavra foram adivinhadas
        if all(letra in letra_digitada for letra in pala):
            print(f'Parabéns! Você venceu! A palavra era {pala}')  # Mensagem de vitória
            break  # Sai do loop, já que o jogador venceu
    else:
        # Caso a letra não esteja na palavra, decrementa o número de tentativas restantes
        erro -= 1
        print(f'\nA letra {tentativa} não existe na palavra!')
        print(f'Você tem {erro} tentativas restantes.')  # Informa o jogador quantas tentativas ainda restam

# Caso o número de erros chegue a zero, o jogador perde o jogo
if erro == 0:
    print("Você perdeu!")  # Exibe a mensagem de derrota
