list1=[1,2,3,4,1,2,3,5,4,5]

#print duplicates alone

duplicates=list(set([x for x in list1 if list1.count(x)>1]))

print("Duplicates in the list:",duplicates)