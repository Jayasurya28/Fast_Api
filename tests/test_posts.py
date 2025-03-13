import pytest
from app import schemas

def test_get_all_posts(authorized_client,test_posts):
    res = authorized_client.get("/posts/")
    def validate(post):
        return schemas.PostOut(**post)
    post_map = map(validate,res.json())
    post_list = list(post_map)
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200

def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401


def test_unauthorized_user_get_one_posts(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_get_one_post_not_exist(authorized_client,test_posts):
    res = authorized_client.get(f"/posts/8888")
    assert res.status_code == 404

def test_get_one_post(authorized_client,test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.title == test_posts[0].title

@pytest.mark.parametrize("title, content, published", [
    ("awesome new title","awesome new content",True),
    ("Fav food","I like pizza",False),
    ("Fav city","Sathyamangalam",True),
])
def test_create_post(authorized_client, test_user, test_posts,title, content, published):
    res = authorized_client.post("/posts/", json={"title": title, "content": content, "published": published})

    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title  
    assert created_post.content == content  
    assert created_post.published == published
    assert created_post.owner_id == test_user["id"] 

def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post("/posts/", json={"title": "arbitrary title", "content": "budbuc"})

    # res = authorized_client.post("/posts/", json={"title": arbitrary title, "content": "budbuc"})

    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title ==  "arbitrary title"
    assert created_post.content == "budbuc" 
    assert created_post.published == True
    assert created_post.owner_id == test_user["id"] 


def test_unauthorized_user_create_posts(client,test_user, test_posts):
   res = client.post("/posts/", json={"title": "arbitrary title", "content": "budbuc"})
   assert res.status_code == 401