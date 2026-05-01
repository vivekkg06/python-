# a=4/2
# print(a)

# b=10*2
# print(b)

# c=10**2
# print(c)

# d=10//3
# print(d)  

# e=10%3
# print(e)

# a=input("enter your name: ")
# b=int(input("enter your birthyear: "))
# age = 2026-b
# print("name:",a)
# print("age:",age)

# a="hello"
# print(len(a))
# print(a[1])
# print(a[-4])

# a="hello"
# print(a[0:3])
# print(a[::-1])
# print(a[-1:0:-1])
# print(a[-1:2:-1])

# a="hello"
# print(a.upper())

# b="ABCD"
# print(b.lower())

# a="hello world"
# print(a.capitalize())

# print(a.title())

# # Area of a rectangle?
# a=int(input("length: "))
# b=int(input("width: "))
# area=a*b
# print(area)

# # Area of a circle?
# a=int(input("radius: "))
# pi=3.14
# area=pi*a**2
# print(area)

# # perimeter of a rectangle?
# a=int(input("length: "))
# b=int(input("width: "))
# perimeter=2*(a+b)
# print(perimeter)


# a="hello world"
# b=a[::-1]
# print(b)

# a="hello"
# b="world"
# c=a+"_"+b
# print(c)

# a="apple"
# b=(a+",\n")*10
# print(b)



# print("  *  ")
# print(" * * ")
# print("* * *")


# print("  *  ""\n"" * *""\n""* * *""\n")


# comparison operators:
# a="Hello"
# b="hello"
# c=a==b
# print(c)

# a="10"
# b=10
# c=a==b
# print(c)

# a=10
# b=20
# c=a!=b
# print(c)

# a=10
# b=20
# c=a<b
# print(c)

# a=10
# b=20
# c=a>b
# print(c)

# a=10
# b=10
# c=a<=b
# print(c)

# a=10
# b=20
# c=a>=b
# print(c)
 
# a=int(input("age "))
# print(a>=18)


# logical operators:
# a=10>5 and 20>30
# print(a)
 
# a=10>5 or 10>20
# print(a) 

# a=10>20
# b=not a
# print(b)

# a=int(input("enter your age:"))
# print(a>=18 and a<=30)


# membership operator:
# a="python is a programming language"
# b="is" in a
# print(b)

# a="python is a programming language"
# b="z" not in a
# print(b)
 
# a=input("enter your id: ")
# b="1001,1002,1003,1004,1005"
# c=a in b
# print(c)

# a=int(input("enter age :"))
# b= a <= 18 or (30 <= a  and 40>=a  )
# print(b)

# # identity oprator:
# a=["apple","banana","grape"]
# b=["apple","banana","grape"]
# c=b
# z=b is c
# print(z)

# a=["apple","banana","grape"]
# b=["apple","banana","grape"]
# c=b
# z=b is not c
# print(z)

# assignment operator:
# a=10
# a=20
# print(a)

# a=10
# a+=20
# print(a)

# a=50
# a-=10
# print(a)

# a=2
# a*=10
# a*=2
# print(a)

# a=10
# a/=2
# print(a)

# a=10
# a//=2
# a//=2
# print(a)

# a=10
# a**=2
# print(a)

# if statement
# age=30
# if age>18 :
#     print("you are eligible for voting")

# age=15
# if age>18 :
#     print("you are eligible for voting")
# else :
#     print("you are not eligible for voting")        

# if elif statement:-
# mark=int(input("enter your mark"))
# if mark>90 :
#     print("grade A")
# elif mark>80 :
#     print("grade B")
# elif mark>70 :
#     print("grade C")
# elif mark>60 :
#     print("grade D")
# else:
#     print("failed") 

# match statement
# grade="B"
# match grade:
#     case "A"|"a" :
#         print("your mark is 90 to 100")
#     case "B"|"b" :
#         print("your mark is 80 to 90")
#     case "C"|"c" :
#         print("your mark is 70 to 80")
        
# grade="D"
# match grade:
#     case "A"|"a" :
#         print("your mark is 90 to 100")
#     case "B"|"b" :
#         print("your mark is 80 to 90")
#     case "C"|"c" :
#         print("your mark is 70 to 80")        
#     case _:
#         print("this case is not valid")



# week=input("enter week :")
# match week:
#     case "mon"|"tue"|"wed"|"thur"|"fri" :
#         print("working day")
#     case "sat"|"sun":
#         print("holiday")
#     case _:
#         print ("invalid input")

# looping statement

# a=100
# i=1
# while i<=a:
#     print(i,"hello world")
#     i+=1

# i=1
# while i<=10:
#     print(i)
#     print("wwww")
#     i=i+1
# print("gggggggggggg")

