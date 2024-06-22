#my solution
'''
def palidorme_number():
    while True:
        num=input('Enter the number contain 3 digits you wish to be tested: ')
        length_num=len(num)
        print(type(length_num))
        print(length_num)
        if num[0]==num[length_num-1]:
            print('the number ',num,' is palindorme')
        else:
            print('the number ',num,' is not palindorme')
        if num=="1":
            break
            '''
#the best solution
def palindorme(number):
    print('original number',number)
    original_num= number
    #reverce the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10)+ reminder
        number = number // 10
    if original_num == reverse_num:
        print("Given number palindrome",original_num)
    else:
        print ('Given number is not palindrome',original_num)
palindorme(121)
palindorme(125)