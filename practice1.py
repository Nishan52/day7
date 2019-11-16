import sys
name=input("Please enter your name")
while name.isalpha()==False or len(name)<4 :
    if ' ' in name :
        break
    else:
        print("THE NAME YOU ENTERED IS INCORRECT")
    name=input('Enter name again')
print("WELCOME! BE READY FOR SECOND AUTHENTICATION")
phonenum=input("Please entrer your phone num")
while len(phonenum)!=10:
        print("THE PHONE NUMBER YOU ENTERED IS NOT CORRECT")
        phonenum=input("Please ENter your phone number")
print("FINALLY! YOUR ARE ONE STEP AWAY")
age=input("PLEASE ENTER YOUR AGE" )
while age.isdigit()==False or int(age)<18:
    print("SORRY THE AGE YOU ENTERED IS INCORRECT")
    age=input("ENTER YOUR AGE")
print("FINALLY YOU ARE HERE")