# i=1
# while i<=10:
#     print(i,end=".")
#     print("hello")
#     i+=1

# i=1
# while i<=10:
#     print(f"{i}.python")
#     i=i+1

# n=1
# while n<=5:
#     print("*"*n)
#     n=n+1

# n=1
# s=5
# while n<=5:
#     print("  "*s,end="")
#     print("* "*n)
#     n=n+1
#     s=s-1

# n=5
# i=1
# z=n
# while i<=n:
#     print("   "*i,end="")
#     print(" * "*z)
#     i=i+1
#     z=z-1

# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j+=1
#     print()
#     i=i+1



# l="abcdefghijkl"
# n=7
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(l[i-1],end=" ")
#         j+=1
#     print()
#     i=i+1

# n=8
# i=1
# num=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(num,end=" ")
#         j=j+1
#         num =num+1
#     print()
#     i=i+1
# output:-
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35 36


# n=5
# i=1
# space = n
# while i<=n:
#     if i==1 or i==n:
#         print((" "*space)+"* "*i,)
#     else:
#         print((" "*space)+'* '+('  '*(i-2))+'*')
#     i=i+1
#     space-=1



# n=5
# i=1
# space = n
# z=n
# while i<=n:
#     if i==1 :
#         print((" "*space)+". "*i,)
#     else:
#         print((" "*space)+'. '+('  '*(i-2))+'.')

#     i=i+1
#     space-=1
# i = 1
# z=n
# space=1
# while i<=n:
#     if i==n :
#         print((" "*space)+". "*z,)
#     else:
#         print((" "*space)+'. '+('  '*(z-2))+'.')
#     i +=1
#     space+=1
#     z=z-1
    

#   9
#  898
# 78987

# limit = 5
# x =1 
# space = limit
# num = limit
# while x<=limit:
    
#     y = 1
#     print("  "*space,end="")
#     while y<= x:
#         print(num,end=" ")
#         y+=1
#         num = num+1
#     z= 1
#     num -=1
#     while z<x:
#         num -=1
#         print(num,end=" ")
#         z=z+1
#     x+=1
#     space = space-1
#     num =num-1
#     print("")

# output
#           5 
#         4 5 4
#       3 4 5 4 3
#     2 3 4 5 4 3 2
#   1 2 3 4 5 4 3 2 1


# for loop:-

# a = "12345678910"
# for b in a: 
#     print(b)


# for i in range(10):
#     print(i)


# for i in range(100):
#     print(i,)


# for i in range(10,21):
#     print(i)

# for i in range(20,10,-1):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(2,10,2):
#     print(i)

# n=5
# for i in range(n):
#     print(" *"*i)

# n=5
# space=n
# for i in range(n):
#     print("  "*space, end="")
   
#     print(" *"*i)
#     space-=1
    
# n=10
# space=n
# for i in range(n):
#     print(" "*space,end="")
#     print(" *"*i)
#     space-=1

#  fibonacci series

# limit=5
# a=1
# b=1
# c=a+b

# for i in range(limit):
#     print(a)
#     a=b
#     b=c
#     c=a+b
    
# 1
# 1
# 2
# 3
# 5

#  armstrong number
# num = 153

# length = len(str(num))
# acnum = num
# result = 0
# for i in range(length):
#     m = acnum%10
#     acnum = acnum//10
#     result = result + m**length

# print(result)
# if result==num:
#     print("armstrong number")
# else:
#     print("sorry")

# prime number
# num = 17
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count = count+1
# print(count)

# if count==2:
#     print("prime number")
# else:
#     print("it's not a prime number")






# for num in range(100,10001):
#     length = len(str(num))
#     number = num
#     result = 0
#     for i in range(length):
#         d = number%10
#         number = number//10
#         result =result + d**length
#     if result==num :
#         print(result)


# for num in range(1,100):
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count = count+1
#     if count == 2:
#         print(num)


# limit=1000
# a=1
# b=1
# c=a+b

# while a <= limit:
#         print(a)
#         a=b
#         b=c
#         c=a+b


# for i in range(10):
#     if i==5:
#         break
#     print(i)

# for i in range(10):
#     if i==5:
#         continue
#     print(i)

# for i in range(10):
#     pass

# limit=100
# a=1
# b=1
# c=a+b
# for i in range(limit): 
          
#         print(a)
#         a=b
#         b=c
#         c=a+b
       
#         if a >=limit:
#                 break
        
        
# 1     1
# 23   23
# 4567654

# n=7
# for i in range (n):
#     print(7[i])


n=4
i=1
num=1
k=n
while i<=n:
    j=1
    while j<=i:
        print(num,end=" ")
        j+=1
        num=num+1
        # while i<=k:
        #     print("  "*n,end="")
        #     print(n)
        #     k-=1
    
        
    print()
    i+=1