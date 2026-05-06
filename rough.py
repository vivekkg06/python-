# i=1
# while i<=10:
#     print(i,end=".")
#     print("hello")
#     i+=1

# i=1
# while i<=10:
#     print(f"{i}.hello")
#     i+=1

# i=1
# while i<=5:
#     print( " *"*i)
#     i+=1

# n=5
# i=1
# z=n
# while i<=n:
#     print("   "*i,end="")
#     print(" * "*z)
#     i=i+1
#     z=z-1

# n=8
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#      print(i,end="")
#      j+=1
#     print()

#     i+=1
    
# l="abcdehjkl"
# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#        print(l[i-1],end="")
#        j+=1
#     print()
#     i+=1
    
# n=10
# space=n
# for i in range(n):
#     print(" "*space,end="")
#     print(" *"*i)
#     space-=1
    
# n=10
# i=1
# num=1
# space=(n*2)+(n-3)

# while i<=n:
#     reverse =""
#     j=1
#     while j<=i:
#         if num<10:
#             print("0"+str(num),end=" ")
#             j+=1
#             reverse +=str(num)[::-1]+"0 "
#             num=num+1
#         else:
#             print(num,end=" ")
#             j+=1
#             reverse +=str(num)[::-1]+" "
#             num=num+1
#     x = 1
#     print("  "*space,reverse[::-1],end=" ")
#     space -=3
#     i+=1
#     print()
    
   
# def fun(a,b):
#     c=a*b
#     return(c)
# d=fun(2,5)
# print(d)
# e=fun(5,10)
# print(e)



# def pattern(x):
#     space=x
#     for i in range(x+1):
#         print("* "*i)
#         print(" "*space,end="")
#         space-=1

# pattern(5)
# pattern(8)


# def num(x,y,z):
#     a=[]

#     if y>1:

#         for i in range(x,y+1,z):
#             a.append(i)
#         return a
    
#     elif z>=1:
#         for i in range(x,y,z):
#             a.append(i)
#         return a
    

# print(num(1,10,2))


class Bike():
    def __init__(self,name,year,price):
        self.name=name
        self.year=year
        self.price=price

    def show(self):
        print(f"name:{self.name}")
        print(f"purchase year:{self.year}")
        print(f"price:{self.price}")
        print("_"*20)

bike1=Bike("ronin",2026,"2L")
bike1.show()
bike2=Bike("CB350",2024,"3L")
bike2.show()

bike1.year=2025
bike1.show()



class Cosmectics():
    def __init__(self,companyname,name,price,expdate):
        self.companyname=companyname
        self.name=name
        self.price=price
        self.expdate=expdate

    def show(self):
        print(f"companyname={self.companyname}")
        print(f"productname={self.name}")
        print(f"price={self.price}")
        print("expdate=",self.expdate)
        
        print("_"*50)

a=Cosmectics("plum","ricewater",399,"4/1/2026")
b=Cosmectics("revlon","serum",799,"5/12/2024")

a.show()
b.show()

