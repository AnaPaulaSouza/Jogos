import forca
import adivinhacao

def escolher_jogo():
    print("Escolhe o seu jogo!")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo quer jogar? "))

    if(jogo == 1):
        print("Jogar forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogo()