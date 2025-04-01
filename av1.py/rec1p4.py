#Escreva um programa que inverta a ordem dos elementos de um array.

def inverter_array(arr):
    return arr[::-1]

arr = [3, 1, 5, 8, 2, 7]
arr_invertido = inverter_array(arr)

print(f'Array original: {arr}')
print(f'Array invertido: {arr_invertido}')
