class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} is created.")
    def sing(self):
        print(self.name+str(self.age)+"歲 很會唱歌")
        
    def grow(self,years):
        self.age += years
        print(f"{self.name} is now {self.age} years old.")
         

        
bird=Animal("鸚鵡", 1)
print(bird.name)
bird.grow(1)
bird.sing()
