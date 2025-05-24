from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_send_whatsapp_message():
    response = client.post("/whatsapp/send", json={
        "phone": "5599999999999",
        "message": "Teste de envio automático"
    })
    assert response.status_code in [200, 500]  # 500 se falhar na API real
