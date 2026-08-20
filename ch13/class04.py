class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __sing(self):
        print(self.__name+str(self.__age)+"歲 很會唱歌",end=" ")
    def talk(self):
        self.__sing()
        print("也會模仿人類說話")

if __name__=="__main__":
    bird1 = Animal("灰鸚鵡",2)
    bird1.talk()
    bird1.__age=-1
    bird1.talk()
  #  bird1.__sing()