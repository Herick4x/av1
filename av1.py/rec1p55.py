#Dado um array de números inteiros, conte quantos são pares e quantos são ímpares.
def contar_pares_e_impares(array):
    pares = 0
    impares = 0
    for numero in array:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares, impares = contar_pares_e_impares(array)
print(f'Pares: {pares}, Ímpares: {impares}')
