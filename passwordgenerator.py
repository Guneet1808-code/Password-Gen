import string
import random
chars=""

len1=int(input("Enter the length of the password:"))
print('''Choose character set for password from these : 
         1. Letters
         2. Digits
         3. Special characters
         4. Exit''')
while True:
    x=int(input("Enter your option:"))
    if x==1:
        chars+=string.ascii_letters
    elif x==2:
        chars+=string.digits
    elif x==3:
        chars+=string.punctuation
    elif x==4:
        break
    else:
        print("Please pick a valid option!")
password=[]
for i in range(len1):
    randchar=random.choice(chars)
    password.append(randchar)
print("The random password is " + "".join(password))