'''Assignment of Class -03
1. Create CRUD (Create, Read, Update, Delete) Operation.'''
createList = ['10', '9', 'rakib', 'uddin']

while True:
    create_list = input("What do you want? Enter Choice : create / read  / update / delete / quit: ")
    if create_list == "quit":
        print("You exist from program")
        break


#create list
    elif create_list == 'create':
        createList.append(input("Please create element to your list : "))
        print("This is your added list",createList)

 # read your list
    elif create_list == 'read':
     print("Congratulations! This is your list: ", createList)


#  delete element from your list
    elif create_list == 'delete':
        dl = input("Enter deleted item: ",)
        if dl in createList:
            createList.remove(dl)
        else:
            print("Not matched item")
        print("This is your deleted list",createList)

# update element from your list
    elif create_list == 'update':
        up_wrong = input("Enter  wrong item: ", )
        up_right = input("Enter right item: ", )
        if up_wrong in createList:
            wr = createList.index(up_wrong)
            createList[wr] = up_right
        else:
            print("Not matched item")
        print("This is your updated list", createList)

#for right command
    else:
        print("Please enter right command.")




