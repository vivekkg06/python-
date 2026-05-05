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

emp1=Emp(year=2000,name="rahul",salary=40000)
emp2= Emp("kiran",2002,20000)
emp1.show()

# emp1.salary = 30000
# emp1.show()

# emp2.name="rajan"
# emp2.show()

# emp2.byear=1998
emp2.show()





