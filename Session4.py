from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.r = radius
    def area(self):
        return 3.142*self.r**2
class square(shape):
    def __init__(self,length):
        self.l = length
    def area(self):
        return self.l**2
    

c = circle(5)
print("Area of circle is : ",c.area())
s = square(5)
print("Area of circle is : ",s.area())