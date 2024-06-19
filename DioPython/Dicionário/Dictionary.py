#O dicionário é um conjunto de par, chave e valor.

pessoa = {"nome": "Raissa", "idade": 17}
print(pessoa)

pessoa = dict(nome="Raissa", idade=17)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Raissa", "idade": 17, "telefone": "3333-1234"}
print(pessoa)