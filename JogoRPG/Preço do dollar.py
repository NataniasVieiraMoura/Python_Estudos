import requests


def obter_taxa_dolar():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erros na solicitação HTTP
        data = response.json()

        # A API do BACEN retorna uma lista de objetos JSON, onde cada objeto contém informações sobre a taxa de câmbio em um dia específico.
        # Vamos considerar o último registro disponível.
        if data:
            ultimo_registro = data[-1]
            data_referencia = ultimo_registro["data"]
            taxa_dolar = ultimo_registro["valor"]
            print(f"Data de referência: {data_referencia}")
            print(f"Taxa de câmbio do dólar: R$ {taxa_dolar}")
        else:
            print("Nenhum dado disponível.")

    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação HTTP: {e}")
    except KeyError:
        print("Erro ao analisar os dados da API.")


if __name__ == "__main__":
    obter_taxa_dolar()


# passo a passo para baixar uma biblioteca no python:
'''    Abra o projeto no PyCharm no qual você deseja instalar a biblioteca.

    No menu superior, vá para "File" (Arquivo) > "Settings" (Configurações) no Windows/Linux ou "PyCharm" > "Preferences" no macOS.

    Na janela de configurações, expanda a seção "Project" (Projeto) e selecione "Python Interpreter".

    Na parte superior direita dessa janela, você verá uma lista suspensa que mostra o interpretador Python atualmente em uso pelo projeto. Clique nele para abrir o gerenciador de pacotes.

    No gerenciador de pacotes, você verá uma lista de bibliotecas Python já instaladas no projeto. Para adicionar uma nova biblioteca, clique no ícone "+" no canto inferior esquerdo da janela.

    Na caixa de diálogo "Available Packages" (Pacotes Disponíveis), você pode pesquisar a biblioteca que deseja instalar. Digite o nome da biblioteca na caixa de pesquisa.

    Quando encontrar a biblioteca desejada na lista, selecione-a clicando sobre ela e, em seguida, clique no botão "Install Package" (Instalar Pacote) no canto inferior direito.

    O PyCharm instalará automaticamente a biblioteca e você verá o progresso da instalação na parte inferior da janela.

    Uma vez instalada, a biblioteca aparecerá na lista de bibliotecas instaladas para o projeto.

    Clique em "OK" para fechar a janela de configurações.'''