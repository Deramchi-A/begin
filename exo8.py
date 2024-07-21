#My solution
list_num=[1,2,3,4,5,6]
for i in list_num:
    x=str(i)+' '
    print(x*int(i))


#the best solution
for num in range (6):
    for i in range(num):
        print(num,end=" ")
    print()
