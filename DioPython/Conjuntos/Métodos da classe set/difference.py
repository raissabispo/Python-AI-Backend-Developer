# Difference: Diferença entre conjuntos, elementos que pertencem somente ao primeiro conjunto

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b) # A - B = {1}
print(resultado)

resultado = conjunto_b.difference(conjunto_a) # B - A = {4}
print(resultado)