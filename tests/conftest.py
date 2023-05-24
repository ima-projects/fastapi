# any fixtures defined in this file will automatically be accessible to any of my tests within this package and its subpackages
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app

from app.config import settings
from app.database import get_db
from app.oauth2 import create_access_token
from app import models
from app.database import Base
#from alembic import command

# fixture function = change in behaviour so model (SQLAchemy model) or if no model then the fixture is defining the state/behaviour of something before being executed within a test case
# test function = contract/data validation (Pydantic schema)

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:mydbpassword@localhost:5432/fastapi_test'

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# creates the tables e.g. posts, users, votes
# Base.metadata.create_all(bind=engine)


# overiding the original database.py in 'app' directory so the new Session object can point to a new Postgres database instead of the old one
# that is why the 'get_db' dependency was set up when first configuring the database and (adding it to the routes) so that I can easily test this during testing by using the overide functionality that is used within FastAPI. The TestClient will now use the new database.
# def overide_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# the 'session' fixture is ran first, then the 'client' fixture
# Database object fixture: contains the logic of the database object
@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine) # allows me to drop my tables after the test finishes which allows me to start with a clean slate again and no more IntegrityErrors
    # tables are dropped first bc this way when I pass the '-x' flag in my pytest command, it will stop it after it fails but its going to keep the table up so I can see the current state of the test database when the test failed and troubleshoot a little more
    Base.metadata.create_all(bind=engine) # allows me to create my tables again
    # yield instead of return the TestClient and allow me to run my code before I run my test (above)
    #command.upgrade("head") # (alembic) this will build out all the tables for me  
    db = TestingSessionLocal() # this is the database object used for querying. This is returned then db object is passed to the 'client' fixture as session and then db overiden with the test db in client function
    try:
        yield db
    finally:
        db.close()


# returning the TestClient instance (the app) to ensure that this is a different instance of the app that is being tested on
@pytest.fixture()
def client(session):
    def overide_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = overide_get_db
    yield TestClient(app)
    # I can then run my code after my test finishes
    #command.downgrade("base") # alembic must be set up with all the right environment variables


    # fixture creates a new user for the test_login_user function so it doesn't have to rely on test_create_user function (test case)
@pytest.fixture
def test_user(client):
    user_data = {"email": "ibti123@gmail.com", "password": "password123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

# second test user fixture which will be used in test case where user tries to delete another users post
@pytest.fixture
def test_user2(client):
    user_data = {"email": "sam123@gmail.com", "password": "password123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


# returning a token to the test function in test_posts.py
@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})

# gives an authenticated 'app' client (a new instance of the FastAPI app built) - so anytime i'm dealing with any path operations that require authentication, I can just call the authorized_client instead of the regular client which in going to save a lot of time
@pytest.fixture
def authorized_client(client, token):
    client.headers ={
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client

# the same test user is creating 3 posts here
# If called it will return a SQLAlchemy model as a respose
@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [{
        "title": "first title",
        "content": "first content",
        "owner_id": test_user['id']
    },{
        "title": "2nd title",
        "content": "2nd content",
        "owner_id": test_user['id']
    },{
        "title": "3rd title",
        "content": "3rd content",
        "owner_id": test_user['id']
    },
        {"title": "3rd title",
        "content": "3rd content",
        "owner_id": test_user2['id']
    }]

# SQLAlchemy models used to implement models in test db and serialise password in db. 
# the post argument is referring to a single post from posts_data list item and then transformed into the Post model sqlalchemy format to be mapped to the database (schema with hard-coded values example below)
    def create_post_model(post):
        return models.Post(**post)

# the map function converts all of them to Post models but it doesn't return a list (it returns a map)
    post_map = map(create_post_model, posts_data)
    # to convert to list
    posts = list(post_map)
    session.add_all(posts)


    # session.add_all([models.Post(title="first title", content="first content", owner_id=test_user['id']), 
    #                  models.Post(title="2nd title", content="2nd content", owner_id=test_user['id']),
    #                  models.Post(title="3rd title", content="3rd content", owner_id=test_user['id']),
    #                 ])
    session.commit()
    
    posts = session.query(models.Post).all()
    return posts