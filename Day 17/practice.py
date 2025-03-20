class User:
    #Use PascalCase
    #no camelCase and snake_case
        # constructor initialize
    def __init__(self, user_id, username):
        print("new user_being created....")
        # ATTRIBUTES
        self.id = user_id
        self.username = username
        self.followers = 0 # default value
        self.following = 0
        
    # METHOD
    def follow(self, user):
        user.followers += 1
        self.following += 1
    
#New Object
user_1 = User("001", "joshua")
# user_1.id = "001"
# user_1.username = "joshua"
print(user_1.username)

user_2 = User("002", "Madam")
# print(user_2.followers)

# method test
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)



