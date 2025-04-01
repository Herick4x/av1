# Dado um array de números, encontre e exiba o maior e o menor valor presentes nele.

def encontrar_maior_menor(arr):
    if len(arr) == 0:
        return None, None  
    maior = menor = arr[0]
    for num in arr:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    return maior, menor

arr = [3, 1, 5, 8, 2, 7]
maior, menor = encontrar_maior_menor(arr)

print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')
