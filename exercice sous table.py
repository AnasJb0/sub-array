def soustableau(ind1,ind2,table) :
    T=[]
    for i in range(ind1,ind2) :
        T.append(table[i])
    return T

while True :
    table=[]
    for i in range(0,10) :
        element=int(input(f"Enter the item {i+1} : "))
        table.append(element)
    print(table)
    ind1=int(input("Enter the first clue: "))
    ind2=int(input("Enter the second clue: "))
    print(soustableau(ind1,ind2,table))
    x=input("want to enter a new list (Yes/No) : ")
    if x != "Yes" :
        break

    

