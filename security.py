from user import User

users = [
   User(1, "pawpaw", "123"),
   User(2, "lolo", "123")
]
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user["password"] == password:
        return {"status": "ok"}

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)