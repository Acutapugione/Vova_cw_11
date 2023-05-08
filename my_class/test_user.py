from user import User

def test_user_login():
    u = User(email='acuta.pugione@gmail.com', password=12345)
    assert u.login == 'acuta.pugione', u.login
    
def test_user_init():
    u = User(email='acuta.pugionegmail.com', password=12345)
    assert u.login == 'acuta.pugione', u.login
