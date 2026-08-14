class Father:
  def drive(self):
    print("爸爸會開車")
class Mother:
  def cook(self):
    print("媽媽會做飯")
class Child(Father, Mother):
  def play(self):
    print("孩子會玩")
    
child = Child()
child.play()
child.drive()
child.cook()