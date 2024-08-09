def test_create_user(client):
    response = client.post(
        "users", json={"email": "e1@e.org", "password": "pass"}
    )
    assert response.status_code == 200



def test_create_user_dublicate(client):
    client.post(
        "users", json={"email": "e1@e.org", "password": "pass"}
    )
    response =  client.post(
        "users", json={"email": "e1@e.org", "password": "pass"}
    )
    assert response.status_code == 400
