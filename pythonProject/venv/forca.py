import random

def jogar():

    print("*************")
    print("Bem vindo no jogo da Forca!")
    print("*************")

    palavra_secreta = "banana"
    letras_acertas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip()

        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertas[posicao] = letra
            posicao = posicao + 1

        print(letras_acertas)

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()