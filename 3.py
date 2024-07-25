list1=[1,2,5,6,8,10,12]
list2=[]

for x in range(1,16):
    if x not in list1:
        list2.append(x)
print(list2)