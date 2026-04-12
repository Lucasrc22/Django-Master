class Animal:
    def emitir_som(self):
        print("O animal emite um som genérico.")
    

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro late: Au Au!")

class Gato(Animal):
    def emitir_som(self):
        print("O gato mia: Miau!")

cachorro = Cachorro()
cachorro.emitir_som()

gato = Gato()
gato.emitir_som()