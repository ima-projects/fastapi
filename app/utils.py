from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Hashing each user password stored in database
def hash(password: str):
    return pwd_context.hash(password)

#Hashing the attempted (raw) password sent by user and comparing it to the hashed password in the database
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
