import re
import requests

def limpar_cnpj(cnpj):
    return re.sub(r'[.\-\/\s]', '', cnpj)

def buscar_dados_receita(cnpj):
    cnpj = limpar_cnpj(cnpj)
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            dados = response.json()

            resultado = {
                "uf": dados.get("uf"),
                "cep": dados.get("cep"),
                "email": dados.get("email"),
                "bairro": dados.get("bairro"),
                "numero": dados.get("numero"),
                "municipio": dados.get("municipio"),
                "logradouro": dados.get("logradouro"),
                "complemento": dados.get("complemento"),
                "razao_social": dados.get("razao_social"),
                "nome_fantasia": dados.get("nome_fantasia"),
                "ddd_telefone_1": dados.get("ddd_telefone_1"),
            }

            return resultado
        else:
            return {"erro": f"Erro {response.status_code} ao consultar CNPJ"}
    except requests.RequestException as e:
        return {"erro": f"Falha na requisição: {str(e)}"}
