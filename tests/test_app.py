from tests.helper import create_user

def test_index_ok(client, db, app):
    resp = client.get("/login")
    assert resp.status_code == 200

def test_login_success(client, db, app):
    create_user(db, username="test001", password="test001password")

    resp = client.post(
        "/login",
        data={"username": "test001", "password": "test001password"},
        follow_redirects=True,
    )

    assert resp.status_code == 200
    assert b"Logged in" in resp.data

def test_login_failed(client, db, app):
    create_user(db, username="test002", password="test002password")

    resp = client.post(
        "/login",
        data={"username": "test002", "password": "invaid"},
        follow_redirects=True,
    )

    assert resp.status_code == 400
    assert b"error" in resp.data

def test_register_success(client, db, app):
    new_username = "test003"
    new_password = "test003password"
    resp = client.post(
        "/register",
        data={"username": new_username, "password": new_password},
        follow_redirects=True,
    )

    # Check registration response
    assert resp.status_code == 201
    assert b"Registered" in resp.data
    assert new_username.encode("utf-8") in resp.data

    # Now try to login with the new user
    resp = client.post(
        "/login",
        data={"username": new_username, "password": new_password},
        follow_redirects=True,
    )

    assert resp.status_code == 200
    assert b"Logged in" in resp.data