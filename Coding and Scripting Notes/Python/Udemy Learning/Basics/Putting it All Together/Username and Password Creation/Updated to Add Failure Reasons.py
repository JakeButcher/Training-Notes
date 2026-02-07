
# Creating username:
user_name = ""
user_name = input("Please Create a Username: ")
# Creating password:
user_password = ""
user_password = input("Please Create a Password: ")
# Enforcing password rules:
lowercase, uppercase, special, digit = 0, 0, 0, 0
s = user_password
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="$@_"
digits="0123456789"
# Check password length:
if len(user_password) < 8:
    print("Invalid Password")
    print("Please include 8 or more characters")
# Check password rules:
else:
    for i in s:
        # counting lowercase characters
        if (i in smallalphabets):
            lowercase+=1  
        # counting uppercase characters
        if (i in capitalalphabets):
            uppercase+=1  
        # counting numbers
        if (i in digits):
            digit+=1     
        # counting the mentioned special characters
        if(i in specialchar):
            special+=1   
# Confirm Password
    if (lowercase>=1 and uppercase>=1 and special>=1 and digit>=1 and lowercase+uppercase+special+digit==len(s)):
        password_confirmation = ""
        password_confirmation = input("Please Confirm your Password: ")
        if password_confirmation == user_password:
            print("Password Created Successfully")
        else:
            print("Passwords Do Not Match")
# Password error messages
    else:
        for q in s: 
            print("Invalid Password")
            if (lowercase<1):
                print("Please include a lowercase character")
                break
            elif (uppercase<1):
                print("Please include an uppercase character")
                break
            elif (special<1):
                print("Please include a special character")
                break
            elif (digit<1):
                print("Please include a number")
                break
