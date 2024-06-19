#my solution
list_len=int(input("Enter the length of the list: "))
num_x=[]
for i in range(list_len):
    x=input('Enter the element of the list: ')
    num_x.append(int(x))

if num_x[0]==num_x[list_len-1]:
    print(True)
    print(num_x)
else:
    print(False)
    print(num_x)

