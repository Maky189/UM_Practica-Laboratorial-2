def parte(lista, e):
    parte1 = []
    parte2 = []
    for i in range(len(lista)):
        if lista[i] >= e:
            parte2.append(lista[i])
        else:
            parte1.append(lista[i])
    print(parte1)
    print(parte2)
    
    
lista = []
tamanho_da_lista = int(input("tamanho da sua lista: "))

for i in range(tamanho_da_lista):
    lista.append(int(input(f"Numero {i + 1} da lista:")))
print(lista)

e = int(input("elemento: "))
parte(lista, e)
