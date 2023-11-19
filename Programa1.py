def pertence(lista, elemento):
    i = 0
    while i != len(lista):
        if lista[i] == elemento:
            return True
        else:
            i += 1
    return False

print(pertence(lista = [2, 3, 4], elemento = int(input("elemento: "))))