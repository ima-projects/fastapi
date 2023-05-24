import pytest
from jose import jwt
from app import schemas

from app.config import settings

"""Defining User test cases"""

# testing a specfic path operation on root path (since there is no server running)
# def test_root(client):
#     res = client.get("/")
#     print (res.json().get('message'))
#     assert res.json().get('message') == 'Hello world'
#     assert res.status_code == 200

# now sending a request to create a user (need to include data in the body because instead of using Postman body for storing data in Postgres, I use the json body as this is for testing purposes, Pydantic schema is used for response validation of the properties/keys needed e.g. "email")
def test_create_user(client):
    res = client.post("/users/", json={"email": "hello123@gmail.com", "password": "password123"})
    
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'password123', 403), # 403 = 'Invalid Credentials'
    ('ibti123@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'password123', 422), # with email set to None the api will send back a 422 instead of 403, so 422 would be the right status_code here
    ('ibti123@gmail.com', None, 422) # 422 correct here too (422 = 'Missing fields')
])
# testing to make sure that if an incorrect password is entered, then the test should show 403 error
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})

    assert res.status_code == status_code
    # getting the 'detail' property from json response
    #assert res.json().get('detail') == 'Invalid Credentials'
