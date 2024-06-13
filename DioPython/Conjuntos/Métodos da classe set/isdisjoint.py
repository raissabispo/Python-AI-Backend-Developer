#isdisjoint é usado para verificar se dois conjuntos são disjuntos, ou seja, se eles não têm nenhum elemento em comum.


conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b) #A ∩ B = ∅
print(resultado)  # True

resultado = conjunto_a.isdisjoint(conjunto_c)  
print(resultado) # False