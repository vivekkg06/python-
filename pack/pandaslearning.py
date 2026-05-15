# import pandas as pd

# data = {
#     'A': [1, 2, 3,''],
#     'B':['apple','banana','mango',''],
#     'name':['rahul','vivek','rayees','arun']
#         }
# a = pd.DataFrame(data)
# print(a)
# print(type(a))



# name class mark
import pandas as pd


data={"name":[],'class1':[],'sub1':[],"sub2":[],'total':[],'avg':[]}

x = True
while x:
    choice = input("enter your choice [add,display,exit]:")
    match choice:
        case "exit":
            x = False
        case "add":
            data['name'].append(input("enter the name :"))
            data['class1'].append(input("enter your class :"))
            sub1 =int(input("enter your sub1mark :"))
            data['sub1'].append(sub1)
            sub2=(int(input("enter your sub2mark :")))
            data['sub2'].append(sub2)
            data['total'].append(sub1+sub2)
            data['avg'].append((sub1+sub2)/2)
        case "display":
            print(data)
            a = pd.DataFrame(data)
            print(a)
