import pytest 
from app import schemas
from . database import client,session

@pytest.fixture
def test_user(client):
    user_data = {"email": "aditra@gmail.com", "password": "surya"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    print(res.json())
    return 



# def test_root(client):
#     res = client.get("/")
#     print(res.json().get("message"))
#     assert res.json().get("message") == "Hi JS !!"
#     assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "aditra@gmail.com", "password": "surya"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "aditra@gmail.com"
    assert res.status_code == 201


def test_login_user(client,test_user):
    res = client.post("/login", data={"username": "aditra@gmail.com", "password": "surya"})
    print(res.json())
    assert res.status_code == 200
