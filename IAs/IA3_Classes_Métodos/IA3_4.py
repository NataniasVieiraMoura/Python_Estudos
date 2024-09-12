'''Herança'''
class Calculadora(Haker):#para uma classe herdar os métodos que a outra tem
    pass#adicione o pass para indicar que você quer herdar os atributos
    def decremento(self):
        self.valor -= 1
    def apagar(self):
        self.valor = 0
    #A classe calculos herda os métodos da classe Haker
c = Calculadora()
print(c.valor)
c.contador()
c.contador()
print(c.valor)
c.c_dora(4)
print(c.v_pot)
print(c.valor)
c.ele_3()
print(c.valor)
print(c.v_pot)
c.p_drão()
print(c.valor)
print(c.v_pot)
c.observ()
c.decremento()
c.decremento()
c.decremento()
print(c.valor)
