#Alex and Chloe
 

#Function
def list():
    print("Please choose an option. Type in a number between 1-8")
    print("1. Add a task \n 2. View current list \n 3. Mark task completed \n 4. Remove a task \n 5. Clear the List \n 6. Sort alphabetically \n 7. Print number of items \n 8. Exit the program")

    todo=["bread", "carrot","milk"]
    option=int(input("Option:  "))

    if option ==1:
        item=input("what item do you want to add?")
        todo.append(item)
        print (todo)
        list()
    elif option == 2:
        print (todo)
        list()
    elif option ==3:
        complete=input("what item is complete?")
        x=todo.index(complete)
        todo[x]=complete+" X"
        print(todo)
        list()
    elif option ==4:
        remove=input("What item do you want to remove?")
        todo.remove(remove)
        print(todo)
        list()
    elif option == 5:
        print(todo.clear())
        list()
    elif option == 6:
        x = sorted(todo)
        print(x)
        list()
    elif option ==7:
        y = len(todo)
        print(y)
    elif option==8:
        ans=input("Would you like to adjust the list?")
        if ans=="yes":
            list()
        elif ans=="no":
            quit()
    
#main
list()