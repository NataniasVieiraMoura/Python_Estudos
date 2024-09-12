
form = []
lista = []
hd = []
cnt = 1
while True:
    nome = str(input("Qual seu nome:")).capitalize()
    idad = int(input("Que ano nasceu?"))
    sex = str(input("Você é Homem ou Mulher?")).upper()[0]
    local = str(input("Onde você nasceu?")).capitalize()
    form = [cnt,[nome,idad,sex,local]]
    lista += form.copy()
    hd += form.copy()
    form.clear()
    cnt += 1
    pso = str(input('Deseja apagar algum dado anteriormente digitado?')).upper()[0]
    if pso == 'S':
        print(lista[:])
        opco = int(input("Digite um número do cadastro que deseja remover:"))
        lista.pop(cnt)
        lista.pop(cnt-1)
    print(lista[:])
    pergunta = str(input('Deseja cotinuar?')).upper()[0]
    if pergunta == 'N':
        break

