nome = "Raissa"
idade = 17
profissao = "Programadora"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Raissa", "idade": 17} #dicionario

print("Nome: %s Idade: %d" % (nome, idade)) #Old style

print("Nome: {} Idade: {}".format(nome, idade)) #Metódo Format

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}") #f-string
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")