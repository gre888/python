class Animal():
    def __init__(self, name):
        self.name = name
    def fly(self):
        print(self.name+"會飛")
    
class Bird(Animal):
    def __init__(self, name,age):
      super().__init__(name)
      self.age=age
    def fly(self):
        print(str(self.age)+"歲的",end="")
        super().fly()
        
        
if __name__ == "__main__":
    pigeon = Animal("鴿子")
    pigeon.fly()
    parrot = Bird("小鸚鵡", 2)
    parrot.fly()