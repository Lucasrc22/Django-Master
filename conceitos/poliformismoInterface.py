class Forma:
    # O método area é definido como um método abstrato, ou seja, 
    # ele não tem uma implementação concreta na classe Forma. 
    # Ele é apenas um contrato que as subclasses devem cumprir, 
    # implementando o método area de acordo com suas próprias características.
    def area(self):
        pass


class Quadrado(Forma):
    # O método __init__ é o construtor da classe, que é chamado quando um objeto é criado.Quando um objeto da classe Quadrado é 
    # criado, o valor do lado é passado como argumento e armazenado no atributo self.lado
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return 3.14 * self.raio * self.raio
    

quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(area_quadrado)

quadrado2 = Quadrado(10)
area_quadrado2 = quadrado2.area()
print(area_quadrado2)

Circulo = Circulo(3)
area_circulo = round(Circulo.area(), 2)

print(area_circulo)