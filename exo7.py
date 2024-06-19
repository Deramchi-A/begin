#my solution
str_x='hamid is a programer. hamid can write a program'
list_x=[]
str_y=str_x.split()
print(str_y)
counter=0
for i in str_y:
    if i=="hamid":
        counter=counter+1
print ('the string contain', counter , "repetition of hamid")
'''
the best solution
str_x='hamid is a programer. hamid can write a program'
#use the count method of a str class
str_x.count('hamid') 
'''