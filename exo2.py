def PrintCurAndPrevNum(num):
    print("printing the current and the previous number sum in the range of n")
    for i in range (num):
        CurrNum=int(i)
        PrevNum=int(i-1)
        if PrevNum==-1:
            PrevNum=0
        print(f"the current {CurrNum} the previous {PrevNum} the sum {CurrNum+PrevNum}")
       

PrintCurAndPrevNum(10)
