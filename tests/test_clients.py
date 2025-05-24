def test_create_client(client):
    response = client.post("/clients", json={
        "name": "Client Test",
        "email": "client@test.com",
        "cpf": "12345678900",
        "phone_number": "+5511999999999"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Client Test"

def test_list_clients(client):
    response = client.get("/clients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_client(client):
    response = client.get("/clients/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_client(client):
    response = client.put("/clients/1", json={"name": "Updated Client"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Client"

def test_delete_client(client):
    response = client.delete("/clients/1")
    assert response.status_code == 200
    assert response.json()["msg"] == "Client deleted"
