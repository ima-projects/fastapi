from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

#all of this code applies where anytime we have a specific endpoint that needs to be protected i.e. user needs to be logged in to use it, 
# we're going to expect them to provide an access token e.g. users who want to create a post need to be logged in and you do that by adding an extra dependency (Depends) into the path operation function in post.py 
# (the function get_current_user is the dependency)

#passing in login endpoint from router
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

#JWT properties
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

#token payload in data variable made into a copy to avoid changing
def create_access_token(data: dict):
    to_encode = data.copy()

#obtaining current time and then adding 30 min
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


# function to verify the access token sent back by client
# this is also code that can error out (as evidenced by the credentials_exception which shows when token (not input just token) provided by user is invalid)
# so make so to add in a try: statement
# token comes from the client request
# Basically function gets token data (which is atm the id)
def verify_access_token(token: str, credentials_exception):

    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        #pydantic schema from client request
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    
    return token_data

# get_current_user function executes verify_access_token, verify_access_token extracts id from token. get_current_user then automatically fetches the user from the database and add user as a parameter into our path operation function (inside current_user parameter as oauth2_scheme - token passed to get current user in def in post.py) but current user parameter not called
# get_current_user also defines the credentials_exception that will be passed in to the verify_access_token function
# Basically function returns user from database so to attach user to path operation in order to perform any neccessary logic automatically w/o each path operation having to do it themselves (which they already do)
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

#returning a call to our verify access token function. get_current_user is the actual function that calles verify_access_token
    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    
    return user