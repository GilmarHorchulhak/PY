# listas

familia=["Gilmar","Eliane","Elisiane","Edimar"]
print (familia) #retorna a lista inteira
print (familia[0]) #retorba o valor do indice 0
familia.extend(["Nelci","Valdemar"]) #adiciona uma lista complementar
print(familia)#retorna a lista inteira
familia.insert(2,"cachorro")#insere um ítem no indice 2 da lista existente
print(familia)#retorna a lista inteira
familia.remove("cachorro")#Remove um item da lista
print(familia)#retorna a lista inteira
familia.pop()#Remove o último item da lista
print(familia)#retorna a lista inteira
# familia.clear()#Limpa toda a lista
print(familia)#retorna a lista inteira
print(familia.index("Eliane")) # retorna o indice referente ao nome na lista
print(familia.count("Eliane"))# rotorna o numero de elementos iguais na liista

idade =[1,3,2,5,2,8]
print(idade)
idade.sort()#organiza os dados em ordem
print(idade)  
idade.remove(5)
print(idade)  
idade2=idade #adiciona a lista a uma nova variável, mas não é cópia!
print(idade2)
familia2 = familia.copy()#faz uma cópia
print(idade2)
idadee = (2,4,6,7,3)#lista do tipo Tuples cujos valores não podem ser alterados
print(idadee)