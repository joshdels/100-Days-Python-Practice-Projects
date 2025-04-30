class User:
    def __init__(self, name):
        self.name = name 
        self.is_logged_in = False
    
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs): #may na add na args or kwargs
        if args[0].is_logged_in == True:
            function(args[0]) # tapos ang function na i pass added args and kwargs
    return wrapper    

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")
        
new_user = User("Angela")
new_user.is_logged_in = True
create_blog_post(new_user)