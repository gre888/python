class Animal:
    def fly(self):
        print("時速20公里")
class Bird(Animal):
    def fly(self):
        print("時速50公里")
class Plane:
  def fly(self):
    print("時速800公里")
  def fly_mile(self, speed):
    print(f"飛行{speed}英里")
    
animal=Animal()
animal.fly()
bird=Bird()
bird.fly()
plane=Plane()
plane.fly()
plane.fly_mile(5)    