class Calculator():
    def add(self,*args):
        num=0
        for i in args:
            num+=i
        print(num)

    def sub(self,a=0,*args):
        num=a
        for i in args:
            num-=i
        print(num)


    def mul(self,*args):
        num=1
        for i in args:
            num*=i
        print(num)

    
class Area():
    def circlearea(self,radius=0):
        pi=3.14
        area=pi*(radius**2)
        print(area)

