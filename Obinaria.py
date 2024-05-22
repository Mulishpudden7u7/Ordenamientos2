def busqueda_binaria(lista, elemento):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Ejemplo de uso
lista = [2, 5, 7, 10, 12, 15, 20]
elemento = 12
print("El elemento", elemento, "se encuentra en el índice:", busqueda_binaria(lista, elemento))
