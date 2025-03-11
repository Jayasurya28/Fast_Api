from app import schemas
from . database import client,session

def test_root(client):
    res = client.get("/")
    print(res.json().get("message"))
    assert res.json().get("message") == "Hi JS !!"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "aditra@gmail.com", "password": "surya"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "aditra@gmail.com"
    assert res.status_code == 201


def test_login_user(client):
    res = client.post("/login", data={"username": "aditra@gmail.com", "password": "surya"})
    print(res.json())
    login_res = schemas.Token(**res.json())
    payload = oauth2.decode_token(login_res.access_token)
    id = payload.get("user_id")
    assert id == 1
    assert login_res.token_type == "bearer"
    assert res.status_code == 200
