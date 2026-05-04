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


# recursive function:-  
# factorial:-

# def fact(x):
#     if x==1:
#         return 1
#     else:
#         return x*fact(x-1)
# a=fact(5)
# print(a)
 
# def num(x,y=1):
#     print(y)
   
#     if x==1:
#         return 1

#     else:
#         return num(x-1,y+1)
# num(5)


# lambda function:-

# without argument and without return
# demo= lambda:print("hello world")
# demo()
# demo()

# with argument and without return
# add= lambda x,y=0 :print(x+y)
# add(10,20)
# add(20,50)
# add(50)


# square= lambda x :print(x**2)
# square(5)

# num=[1,2,3,4,5,6,7]
# sqrnum =[]
# for i in num:
#     sqrnum.append (i**2)

# print(sqrnum)

# num=[1,2,3,4,5,6,7,8,9,10]
# even= list(filter(lambda x:x%2==0,num))
# print(even)

# num=[1,2,3,4,5,6,7,8,9,10]
# odd= list(filter(lambda x:x%2==1,num))
# print(odd)


# reduce:-

# from functools import reduce
# a=[1,2,3,4,5,6,7]
# sum=reduce((lambda x,y:x+y),a)
# print(sum)


def adddata(name,age,subject1,subject2,subject3):
    data ={
        'name':name,
        'age':age,
        'subject1':subject1,
        'subject2':subject2,
        'subject3':subject3

    }
    return data
x=True
z =[]
while x:
    choice = input("enter your choice add/display/exit:")

    match choice:
        case 'exit':
            x= False
        case 'add':
            name = input("enter you name :")
            age= input("enter your age :")
            subject1=int(input("enter subject1 :"))
            subject2=int(input("enter subject2 :"))
            subject3=int(input('enter subject3 :'))
            z.append(adddata(name,age,subject1,subject2,subject3))

        case 'display':
            print(z)
            for x in z:
                print('name:',x["name"])
                print('age:',x["age"])
                print('subject1:',x["subject1"])
                print('subject2:',x["subject2"])
                print('subject3:',x["subject3"])
            
                total=(x["subject1"]+x["subject2"]+x["subject3"])
                avg = total//3
                print("total:",total)
                print("avg:",avg)
                print("------------------")
        case _:
            print("invalid input")



            
