# funções
def lista():
    print('Gilmar')
    print('31 anos')
    print('Solteiro')


lista()


def soma_num(numerox, numeroy):
    return numerox + numeroy


resultado = soma_num(15, 20)
print(resultado)
resultado2 = soma_num(3, 6)
print(resultado2)


def lista_num_maior(lista):
    lista.sort()#coloca em ordem crescente
    lista.reverse()#inverte a ordem da lista
    maior = lista[0]#pega o primeiro indice da lista, o maior
    return maior #retorna


result = lista_num_maior([1, 2, 3, 4, 5, 60, 75, 8, 9])
print(result)
