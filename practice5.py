import sys
list=["nishan",44,'abhi',98.8,'luffy',33,12.0,'bey']
list2=[]
list3=[]
list4=[]
for x in list:
    if type(x)==int:
        list2.append(x)
    elif type(x)==float:
        list3.append(x)
    elif type(x)==str:
        list4.append(x)
    else:
        sys.exit("unclassified")
print(list2)
print(list3)
print(list4)