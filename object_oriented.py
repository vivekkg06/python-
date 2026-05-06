# class Car():
#     def add(self,name,year,price):
#         self.name=name
#         self.year=year
#         self.price=price

#     def show1(self):
#         print(f"name:{self.name}")
#         print("purchase year:",self.year)
#         print("price :",self.price)

                
# car1 = Car() 
# car1.add('bmw m5',2025,'50L')
# car2= Car()
# car2.add("alto",2020,"2L")


# car1.show1()
# car2.show1()


class Emp():
    def __init__(self,name,year,salary):
        self.name=name
        self.byear=year
        self.salary=salary

    def show(self):
        print(f"name:{self.name}")
        print(f"birth year:{self.byear}")
        print(f"salary:{self.salary}")
        print("_"*100)

# emp1=Emp(year=2000,name="rahul",salary=40000)
# emp2= Emp("kiran",2002,20000)
# emp1.show()

# # emp1.salary = 30000
# # emp1.show()

# # emp2.name="rajan"
# # emp2.show()

# # emp2.byear=1998
# emp2.show()



class Bank():
    def __init__(self,acno=0,name="",age=0,amount=0):
        self.__acno=acno
        self.name=name # public atribute
        self._age=age
        self.__balance=amount # private atribute

    def checkbalance(self):
        print(f"account number :{self.__acno}")
        print(f"name:{self.name}")
        print(f"balance:{self.__balance}")
        print("_"*50)

    def deposit(self,amount=0):
        self.__balance += amount

    def withdraw(self,amount):
        self.__balance -=amount

    def __profilechange(self,acno):
        self.__acno = acno


    def changeacno(self,n):
        self.__profilechange(n)



p1= Bank(1234556,"vivek",27,1000)

p1.checkbalance()

p1.deposit(2000)

p1.checkbalance()

p1.withdraw(1500)

p1.checkbalance()

p1.__balance=10000000

p1.checkbalance()

p1.deposit(1000)
p1.checkbalance()

class SBI(Bank):
    def namecorrect(self,name):
        self.name = name
    def profile(self):
        print(f"name:{self.name}")
        print(f"age :{self._age}")
        print("_"*50)
    def age_c(self,ag):
        self._age = ag
        


p23 = SBI(acno=1313131,name='rahul',age=30,amount=1000)



p23.checkbalance()
p23.namecorrect('rahul k')






p23.checkbalance()

p23.age_c(35)

p23._age=70

p23.changeacno(70)

p23.profile()


