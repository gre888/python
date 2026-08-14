
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
#dog cat 去繼承Animal 然後實作  介面規格繼承實做 才能用      
class Dog(Animal):
    def sound(self):
        return "Woof!"
class Cat(Animal):
    def sound(self):
        return "Meow!"            



d=Dog()
print(d.sound())      