maior_idade = 18 
idade_especial = 12
idade = int(input("Informe sua idade:"))

if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH")
    
elif idade == idade_especial:
    print("Pode fazer aulas teórias, mas não aulas práticas")
    
else:
    print("Menor de idade, ainda não pode tirar a CNH")