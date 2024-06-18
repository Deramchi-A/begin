'''
def even_char(num_char):#definetion of the func
    num_list=[]#an empty list
    n=0# the steps 
    for i in num_char:# the for loop to create 
                       #a list with seperate characters
        num_list.append(i)
    for i in num_list[n::n+2]:# print the even elementes in the list
        print(i)
    
    print(num_list)


even_char("hamidderamchi")
'''
word = input('Enter word: ')
print('Original String: ', word)
size = len(word)
print ('Printing only even index chars')
for i in range (0,size-1,2):
    print ("index[",i,"]",word[i])
