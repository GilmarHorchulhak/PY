
numero1=int(input('Digite um número: '))#a variável numero1 armazena o valor digitado na fomra de um numero inteiro.

numero2=int(input('Digite outro número: '))
operacao = input('Qual a operação?')
if operacao=='+':
    soma = numero1 + numero2
elif operacao=='-':
    soma= numero1 - numero2
    
print(soma)
