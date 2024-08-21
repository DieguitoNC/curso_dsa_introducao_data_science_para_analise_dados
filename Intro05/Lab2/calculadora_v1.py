# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!


# A pessoa deve selecionar de com um numero de 1 a 4 o tipo de conta que ela deseja realizar
# A pessoa deve colocar o primeiro numero e depois o segundo numero
# Irá imprimir o "input da conta na tela"
print("\n******************* Calculadora em Python ******************* \n")

type_calc = int(input('\n Digite um numero de 1 a 4 para selecionar a operação que deseja \n 1 - Soma \n 2 - Subtracao \n 3 - Multiplicação \n 4 - Divisão \n'))
num1 = int(input("Digite o primeiro numero que deseja fazer a operacao: "))
num2 = int(input("Digite o segundo numero que deseja fazer a operacao: "))

def calculator(type_calc, num1, num2):
  if type_calc == 1:
    print(num1, "+", num2, "=", (num1 + num2))
  elif type_calc == 2:
    print(num1, "-", num2, "=", (num1 - num2))
  elif type_calc == 3:
    print(num1, "x", num2, "=", (num1 * num2))
  elif type_calc == 4:
    if num2 != 0:
      print(num1, "/", num2, "=", (num1 / num2))
    else:
      print("O numero nao pode ser dividido por zero")
  else:
    return ("Algum erro aconteceu !")

calculator(type_calc, num1, num2)

  

