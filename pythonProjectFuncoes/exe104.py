


def leiaint(num):
    resposta = ''
    x = 0
    global txt
    if txt.isnumeric() == False:
        while txt.isnumeric() == False:
            txt = input(f'\033[31;1mO valor {txt} digitado não é inteiro {type(txt)}\n.Erro, Digite um valor inteiro:\033[m ')
    if txt.isnumeric():
        resposta = f'O valor {txt} digitado é inteiro :{type(int(txt))}'
        return print(resposta)

print('-'*35)
txt = str(input('Digite um número: '))

leiaint(txt)
