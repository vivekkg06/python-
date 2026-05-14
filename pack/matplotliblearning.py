import matplotlib.pyplot as plt




  
year = []
profit=[]


x = True
while x:
    choice = input("enther your choice [add,display,exit,v]:")
    match choice:
        case "exit":
            x = False
        case "add":
            year.append(int(input("enter the year:")))
            profit.append(int(input("enter your profit:")))
        case "display":
            print("year",year)
            print("profit:",profit)
        case 'v':
            fig, ax = plt.subplots()  
            ax.plot(year,profit) 
            plt.show()
        case _:
            print("invalid input")