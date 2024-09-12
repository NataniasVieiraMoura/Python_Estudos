def dollar():
    contador = 0
    import requests
    dados = list
    # URL da API do BCB para cotação do dólar
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json"

    try:
        response = requests.get(url)

        # Verifique se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            data = response.json()
            # A cotação mais recente estará no último elemento da lista
            ultima_cotacao = data[-1]
            data_cotacao = ultima_cotacao['data']
            valor_cotacao = ultima_cotacao['valor']
            dados = data
            print(f'Cotação do dólar em {data_cotacao}: R$ {valor_cotacao}')
            #print(data)
        else:
            print('Erro ao obter a cotação do dólar. Código de status:', response.status_code)

    except requests.exceptions.RequestException as e:
        print('Erro na solicitação:', e)
    '''criar uma lista dado com as datas para pk e outra para os dados'''
    cnt = 0
    datas = list()
    valor = list()
    contador = len(dados)
    while cnt < contador:
        datas.append(dados[cnt]['data'])
        valor.append(dados[cnt]['valor'])
        cnt += 1
    #print(datas[:])
    #print(valor[:])
    #print(contador)
    import pandas as pd
    from pandas import DataFrame
    import numpy as np
    from numpy import sum, mean
    df = pd.DataFrame({
        'Datas': datas[:],
        'Valor': valor[:]
    })
    print(df)
dollar()

#x = [{'gas':1506},{'metal':954},{'tos':965}]
#print(x[1]['metal'])