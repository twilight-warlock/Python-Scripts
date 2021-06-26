import random
import string

choice = int(input("\n1. Random\n2. Work with\nEnter your choice from 1-2 : "))

password = ""
if(choice == 1):
    passlen = int(input("Enter length of password : "))
    for x in range(passlen):
        num = random.randint(1, 4)
        if(num == 1):
            password += random.choice(string.ascii_uppercase)
        elif(num == 2):
            password += random.choice(string.ascii_lowercase)
        elif(num == 3):
            password += random.choice(string.digits)
        elif(num == 4):
            password += random.choice(string.punctuation)
elif (choice == 2):
    password = input("Enter work with word : ")
    passlen = int(input("Enter total length of password required : "))
    num = random.randint(1, 4)
    if(len(password) >= 5):
        newpass = ""
        for i in password:
            if i.isalpha():
                num = random.randint(1, 2)
                if(num == 1):
                    newpass += i.upper()
                elif(num == 2):
                    newpass += i.lower()
            else:
                newpass += i
        password = newpass
    for x in range(passlen-len(password)):
        num = random.randint(1, 4)
        if(num == 1):
            password += random.choice(string.ascii_uppercase)
        elif(num == 2):
            password += random.choice(string.ascii_lowercase)
        elif(num == 3):
            password += random.choice(string.digits)
        elif(num == 4):
            password += random.choice(string.punctuation)
print(password)
