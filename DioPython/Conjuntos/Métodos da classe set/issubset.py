#Issubset: é usada para verificar se um conjunto é subconjunto de outro.

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b) #A ⊆ B
print(resultado)  # True

resultado = conjunto_b.issubset(conjunto_a)  
print(resultado) # False