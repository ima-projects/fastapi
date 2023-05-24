# using the create_access_token idea from outh2.py to create an test access token separate to the one in that file
# token using to login to access posts
import pytest
from app import schemas

"""Defining Post test cases"""

"""Tests for retrieving/getting post(s)"""

# Pydantic schema used with pytest to validate the posts schema that is returned from db (to give me a PostOut model from 'the contract' (schemas.py))
def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    
    def validate(post):
        return schemas.PostOut(**post)
    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    #assert posts_list[0].Post.id == test_posts[0].id


# making sure an unauthenticated user is not able to retrieve all the posts
def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401


# testing getting a post by an id when you're an unauthenticated user
def test_unauthorized_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}") #test_posts id is generated after being implemented in db but not specfied in list of dictionaries in the fixture
    assert res.status_code == 401


# trying to test to retrieve a post with an id that doesn't exist
def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/88888")
    assert res.status_code == 404

# trying to retrieve a valid test post. Unpacking to a Pydantic schema model
def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    #print(res.json())
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_posts[0].id # bc post variable return only one post here but the test_posts fixture/function returns 3 posts so index must be specifed
    assert post.Post.content == test_posts[0].content # must refer to PostOut pydantic model and then from there can obtain content property from Post model in schemas.py because PostOut class is a dependency of Post class
    assert post.Post.title == test_posts[0].title
    #assert res.status_code == 200



"""Tests for creating a post"""

@pytest.mark.parametrize("title, content, published",[
    ("awesome new title", "awesome new content", True),
    ("favorite pizza", "i love cheese", False),
    ("tallest skyscrapers", "awesome skyscraper", True)
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post(f"/posts/", json={
        "title": title, "content": content, "published": published})

    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user['id']


# testing when published in set to True by default
def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post(f"/posts/", json={
        "title": "arbitrary title", "content": "arbitrary content"})
    
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == "arbitrary title"
    assert created_post.content == "arbitrary content"
    assert created_post.published == True
    assert created_post.owner_id == test_user['id']


# testing for when a user is not logged in (unauthorised) and is trying to create a post
def test_unauthorized_user_create_post(client, test_user, test_posts):
    res = client.post(f"/posts/", json={
        "title": "arbitrary title", "content": "arbitrary content"})
    assert res.status_code == 401


"""Tests for deleting a post"""

# testing for when an unauthorised user is trying to delete a post
def test_unauthoized_user_delete_Post(client, test_user, test_posts):
    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

# testing a valid deletion (authorised)
def test_authorized_user_delete_post_success(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 204

# trying to delete a post that does not exist in the database
def test_delete_post_non_exist(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/80000000")
    assert res.status_code == 404

# test where a user tries to delete a post that is does not belong to them (owned by someone else)
def test_delete_other_user_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert res.status_code == 403


"""Tests for updating a post"""

# defining a dictionary with the values I want to update
def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[0].id
    }
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data) # data dictionary being sent out with the Post pydantic schema in the router in post.py...
    updated_post = schemas.Post(**res.json()) #...(cont.) so being validated on this end with the same schema when the res.json() data is sent back to be unpacked
    assert res.status_code == 200
    assert updated_post.title == data['title']
    assert updated_post.content == data['content']

# trying to update another user's post (that is not their's)
def test_update_other_user_post(authorized_client, test_user, test_user2, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[3].id
    }
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    assert res.status_code == 403

# unauthenticated user trying to update a post
def test_unauthoized_user_update_post(client, test_user, test_posts):
    res = client.put(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

# user trying to update a post that doesn't exist
def test_update_post_non_exist(authorized_client, test_user, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[3].id
    }
    res = authorized_client.put(f"/posts/80000000", json=data)
    assert res.status_code == 404
    # create a pydantic model for each entry within the response and then try to validate each one



