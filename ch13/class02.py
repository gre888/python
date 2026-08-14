class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is created.")
    def sing(self):
        print(self.name,"can sing.")    
        
    def __del__(self):
        print(f"{self.name} is deleted.")    
        
bird=Animal("鸚鵡")
print(bird.name)
bird.sing()
del bird        