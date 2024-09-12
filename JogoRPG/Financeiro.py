import yfinance as yf
import requests


# Função para obter dados de ações
def obter_dados_acoes(symbol):
    try:
        # Criar um objeto para a ação desejada usando a biblioteca yfinance
        acao = yf.Ticker(symbol)

        # Obter informações gerais sobre a ação
        info = acao.info
        nome = info['shortName']
        setor = info['sector']
        preco_atual = info['last_price']

        # Obter o histórico de preços
        historico = acao.history(period='1d')
        maximo = historico['High'][0]
        minimo = historico['Low'][0]

        print(f"Nome da Ação: {nome}")
        print(f"Setor: {setor}")
        print(f"Preço Atual: {preco_atual}")
        print(f"Máximo do Dia: {maximo}")
        print(f"Mínimo do Dia: {minimo}")

    except Exception as e:
        print(f"Erro ao obter dados da ação: {e}")


# Função para obter a taxa de câmbio do dólar
def obter_taxa_dolar():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data:
            ultimo_registro = data[-1]
            data_referencia = ultimo_registro["data"]
            taxa_dolar = ultimo_registro["valor"]
            print(f"Data de Referência: {data_referencia}")
            print(f"Taxa de Câmbio do Dólar: R$ {taxa_dolar}")
        else:
            print("Nenhum dado disponível.")

    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação HTTP: {e}")
    except KeyError:
        print("Erro ao analisar os dados da API.")


if __name__ == "__main__":
    # Exemplo de uso das funções
    obter_dados_acoes("AAPL")  # Exemplo: Ação da Apple
    obter_taxa_dolar()
