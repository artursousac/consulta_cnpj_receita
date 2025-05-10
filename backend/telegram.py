import requests

def enviar_dados_telegram(mensagem, token, chat_id):
    message = mensagem
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Mensagem enviada com sucesso!")
        else:
            print(f"Falha ao enviar a mensagem: {response}")
    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")
