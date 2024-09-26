# database.py
# In memory database to store users and posts.

users = {}
posts = []

def add_user(username, password):
    if username in users:
        return False
    users[username] = password
    return True

def validate_user(username, password):
    return users.get(username) == password

def add_post(username, post_content):
    post = {"user": username, "content": post_content}
    posts.append(post)

def get_posts():
    return posts
