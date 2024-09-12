#pp6

'''Aula 9'''
fraze = str('       A formacão vegetal Brasileira é diversificada.       ')
'''Os métodos abaixo não necessitam de importação de biblioteca:'''
'''O texto de exemplo é fraze'''
#print(fraze.strip())
'''linha 6: remove os espaços do texto'''
#print(fraze.lstrip())
'''Linha 8: remove os espaços da esquerda(left:l)'''
#print(fraze.rstrip())
'''Linha 10: remove os espaços da direira(rigth: r)'''
#print(fraze.find('a'))
'''linha 12: indica a posição que aparece pela primeira vez o nome(string) escolhida no texto;
    No python a contagem começa no 0. Cada elemento do texto "fraze" tem uma posição.'''
#print(fraze.count('a'))
'''linha 15: conta a quantidade de vezes que o elemento escolhido aparece no texto escolhido'''
#print(fraze.lower())
'''linha 17: transforma todas as letras do texto em minusculas'''
#print(fraze.upper())
'''linha 19: tranforma todas as letras do texto em maiusculas'''
#print(len(fraze))
'''linha 21: conta a quantidade de todos os elementos no texto(caracteries, espaços, etc..)'''
#print('Trabalho' in fraze)
'''linha 23: retorna true ou false. Pesquisa se há ou não o elemento(no caso Trabalho) na frase'''
#print(fraze.replace('formacão', 'Conposição'))
'''linha 25: método que remove um elemento(formação) do texto e insere outro escolhido(Composição) respectivamente'''
#print(fraze.split())
'''linha 26: esse método insere todos os elementos em uma lista'''
#print('@'.join(fraze))
'''linha 29: insere entre as letras do texto uma váriável'''
#print(fraze.capitalize())
'''linha 31: Coloca a primeira letra do texto em mauisculo e o resto em minusculo'''
#print(fraze.title())
'''linha 33: Todas as primeiras letras de cada palavra do texto fica maiuscula'''
#print(fraze.rfind('a'))
'''linha 35: busca a primeira ocorrencia do elemento escolhido(no caso a) da esquerda 
    para a direita. Retorna a posição contada da esquerda pela direita.'''
'''Atenção: métodos find() e rfind() caso não encontrem o valor digitado, retornaram -1'''
'''Atividade 9:'''


#soid = str(input('Digite seu nome:')).strip()
#print('Seu nome em maiúsculas:{}'.format(soid.upper()))
#print('Seu nome em minúsculas:{}'.format(soid.lower()))
#n = len(soid)
#h = soid.count(' ')
#y = n - h
#so = soid.split()
#sos = len(so[0])
#print('Seu nome têm {} letras.'.format(y))
#print('Seu primeiro é {} e têm {} letras'.format(so[0], sos))


#cos = int(input('Digite um número:'))
#cos = str(cos)
#print(cos.split())
#print('Unidade:{}\nDezena:{}\nCentena:{}\nMilha:{}'.format(cos[3], cos[2], cos[1], cos[0]))

#gha = str(input('Digite o nome da Cidade:')).title().strip()
#k = gha.split()
#print('O nome da Cidade começa com Santo?', 'Santo' in k[0])


#nome = str(input('Digite seu nome:')).strip().title()
#print('Há Silva no seu nome?{}'.format('Silva' in nome))


#cod = str(input('Digite uma frase:')).upper().strip()
#print('Essa frase possui {} letras A'.format(cod.count('A')))
#print('A primeira vez que A aparece é na posição {}'.format(cod.find('A') + 1))
#print('A ultima vez que A aparece é na posição {}'.format(cod.rfind('A') + 1))

#non = str(input('Digite Seu nome:'))
#non1 = non.split()
#print('Sr {}, seu último é {}'.format(non1[0], non1[len(non1) - 1]))
