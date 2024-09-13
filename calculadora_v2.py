saida = ''

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'Não foi possível realizar a divisão por 0'
    else:
        return a / b

def calculadora(numero1, numero2, operador):
    if operador == '+' or operador.lower() == 'adição':
        resultado = adicao(numero1, numero2)
        return resultado
    elif operador == '-' or operador.lower() == 'subtração':
        resultado = subtracao(numero1, numero2)
        return resultado
    elif operador == '*' or operador.lower() == 'multiplicação':
        resultado = multiplicacao(numero1, numero2)
        return resultado
    elif operador == '/' or operador.lower() == 'divisão':
        resultado = divisao(numero1, numero2)
        return resultado
    else:
        resultado = 'Operação inválida'
        return resultado
while saida.lower() != 'n':
    try:
        numero1 = float(input('Digite o primeiro número:'))
        numero2 = float(input('Digite o segundo número:'))
        operador = input('Digite o operador desejado (+, -, *, / ou \
                         adição, subtração, multiplição, divisão): ')
    
        resultado = calculadora(numero1, numero2, operador)
        print(f'Resultado da operação: {resultado}')
        
        saida = input('Deseja continuar? (S/N):').strip()

    except ValueError:
        print('Por favor, insira valores numericos válidos.')