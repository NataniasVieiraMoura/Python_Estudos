i = f = 0


def leiaint():
        try:
            global x
            x = '-'*35
            print(x)
            global i
            i = int(input('Digite um inteiro: '))
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


def leiafloat():
    try:
        print(x)
        global f
        f = float(input('Digite um real:'))
    except Exception as g:
        print(f'\033[31m Valor digitado errado -> {g.__class__}\033[m')
        print(f'\033[31m A causa do Erro é : {g.__cause__}\033[m')
        print(f'\033[31m O contexto do Erro é : {g.__context__}\033[m')
    except (TypeError):
        print(f'\033[31m O erro foi o tipo digitado.\033[m')
    except (ValueError):
        print(f'\033[31m O erro foi o valor digitado.\033[m')
    except (KeyboardInterrupt):
        print(f'\033[31m O usuário preferiu não digitar.\033[m')
    except (FileNotFoundError):
        print(f'\033[31m Erro de  arquivo não foi encontrado.\033[m')
    else:
        print(f'\033[34m Valor {f} foi salvo com sucesso.\033[m')
    finally:
        print('\033[37mFim do programa.\033[m')


def tudo():
    global i, f
    leiaint()
    leiafloat()
    return print(f'O valor inteiro digitado foi {i} e o real é {f}')

while True:
    tudo()