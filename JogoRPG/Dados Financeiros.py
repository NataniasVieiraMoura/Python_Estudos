import requests


def obter_taxa_dolar():
    url_dolar = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json"
    url_selic = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"
    url_ibovespa = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json"

    try:
        # Obter a taxa de câmbio do dólar
        response_dolar = requests.get(url_dolar)
        response_dolar.raise_for_status()
        data_dolar = response_dolar.json()
        if data_dolar:
            ultimo_registro_dolar = data_dolar[-1]
            taxa_dolar = ultimo_registro_dolar["valor"]
            print(f"Taxa de câmbio do dólar: R$ {taxa_dolar}")
        else:
            print("Nenhum dado disponível para a taxa de câmbio do dólar.")

        # Obter a taxa Selic
        response_selic = requests.get(url_selic)
        response_selic.raise_for_status()
        data_selic = response_selic.json()
        if data_selic:
            ultimo_registro_selic = data_selic[-1]
            taxa_selic = ultimo_registro_selic["valor"]
            print(f"Taxa Selic: {taxa_selic}%")
        else:
            print("Nenhum dado disponível para a taxa Selic.")

        # Obter o índice Bovespa (Ibovespa)
        response_ibovespa = requests.get(url_ibovespa)
        response_ibovespa.raise_for_status()
        data_ibovespa = response_ibovespa.json()
        if data_ibovespa:
            ultimo_registro_ibovespa = data_ibovespa[-1]
            valor_ibovespa = ultimo_registro_ibovespa["valor"]
            print(f"Valor do Ibovespa: {valor_ibovespa}")
        else:
            print("Nenhum dado disponível para o Ibovespa.")

    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação HTTP: {e}")
    except KeyError:
        print("Erro ao analisar os dados da API.")


if __name__ == "__main__":
    obter_taxa_dolar()
