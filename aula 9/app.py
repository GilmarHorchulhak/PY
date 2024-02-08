# EXEMPLO 1


'''i = 1
while i < 10:  # até que i=10
    print(i)
    i += 1
print('terminou')
print(i)'''


# EXEMPLO 2


'''lista = ["azul", "amarelo", "vermelho"]

for item in lista:  # percorre os itens de uma lista
    print(item)'''

# EXEMPLO 3


'''palavra = "Gilmar"

for letra in palavra:  # percorre as letras de uma palavra
    print(letra)

for index in range(10, 20, 2):  # range(inicio,fim,passos)
    print(index)

for index in range(5):  # range(fim)
    print(index)

for index in range(len(palavra)):  # range
    print(palavra[index], index)'''

# EXEMPLO 4


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for linha in matriz:
    print("---")
    for coluna in linha:
        print(coluna)#imprime as linhas da matriz