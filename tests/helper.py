from myflaskbase.blueprints.user.models import User

def create_user(db, username="test", password="password"):
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user