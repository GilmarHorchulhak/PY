#OPERADORES LÓGICOS
# tenho_sede = True
# if tenho_sede:
#    print('bebe agua')
# else:
#    print('não tenho sede')

tenhoSede = True
tenhoFome = True

if tenhoSede or tenhoFome:  # se senho sede ou fome
    print('vá para a cozinha')
else:
    print('fica sentado')  # se não tenho sede nem fome


if tenhoSede and tenhoFome:  # se tenho sede e tenho fome
    print('vá para a cozinha fazer algo')

elif (tenhoSede) and not (tenhoFome):  # se tenho sede e não tenho fome
    print('só beber agua')

elif not (tenhoSede) and (tenhoFome):  # se não tenho sede e tenho fome
    print('só comer um pão')

else:
    print('fica sentado')  # se não tenho sede nem fome

#OPERADODES DE COMPARAÇÃO
n1 = 5
n2 = 8

if n1 == n2:  # operador igual
    print('O n1 é igual ao n2')
elif n1 != n2:  # diferente
    print('o n1 é diferente do n2')
elif n1 > n2:  # maior
    print(" n1>n2")
elif n1 < n2:  # menor
    print('n1<n2')
elif n1 >= n2:  # maior igual
    print(" n1 maior ou igual a n2")
elif n1 <= n2:  # menor igual
    print('n1 é menor ou iguial a n2')
else:
    print('nada')
