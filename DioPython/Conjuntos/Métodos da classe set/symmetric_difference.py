# Diferença simétrica : é um novo conjunto que contém todos os elementos que estão em A ou em B, mas não em ambos.
#A Δ B= (A−B) ∪ (B−A)


conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b) # A Δ B= {1, 4}
print(resultado)