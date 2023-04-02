from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

print(settings.database_username)

# no longer need this command now that I have Alembic. This is the command that tells SQLAlchemy to run the create statement so that it generated all the tables when it first started up but since we have Alembic now, you no longer need this command however if I keep it in it's not going to break anything but if it does create the tables for you then your first Alembic migration isn't going to do anything so probs best to comment it out
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# lists of urls that can talk to this api. "*" means every single origin. 
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# original in memory posts array before database
# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#              {"title": "favorite foods", "content": "I like pizza", "id": 2}]

# two functions below no longer needed because they were before I was working with databases
# def find_post(id):
#     for p in my_posts:
#         if p ['id'] == id:
#             return p
        
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello world"}

