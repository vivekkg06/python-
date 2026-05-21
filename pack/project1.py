import pandas as pd
import json
import matplotlib.pyplot as plt


with open("prdatastore.json", 'r') as f:
    data = json.load(f)

x=True
while x :
    choice=input("enter your choice[add,display,exit,v]:")
    match choice:
        case "exit":
            x=False
        case "add":
            data["year"].append(int(input("enter year:")))
            data["profit"].append(int(input("enter profit:")))
            with open("prdatastore.json", 'w') as f:
                json.dump(data,f,indent=4)
        case "display":
            a=pd.DataFrame(data)
            with open("prdisply.txt","w") as f:
                f.write(str(a))
                print(a)
        case "v":
            f ,ax =plt.subplots()
            ax.plot(data["year"],data["profit"])
            ax.set_xlabel('year')
            ax.set_ylabel('profit')
            ax.set_xticks(data["year"])
            plt.show()
        case _:
            print("invalid input")  
            


