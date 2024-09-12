'''Erros e Execeções'''
#help(Error)#'''Ctrol+barra(espaço)'''
try:
    print('''\033[7;1mO Try é onde você declarará 
o programa que pode funcionar ou não\n\033[m''')
    print(x)
except Exception as erro:
    print(f'''\033[31;1mO except é onde você vai dizer o que
fazer quando o programa escrito no try der erro
.Imfelizmente o programa deu erro º:(, nesse caso
=>>>x não foi declarado >>{erro.__class__}\033[m''')
except ZeroDivisionError:
    print(f'A divisão por zero não existe!>:(')
except (ValueError, TypeError):
    print(f'Você digitou o tipo de dado errado.')
    print(f'O erro é de {TypeError}')
    print(f'O erro é de {ValueError}')
except KeyboardInterrupt:
    print('Os dados não foram imformados(só deu enter!)')
else:
    print('''\033[34;1mO else é onde você vai dizer o que o programa
vai fazer caso dê certo o programa escrito no try\033[m''')
finally:
    print('''\033[37;1mO finally é onde você vai dizer o que o programa
vai fazer caso dê Certo ou Não.\033[m''')


#help(Exception.__class__)

#help(Exception.__cause__)

#help(Exception.__context__)

#help(Exception.__module__)


print(type(2.3))
f = 4.3
print(type(str(f)))