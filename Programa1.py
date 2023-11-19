def pertence(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

print(pertence(lista = [2, 3, 4], elemento = int(input("elemento: "))))