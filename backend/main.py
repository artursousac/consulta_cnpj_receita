from telegram import enviar_dados_telegram
from receita import buscar_dados_receita
from dotenv import load_dotenv
import os

load_dotenv()
token_telegram = os.getenv("TOKEN_TELEGRAM")
chat_id_telegram = os.getenv("CHAT_ID")

enviar_dados_telegram(buscar_dados_receita("07234009000106"), token_telegram, chat_id_telegram)
