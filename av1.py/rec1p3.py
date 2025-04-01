#Receba um array de números e calcule a média aritmética dos valores
def calcular_media(arr):
    if len(arr) == 0:
        return none
    soma = sum(arr)
    media = soma / len(arr)
    return media

    arr = [9, 9, 9, 8, 8, 8]
    media = calcular_media(arr)
    if media is not none:
        print(f'a media aritmetica é:{media}')
    else: 
        print('o array esta vazio... ')