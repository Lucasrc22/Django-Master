class Celular:
    marca = "Iphone"
    modelo = "14 Pro Max"
    cor = "Dourado"
    memoria = "512GB"
    
    def fazer_ligacao(self):
        print("Fazendo ligação...")
    
    def jogar(self):
        print("Jogando...")
    
    def despertador(self):
        print("Despertador tocando...")
    
    def calcular(self, a, b):
        return a + b




celular = Celular()
print(celular.marca)
print(celular.modelo)
print(celular.cor)
print(celular.memoria)
celular.fazer_ligacao()
celular.jogar()
celular.despertador()

print(celular.calcular(5, 10))
