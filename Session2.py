class Animal:
    name = ""
    def __init__(self,n,c):
        self.name = n
        self.color = c
   
    def display(c):
        print(c.name)
        print(c.color)
class dog(Animal):
    
    def __init__(self,n,c,s):
        super().__init__(n,c)
        self.sound = s
        
    def sd(s):
        print(s.sound)

class cat(Animal):
    def __init__(self,n,c,s):
        super().__init__(n,c)
        self.sound = s  
    def sd(s):
        print(s.sound)