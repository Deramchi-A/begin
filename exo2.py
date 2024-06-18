#MySolution
def PrintCurAndPrevNum(num):
    print("printing the current and the previous number sum in the range of n")
    for i in range (num):
        CurrNum=int(i)
        PrevNum=int(i-1)
        if PrevNum==-1:
            PrevNum=0
        print(f"the current {CurrNum} the previous {PrevNum} the sum {CurrNum+PrevNum}")
       

PrintCurAndPrevNum(10)
'''
the best solution

print ('printing current and previous number and their sum in a range of (10)')
previous_num= 0
for i in range (1,11):
    x_sum = previous_num + i
    ptint("current Number",i,"previous Number ",previous_num,"sum: ", x_sum)
    previous_num = i
'''
