import pytest
from app import models

# this fixture displays a vote that has been made by the user (SQLAlchemy)
# authorized_client not needed because the vote will be changed in the database directly and no api request is being made in the fixture
@pytest.fixture()
def test_vote(test_posts, session, test_user):
    new_vote = models.Vote(post_id=test_posts[3].id, user_id=test_user['id'])
    session.add(new_vote)
    session.commit() # the session.commit changes in the db directly

"""Defining Votes test cases"""

# testing for logged in as user 1 voting on user 2 post
def test_vote_on_post(authorized_client, test_posts):
    res = authorized_client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 1})
    assert res.status_code == 201

# testing for when a user tries to like a post that they'v already liked
def test_vote_twice_post(authorized_client, test_posts, test_vote):
    res = authorized_client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 1})
    assert res.status_code == 409

# testing for successfully deleting a vote:
def test_delete_vote(authorized_client, test_posts, test_vote):
    res = authorized_client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 0})
    assert res.status_code == 201

# testing for deleting a vote that doesn't exist (i.e. vote never made)
def test_delete_vote_non_exist(authorized_client, test_posts):
    res = authorized_client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 0})
    assert res.status_code == 404

# testing for voting/liking on a post that doesn't exist 
def test_vote_post_non_exist(authorized_client, test_posts):
    res = authorized_client.post("/vote/", json={"post_id": 80000, "dir": 1})
    assert res.status_code == 404

# testing for a user who is unauthenticated can't vote
def test_vote_unauthorized_user(client, test_posts):
    res = client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 1})
    assert res.status_code == 401
