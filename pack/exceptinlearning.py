# a=0
# b=0

# try:
#     c=a/b
# except ValueError:
#     c="valueError"



# x = True
# while x:
#     try :
#         a= int(input("enter first number :"))
#         b = int(input("enter second number :"))
        
#         if a ==0:
#             a = 1
#             c = b / a
#         else:
#             c = a / b

        
        
#     except ZeroDivisionError:
        
#         if b == 0:
#             b = 1
#             c = a / b
#         x = False
#     except TypeError:
#         c=("string not allowed")
#     except ValueError:
#         c=("enter the number input")
#     except :
#         c=("any error")

#     else:
        
#         x = False

#     finally:
#         print(c)


class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age:"))
    if age < 100 and age > 0:
        print(age)

    else :
        raise AgeError("age not posible")
    
except AgeError:
    print("age error")
except :
    print("any error")

else:
    print("try block working")



