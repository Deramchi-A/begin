list_1=[10,15,20,25,30,35]
list_2=[40,45,50,55,60,65]
list_3=[]
for i in list_1:
    if i % 2 ==0 :
        list_3.append(i)
print(list_3)
for j in list_2:
    if j % 2 != 0:
        list_3.append(j)
print(list_3)