#import
import random
from os import system, name

def limpa_tela():
  #windows
  if name == 'nt':
    _ = system('cls')

  #Mac ou Linux
  else:
    _=system('clear')





#Função

def game():

  limpa_tela()

  print("\nBem-vindo(a) ao jogo da forca!")
  print("Advinhe a palavra abaixo:\n")

  #lista de palavras para o jogo
  palavras=['banana','abacate','uva','morango','laranja']

  #escolhe randomicamente uma palavra
  palavra = random.choice(palavras)

  #list comprehension
  letras_descobertas = ['_' for letra in palavra]

  #numero de chances
  chances = 6

  #lista para as letras erradas
  letras_erradas = []

  #loop enquanto numero de chances for maior que zero
  while chances > 0:
    #print
    print(" ".join(letras_descobertas))
    print('\nChances restantes:',chances)
    print("Letras erradas:"," ".join(letras_erradas))

    #tentativa
    tentativa = input('\nDigite uma letra: ').lower()

    #condicional
    if tentativa in palavra:
      index = 0
      for letra in palavra:
        if tentativa == letra:
          letras_descobertas[index] = letra
        index +=1
    else:
      chances -=1
      letras_erradas.append(tentativa)
    
    #condicional
    if "_" not in letras_descobertas:
      print("\n Você venceu, a palavra era:",palavra)
      break


  #condicional
  if "_" in letras_descobertas:
    print("\n Você perdeu, a palavra era", palavra)

  
#Bloco main
if __name__ =="__main__":
  game()
  print("\n Parabens. Voce esta aprendendo programacao em Python com a DSA. :)\n")

