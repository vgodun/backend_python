def create_user(username, email, password, **kwargs):
    if len(username) <= 5:
        return "Username is too short"
    if '@' not in email:
        return "Email must be a valid email address"
    if len(password) <= 8:
        return "Password must be at least 8 characters long"


    user = {
        "username": username,
        "email": email,
        "password": password,
    }

    user.update(kwargs)

    return user


print(create_user("test_name", "test@example.com", "123456789",))