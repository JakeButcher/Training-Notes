Firstly we want to import Active Directory Module:

![alt text](image-23.png)


Get-ADUser:

![alt text](image-24.png)


We can make users variables and then use variables:

![alt text](image-25.png)

![alt text](image-26.png)

![alt text](image-27.png)


Adding/Removing a User to a Group:

![alt text](image-28.png)


Adding a new user:

![alt text](image-29.png)

When creating a password we need to use a secure string
    -AccountPassword(ConvertTo-SecureString "Password") 

![alt text](image-30.png)
