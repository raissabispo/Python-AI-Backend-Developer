#Maiusculo, Minusculo e titulo
nome = "Vitória"

print(nome.upper()) #Maiuscula
print(nome.lower()) #Minuscula
print(nome.title()) #titulo

#Eliminandoo os espaços em branco

texto = "  Olá Mundo    "
print(texto.strip())
print(texto.rstrip())

#junçoes e centralizacao
menu = "Python"
print("####" + menu +" #####")
print(menu.center(14))
print(menu.center(14, "#"))