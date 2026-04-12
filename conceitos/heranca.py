class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5

    def acacelerar(self):
        print("O carro está acelerando...")
    
    def frear(self):
        print("O carro está freando...")
    
    def buzinar(self):
        print("Buzinando...")
   
class Uno(Carro):
    modelo = "Uno"
    marca = "Fiat"
    ano = 1992

uno = Uno()
uno.acacelerar()
print(uno.modelo)