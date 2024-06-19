#My solution
list_len=int(input("Enter the length of the list: "))
num_x=[]
for i in range(list_len):
    x=int(input('Enter the element of the list: '))
    num_x.append(x)
    if x%5==0:
        print('the number', x ,'is divisible by 5')
    else:
        print('the number', x ,'is not divisible by 5')

print ('the list is = ',num_x)