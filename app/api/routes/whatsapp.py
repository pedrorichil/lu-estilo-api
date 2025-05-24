from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.whatsapp_service import whatsapp_service

router = APIRouter()

class WhatsAppMessage(BaseModel):
    phone: str
    message: str

@router.post("/whatsapp/send")
def send_whatsapp_message(data: WhatsAppMessage):
    result = whatsapp_service.send_message(data.phone, data.message)
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["detail"])
    return result
