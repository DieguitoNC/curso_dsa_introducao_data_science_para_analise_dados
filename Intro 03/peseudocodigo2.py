
def check_operator (digit_1, digit_2, operator):
  if operator == 'Soma':
    return digit_1 + digit_2
  elif operator == 'Subtração':
    return digit_1 - digit_2
  elif operator == 'Multiplicação':
    return digit_1 * digit_2
  elif operator == 'Exponenciação':
    return digit_1 ** digit_2
  elif operator == 'Divisão':
    return digit_1 / digit_2
  else:
    return 'Operador inválido'




print('Seja bem vindo a sua calculadora particular')

digit_1 = float(input('Digite o primero número da sua operação: '))
operator = input('Digite o operador que deseja utilizar, sendo possível as opções: Soma, Subtração, Multiplicação, Exponenciação e divisão')
digit_2 = float(input('Digite o segundo número da sua operação: '))

result = check_operator(digit_1, digit_2, operator)

print('O resultado é: ', result)


