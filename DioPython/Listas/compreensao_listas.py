#filtr0: todos os números ínpares:

numeros = [11, 24, 33, 45, 66, 78, 21]

inpares =[]

for numero in numeros:
    if numero % 2 != 0:
        inpares.append(numero)
        print(inpares)
        

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)