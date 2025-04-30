# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You call {function.__name__}{args}") # do something
        result = function(*args) # function
        print(f"It returned: {result}") # do something
        return result
    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)