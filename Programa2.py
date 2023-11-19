def posicoes_lista(lista, elemento):
    nova_lista = []
    for i in range(len(lista)):
        if lista[i] == elemento:
            nova_lista.append(i)
    return nova_lista

print(posicoes_lista(lista = ['a', 2, 'b', 'a'], elemento = input("Elemento: ")))