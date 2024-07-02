class Bicicleta: #classe
    def __init__(self,cor,modelo,ano,valor): #Construtor
     self.cor = cor
     self.modelo = modelo
     self.ano = ano
     self.valor = valor
     
     
    def buzinar(self): #Metodos
        print("plim...plim")
    def parar(self):
        print("Parando bicleta")
        print("bicicleta parada")
    def correr(self):
        print("vrummmmmmmmmmmmmmm...")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
     
     
b1 = Bicicleta("rosa", "caloi", "2015","900")
b1.buzinar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
   

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()  
  