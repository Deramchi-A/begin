#my solution
list_1=input('Enter you number: ')
print (list_1[4:0:-1])

print (list_1[0:4:1])
'''
#the solution 
number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")
    '''