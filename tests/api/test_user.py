def test_create_user(client):
    response = client.post(
        "/users", json={"email": "e1@e.org", "password": "pass"}
    )
    assert response.status_code == 200
