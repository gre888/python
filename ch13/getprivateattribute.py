class Father():
  def __init__(self,name):
    self.name=name
    self.__eye="黑色"
  def getEye(self):
    return self.__eye

class Child(Father):
  def __init__(self,name,eye):
    super().__init__(name)
    self.eye=eye
    self.fatherEye=super().getEye()
joe=Child("小華","棕色")
print(joe.name)
print(joe.eye)
print(joe.fatherEye) 
