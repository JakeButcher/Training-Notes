# Below the code allows the user to input a Username and Password. 
#
# The Username can be anything the user inputs
#
# The Password must contain:
#	- 8+ Characters
#	- A Uppercase
#	- A Lowercase
#	- A Number
#	- A Special Character
#
# ** Notes. 
#	- This could also be improved by allowing the user to confirm password after successful creation.
#	- Could implement printing the specific password rule not followed after a password failure.
#		○ Can only give 1 error at a time even if multiple errors
#
#
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


# Creating username:
user_name = ""
user_name = input("Please input username: ")

# Creating password:
user_password = ""
user_password = input("Please create a password: ")

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
    print("Password Created Successfully")
else:
    print("Invalid Password")
