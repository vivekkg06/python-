# num1=12
# print(type(num1))

# a=10.20
# print(type(a))

# a="kiran"
# print(type(a))

# a=input("enter your name: ")
# print(type(a))

# a=input("enter your age: ")
# print(type(a))


# a=int(input("enter your first number: "))

# b=int(input("enter your second number: "))

# c=a+b
# print(c)


# boolean datatype:
# a=True
# print(type(a))
# b=False
# print(b)

# complex datatype:-

# a=4j
# b=3
# print(a*b)
# print(type(a))


# list:-

a=["apple","banana","grapes","orange"]
# print(a)
# print(type(a))
# print(a[1])
# print(len(a))
# a.append("cherry")
# print(a)
# a.insert(1,"cherry")
# print(a)
# a[1]="pineapple"
# print(a)
# a.pop(0)
# print(a)
# a.remove("grapes")
# print(a)
# a.reverse()
# print(a)
# print(a[1:3])

# for i in a:
#     print(i)

# b=[]
# for i in range(5):
#         b.append(input("enter the fruits name:"))
# print(b)

# a=[1,"hello",3.01,True,"orange"]
# print(a)
# print(a.index(3.01))
# a=[51,20,40,50]
# b=["apple","grapes","banana"]


# c=[a,"hello","python",b]
# print(c[3][1])

# a=[[],[]]
# for i in range(5):
#     a[0].append(input("name:"))
#     a[1].append(input("mark:")) 
# for i in range(5):
#     print("name:",a[0][i])
#     print("mark:",a[1][i])
#     print("--------------------------")

# op:-
# ame: hjh
# mark: 54
# --------------------------
# name: jhy
# mark: 87
# --------------------------
# name: ses
# mark: 45
# --------------------------
# name: cvv
# mark: 98
# --------------------------
# name: tru
# mark: 12
# --------------------------

# tuple:-

# a=1,2,3,"apple","banana"
# print(type(a))
# print(a[2])
# print(a)
# a=list(a)
# a[3]="orange"
# a=tuple(a)
# print(a)

# a=1,2,3,"apple","banana"
# b=24,45,65
# c=a+b
# print(c)

# a=(1,2,3,("apple","banana"))
# print(a[3][1])

# set:-

# a={1,2,3,3,"apple","banana",10,"orange"}
# print(a)

# b={8,2,4,3,1,6,5}
# print(b)

# a={"apple","banana",10,"orange"}
# for i in a:
#     print(i)
# a.add("grapes")
# a.remove("apple")
# a.pop()

# print(a)
# a.update({"grapes","cherry"})
# print(a)

# a={"apple","banana","orange","grapes"}
# b={"cherry","mango","apple","watermelon"}
# c=a.union(b)
# print(c)

# a="helloworld"
# a=list(a)
# a=set(a)
# b=""
# for i in a:
#     b+=i
# print(b)

# a={"apple","banana","mango","orange","grapes"}
# b={"cherry","mango","apple","watermelon"}


# c=a.intersection(b)
# print(c)

# c = a.difference(b)
# print(c)

# c = a.symmetric_difference(b)
# print(c)

# dictionary:-
# a={"name":"kiran","place":"thrissur"}


# print(a['name'])
# print(type(a))



# a['name']='vishnu'
# print(a)

# a=[{"name":"kiran","place":"thrissur"},{"name":"raju","place":"kozikode"}]
# print(a[1])

# a=[]
# for i in range(2):
#     b = {'name':'','age':'','place':''}
#     b['name']=input("name:")
#     b['age']=input ("age:")
#     b['place']=input("place:")
#     a.append(b)
#     print(b)
# for i in a:
#     print(i['name'],)
#     print(i['age'])
#     print(i['place'])
#     print("-------------------------------------")


# a = {'name':['naveen','kiran','vishnu'],'place':['thrissur','plakkad','kannur']}
# print(a['name'][0])

# a={"name":"rahul","age":24}
# a["place"]="thissur"
# a['age']=40
# print(a)

