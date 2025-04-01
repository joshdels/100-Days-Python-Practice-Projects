#args and kwargs

def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(5,4,3,2,1))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    
    # print(kwargs["add"])
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add=3, multiply=5)

# more kwargs example to a Class
class Car:
    
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model") #.get gives value none instead of error when missing values
        
        
my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model) # goes none eventhough missing values