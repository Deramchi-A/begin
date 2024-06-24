#my solution
def power_func(base,exp):
    print ("base= ",base)
    print ("power= ",exp)
    resulte=base**exp
    print(base," raises to the power of ",exp," is= ",resulte)
    
power_func(2,5)
'''
#thier solution
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)
'''