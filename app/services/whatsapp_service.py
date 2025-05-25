import os
import requests
from app.core.logger import logger
from app.core.config import settings

class WhatsAppService:
    def __init__(self):
        self.token = settings.WHATSAPP_TOKEN
        self.phone_number_id = settings.WHATSAPP_PHONE_NUMBER_ID
        self.api_url = settings.WHATSAPP_API_URL
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def send_message(self, to: str, message: str):
        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {"body": message}
        }

        try:
            response = requests.post(self.api_url, json=payload, headers=self.headers)
            response.raise_for_status()
            logger.info(f"Mensagem enviada com sucesso para {to}")
            return {"status": "success", "message_id": response.json().get("messages", [{}])[0].get("id")}
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao enviar mensagem para {to}: {e}")
            return {"status": "error", "detail": str(e)}

whatsapp_service = WhatsAppService()
