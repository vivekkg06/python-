# f = open('demo.txt','a')

# z = input("enter your text :")
# f.write(z+"\n")
# f.close()


# f= open("demo.txt","r")

# a = f.read()
# print(a)
# f.close()


# f= open("demo.txt","w")

# a = f.write()
# print(a)
# f.close()


# a=""
# with open('demo.txt','r')as file:
#     a = file.read()
#     print(a)
# with open('demo1.txt',"w")as f:
#     f.write(a)


# while True:
#     with open('demo.txt','r')as file:
#         a = file.read()
#         print(a)
#     with open('demo1.txt',"w")as f:
#         f.write(a)

    

# import csv

# a =[['name','age','mark'],['rahul',28,70],['arun',30,65]]
# with open("data.csv","w",newline='')as f:
#     w = csv.writer(f)
#     w.writerows(a)


# import csv
# with open('data.csv','r')as f:
#     r = csv.reader(f)
    
#     c =0
#     for i in r:
#         print(i)
#         c+=1
#         if c ==1:
#             continue
#         print("name:",i[0],"age:",i[1],"mark:",i[2])



       
import json

d ={
    'name':['rahul,manu'],
    'place':'thrissur',
}

f = open('data1.json','w')
w = json.dump(d,f,indent=4)
f.close()

# import json


# with open("data1.json","r") as file:
#     a = json.load(file)
#     print(a)
    