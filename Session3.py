class person:

    def __init__(self,n,a):
        self.__name = n
        self.__age = a
   
    def _display(c):
        print(c.__name)
        print(c.__age)
        
class student(person):
    def __init__(s,n,a,i):
        super().__init__(n,a)
        s._id = i
    def _std_info(s):
        s._display()
        print(s._id)
                        

abdullah = student("Abdullah",55,1307464)
abdullah._std_info()
