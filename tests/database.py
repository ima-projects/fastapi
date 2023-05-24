from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app

from app.config import settings
from app.database import get_db
from app.database import Base
#from alembic import command

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
