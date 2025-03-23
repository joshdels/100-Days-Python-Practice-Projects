class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")
        
class Fish(Animal):
    def __init__(self):
        # inheritance
        super().__init__()
        
    def breathe(self):
        # call superclass to inherit
        super().breathe()
        print("doing this underwater")
        
    def swim(self):
        print("moving in the water")
        
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

