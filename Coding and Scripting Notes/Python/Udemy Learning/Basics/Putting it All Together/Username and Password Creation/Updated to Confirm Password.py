
# Creating username:
user_name = ""
user_name = input("Please Create a Username: ")
# Creating password:
user_password = ""
user_password = input("Please Create a Password: ")
# Enforcing number in password:
lowercase, uppercase, special, digit = 0, 0, 0, 0
s = user_password
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="$@_"
digits="0123456789"
if (len(s) >= 8):
    for i in s:
        # counting lowercase alphabets
        if (i in smallalphabets):
            lowercase+=1            
        # counting uppercase alphabets
        if (i in capitalalphabets):
            uppercase+=1            
        # counting digits
        if (i in digits):
            digit+=1            
        # counting the mentioned special characters
        if(i in specialchar):
            special+=1        
if (lowercase>=1 and uppercase>=1 and special>=1 and digit>=1 and lowercase+uppercase+special+digit==len(s)):
        password_confirmation = ""
        password_confirmation = input("Please Confirm your Password: ")
        if password_confirmation == user_password:
            print("Password Created Successfully")
        else:
            print("Passwords Do Not Match")
else:
    print("Invalid Password")
