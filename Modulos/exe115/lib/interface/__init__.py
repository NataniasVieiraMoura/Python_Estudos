i = f = 0


def leiaint():
        try:
            linha()
            i = int(input('\033[33mDigite um inteiro: \033[m'))
        except Exception as e:
            print(f'\033[31m Valor digitado errado -> {e.__class__}\033[m')
            print(f'\033[31m A causa do Erro é : {e.__cause__}\033[m')
            print(f'\033[31m O contexto do Erro é : {e.__context__}\033[m')
        except (TypeError):
            print(f'\033[31m O erro foi o tipo digitado.\033[m')
        except (ValueError):
            print(f'\033[31m O erro foi o valor digitado.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31m O usuário preferiu não digitar.\033[m')
        except (FileNotFoundError):
            print(f'\033[31m Erro de  arquivo não foi encontrado.\033[m')
        else:
            print(f'\033[34m Valor {i} salvo com sucesso.\033[m')
        finally:
            print('Fim do programa.')




def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cnt = 0
    cabeçalho('Menu Principal')
    for x in lista:
        cnt += 1
        print(f'\033[33m{cnt}\033[m - \033[34m{x}\033[m')
    print(linha())
    opc = leiaint()
    return opc


