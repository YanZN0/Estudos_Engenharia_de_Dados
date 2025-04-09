lista_numeros: list = [40,50,60,70,0,-400000,1,50]


def ordenar_lista_numeros(numeros: list) -> list:
    nova_lista_numeros = numeros.copy()
    for i in range(len(nova_lista_numeros)):
        for j in range(i+1, len(nova_lista_numeros)):
            if nova_lista_numeros[i] > nova_lista_numeros[j]:
             nova_lista_numeros[i], nova_lista_numeros[j] = nova_lista_numeros[j], nova_lista_numeros[i]

    return nova_lista_numeros
nova_lista = ordenar_lista_numeros(lista_numeros)
print(nova_lista)