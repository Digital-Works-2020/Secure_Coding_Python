class User:
    def __init__(Self, trust=False):
        Self.trust = trust

    @property        
    def can_login(Self):
        print("Checking Login Functionality")
        return Self.trust


def login(user):
    #If class method has @property decorator, it should be called without parentheses
    if user.can_login:
        print("User is trusted!!")
    else: 
        print("User seems to be Hacker :(")

hacker = User(trust=False)
friend = User(trust=True)

login(hacker)
login(friend)
