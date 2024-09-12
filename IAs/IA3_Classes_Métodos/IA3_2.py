class Habilidade:
    def xis_to(self,dado,estado):#O self representa o objeto ou a instanci de uma classe
        #Refencia a instancia atual da classe
        #É um ponteiro para o objeto atual
        self.inf = dado
        self.dist = estado
        self.resultado = self.inf/ self.dist
        return self.resultado
#a = Habilidade()
#b = a.xis_to(20,2)
'''A cada uso do método, o self armazena os ultimos valores utilizados para as
variáveis locais como inf = 20,dist = 2, resultado = 10'''
#print(a.inf)#Aqui você chama o valor do atributo de um objeto
#print(a.dist)
#print(a.resultado)
#q = a.xis_to(45,4)
#print(a.inf)
#print(a.dist)
#print(a.resultado)
'''Como eu disse, os ultimos dados utilizados no método serão armazenados. No caso será:
    inf = 45
    dist = 4
    resultado = 11.25'''
