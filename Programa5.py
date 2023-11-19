def remove_repetidos(lista):
    i = len(lista) - 1
    
    while i >= 0:
        j = i - 1
        
        while j >= 0:
            if lista[j] == lista[i]:
                del lista[i]
                break
            j -= 1
        
        i -= 1
    
    print(lista)

remove_repetidos(lista=[2, 4, 3, 2, 2, 2, 3])
