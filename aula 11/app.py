try:  # tentar
    numero1 = int(input('Digite um número:'))
    print(numero1)
    numero2 = int(input('Digite um número:'))
    print(numero2)
    
    operacao = str(input('Qual operação deseja fazer?'))
    
    if operacao =='+':
        result = numero1+numero2
        print(f"O resultaeo da soma é: {result}")

    elif operacao =='-':
        result = numero1-numero2
        print(f"O resultado da subtração é: {result}")
    
except:  # excessão
    print('Digite um valor válido:')
    
finally:
    print('Deu certo!')