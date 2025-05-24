def test_register_user(client):
    response = client.post("/auth/register", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert response.json()["msg"] == "User created successfully"

def test_login_user(client):
    response = client.post("/auth/login", json={
        "username": "testuser",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
