#my solution
for i in range(1,11):
    print("The multiplication table of ",i," is: ",end=" ")
    #print(i,end=": ")
    for j in range(1,11):
        print (j*i,end=" ")
    print("\n")
'''
#Their solution
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")
'''