can_login = False
try:
    assert can_login
except AssertionError:
    print("User has no access to login")
"""
This runs fine with pipenv run python3 Assertions.py & prints the message
When run with pipenv run python -O Assertions.py, it does not print the message
"""
