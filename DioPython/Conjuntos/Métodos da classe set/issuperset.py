#issuperset: é usada para verificar se um conjunto é um superconjunto de outro

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  
print(resultado) # False

resultado = conjunto_b.issuperset(conjunto_a)  #A ⊇ B
print(resultado) # True