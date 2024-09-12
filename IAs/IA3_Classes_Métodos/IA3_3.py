
'''Método construtor'''
class Monolit:#Atributos são iguais aos parametros das funções, só que para métodos
    def __init__(self,num=int,dec=float):#init é o método construtor
        #Aqui você só definiu  o tipo e não os valores dos atributos
        #Você já pode definir no construtor valores padrões para cada atributo internamente
        self.nota = num#incremento
        self.dc = dec#número de inicio
    def contado(self):#o self chama os atributos padrões definidos pelo construtor
        #Você pode adicionar mais atributos para um método
        self.nota += self.dc
#Com o método construtor eu posso passar atributos padrões diretamente para a classe de um objeto especifico
#objeto = Monolit(20,1)#Aqui você pode definir os atributos para a class desse objeto especificamente
#print(objeto.nota)#aqui o objeto ainda não foi utilizado, logo não há alteração do atributo
#objeto.contado()#aqui o objeto é utilizado pela primeira vez
#print(objeto.nota)
#objeto.contado()#cada execução da class o objeto armazena as alterações
#print(objeto.nota)
#print(" ")
#Cada objeto possui sua própia classe. Cada objeto tem suas própias variáveis, um objeto não interfere outro.
#objeto2 = Monolit(992,23)
#print(objeto2.nota)
#objeto2.contado()
#print(objeto2.nota)


class Tarefa:
    def __init__(self,numero = 10,incremento=3):#definido os atributos padrões pelo construtor
        self.var1 = numero
        self.var2 = incremento
    def cal_culo(self):
        self.var1 += self.var2
#garg = Tarefa()
#print(garg.var1)
#print(garg.var2)
#garg.cal_culo()#O método irá funcionar, pois os atributos já foram definidos internamente pelo construtor
#print(garg.var1)

#print("\033[7m\n\033[m")

#outro_s = Tarefa(76,2)#Os atributos do construtor da classe foram alterados para novos valores
#print(outro_s.var1)
#print(outro_s.var2)
#outro_s.cal_culo()
#print(outro_s.var1)#Com os valores alterados dos atributos padrão, o objeto passa a funcionar por eles
'''Atenção: Objetos não são compartilhados: o que acontece com garg
é independente do que ocorre com outro_s'''

'''
Objeto:
    Métodos;
    Atributos;
Objeto:
    Comportameto;
    Estado;'''



class Haker():
    def __init__(self,cnt = 1, calc =16):
        self.valor = cnt
        self.inc = cnt
        self.v_pot = calc
    def contador(self):
        self.valor = self.valor + self.inc
    def observ(self):
        if(self.valor >= 10):
            print("Seu programa chegou ao liminte de tentativas {}".format(self.valor))
        else:
            print("Pode continuar tentando")
    def c_dora(self,elev):#Esse método recebe uma variável própia
        self.v_pot = self.valor**elev
    def p_drão(self):
        self.contador()#Aqui o método da mesma classe pode ser usado dentro de outro método
        self.c_dora(2)#O método chama outro método e atribui um valor
    def ele_3(self):
        self.contador()
        self.c_dora(3)
obj = Haker()
obj.contador()
print(obj.valor)
obj.observ()
obj.c_dora(2)
print(obj.v_pot)
obj.ele_3()
print(obj.v_pot)
obj.p_drão()
print(obj.v_pot)

oab = Haker(30,4)
oab.contador()
oab.contador()
oab.observ()
oab.p_drão()
print(oab.valor)
print(oab.v_pot)
oab.ele_3()
print(oab.v_pot)
oab.c_dora(10)
print(oab.v_pot)

