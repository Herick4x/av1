#Desloque todos os elementos de um array para a direita (ou esquerda).
*def deslocar_array(array, direcao):
    if direcao == "direita":
        return [array[-1]] + array[:-1]
    elif direcao == "esquerda":
        return array[1:] + [array[0]]
    else:
        raise ValueError("A direção deve ser 'direita' ou 'esquerda'.")

array = [1, 2, 3, 4, 5]
array_direita = deslocar_array(array, "direita")
print("Deslocado para a direita:", array_direita)
