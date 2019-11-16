import sys
list=["nishan",44,'abhi',98.8,'luffy',33,12.0,'bey']
#list=['aa','bb','cc','dd','ee']
num=input("please enter a number you want to delete")
for i in list:
    if (i==num):
        print("matched")
        '''list.remove(i)
        print("The resulted list is",list)
        sys.exit("the resulted list is obtained")
    else:
        num=input("Sorry not in a list\n Enter value if you want to continue to remove element")
        '''