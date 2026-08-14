class Animal():
    def __init__(self, name):
        self.name = name
    def fly(self):
        print(self.name+"會飛")
    
class Bird(Animal):
    def __init__(self, name):
        self.name = "粉紅色" + name
    def sing(self):
        print(self.name+"也愛唱歌")      
          
pigeon=Animal("鴿子")
pigeon.fly()
parrot=Bird("鸚鵡")
parrot.fly()
parrot.sing()
        