from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)

#this is going to be a post operation bc we have to send some information to the server
@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    # if vote does not exist
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first() # trying to grab first post
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {vote.post_id} does not exist") 
    
   
    #defining query to see if vote already exists
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id) # here in the first check we are trying to see if there is already a vote for a specific id. However, second check accounts for the fact that multiple people can vote on the same post. therefore two conditions are needed. Not querying the database yet, just building out the query - checks to see if this specific user has voted or liked this post already #

    #performing the query:
    found_vote = vote_query.first()
    
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted on post {vote.post_id}") 
        # if vote not found
        new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id) 
        # adding to database
        db.add(new_vote)
        db.commit()
        return {"message": "sucessfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")
        
        # if vote is found then you have to delete it
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "succesfully deleted vote"}