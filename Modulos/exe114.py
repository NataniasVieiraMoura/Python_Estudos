import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except Exception as erro:
    print('\033[31mDeu erro')
    print(erro)
    print('O site não pode ser acessado no momento.\033[m')
else:
    print('\033[36mDeu certo')
    print(site.read())
    print('\033[m')
finally:
    print('\033[37mFim!\033[m')
