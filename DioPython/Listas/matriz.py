# Matriz Nula:Todos os elementos são zero
print("Matriz nula")
matriz_nula = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Matriz Diagonal:  Matriz quadrada onde todos os elementos fora da diagonal principal são zero.
print("Matriz Diagonal")
matriz_diagonal = [
    [4, 0, 0],
    [0, 5, 0],
    [0, 0, 6]
]

# Matriz Simétrica: 
matriz_simetrica = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

# Matriz Anti-simétrica
matriz_anti_simetrica = [
    [0, -2, 3],
    [2, 0, -1],
    [-3, 1, 0]
]

# Matriz Triangular Superior
matriz_triangular_superior = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

# Matriz Triangular Inferior
matriz_triangular_inferior = [
    [1, 0, 0],
    [2, 3, 0],
    [4, 5, 6]
]


#matriz identidade:Matriz quadrada onde todos os elementos da diagonal principal são 1 e os outros são 0.
print("Matriz identidade")
matriz = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]

print(matriz[0])  # [1, 0, 0, 0]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 0
print(matriz[-1][-1])  # 0