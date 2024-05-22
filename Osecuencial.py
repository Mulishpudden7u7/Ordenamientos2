def busqueda_secuencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# Ejemplo de uso
lista = [2, 5, 7, 10, 12, 15, 20]
elemento = 12
print("El elemento", elemento, "se encuentra en el índice:", busqueda_secuencial(lista, elemento))
