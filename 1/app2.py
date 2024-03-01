numero1=int(input('Digite um número: '))
#a variável numero1 armazena o valor digitado na fomra de um numero inteiro.
numero2=int(input('Digite outro número: '))
# a variável numero2 armazena o valor digitado na forma de um numero inteiro.
operacao = input('Qual a operação?')
# a operação o usuário insere a operação matemática.
if operacao=='+':
    #se a operação for de soma, executa a soma
    resultado = numero1 + numero2
elif operacao=='-':
    # se a operação for subtração executa a subtração
    resultado= numero1 - numero2

elif operacao=='/':
    resultado= numero1 / numero2
    
print(resultado)
#mostra o resultado na tela
