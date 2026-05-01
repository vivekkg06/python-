# def demo():
#     print("hello world")
# demo()
# demo()

# def add(x,y=0):
#     print(x+y)
# add(10)
# add(20,50)

# def mul(a,b=0):
#     print(a*b)
# mul(2,5)
 
# def mul(x,y):
#     c=x*y
#     return(c)
# a=mul(10,5)
# print(a)


# def mul(x,y=0):
#     c=x*y
#     return(c)
# a=mul(10,5)
# print(a)
# b=mul(5)
# print(b)

# def message():
#     a="python is powerfull language"
#     return a

# print (message())

# b=message()
# print(b)


# def calculate(x,y,symbol):
#     match symbol:
#         case "+":
#             print("answer is :",x+y)
#         case "-":
#             print("answer is :",x-y)
#         case "*":
#             print("answer is :",x*y)


# calculate(symbol='*',x=30,y=10)


# def pattern(x):
#     space=x

#     for i in range(x+1):
#         print(" "*space,end="")
#         print("* "*i)
#         space-=1

# pattern(15)
# pattern(4)
# pattern(3)


# def add(* args):
#     print(args)
#     print(type(args))
# add(10)
# add(10,20)
# add(10,20,30,40,50)



# def add(*a):
#     x =0
#     for i in a:
#        x+=i
#     return x

# a=add(10,20,30,40,50)
# print(a)

# b=add(1,2,3,4,5,6)
# print(b)
# print(add(20,30))




# def number(x):
#     r=[]
#     for i in range(1,x+1):
#         r.append(i)
#     return r

# print(number(10))



# def number(x,y=None,z=0):
#     r=[]
#     if y==None:
#         for i in range(1,x+1):
#             r.append(i)
#         return(r)
#     elif z >=1 :
#         for i in range(x,y+1,z):
#             r.append(i)
#         return(r)
#     elif z<0:
#         for i in range(x,y-1,z):
#             r.append(i)
#         return(r)
#     else:
#         for i in range(x,y+1):
#             r.append(i)
#         return r
    
# a=number(30,20,-1)
# print(a)


# def fib(x):
    
#     a=1
#     b=1
#     c=a+b
#     for i in range(x):
#         print(a)
#         a=b
#         b=c
#         c=a+b
    

# fib(15)


      



    

