from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.whatsapp_service import send_whatsapp_message

router = APIRouter()

class WhatsAppMessage(BaseModel):
    phone_number: str  # E.164 format, e.g., +5511999999999
    message: str

@router.post("/whatsapp/send")
async def send_whatsapp(msg: WhatsAppMessage):
    try:
        response = await send_whatsapp_message(msg.phone_number, msg.message)
        return {"msg": "Message sent", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
