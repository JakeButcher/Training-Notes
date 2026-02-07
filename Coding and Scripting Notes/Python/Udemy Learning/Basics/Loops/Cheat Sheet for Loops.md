In this section, you learned the following:


• A for-loop is useful to repeatedly execute a block of code.


• You can create a for-loop like so:

1. for letter in 'abc':
2.     print(letter.upper())
Output:
A
B
C
As you can see, the for-loop repeatedly converted all the items of 'abc' to uppercase.



• The name after for (e.g. letter) is just a variable name



• You can loop over dictionary keys as follows:

1. phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
2. for value in phone_numbers.keys():
3.     print(value)
Output:
John Smith
Marry Simpsons



• You can loop over dictionary values:

1. phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
2. for value in phone_numbers.values():
3.     print(value)
Output:
+37682929928
+423998200919




• You can loop over dictionary items:
    1. phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
    2. for key, value in phone_numbers.items():
    3.     print(key, value)
Output: 
    1. John Smith +37682929928
    2. Marry Simpons +423998200919
    • We also have while-loops. The code under a while-loop will run as long as the while-loop condition is true:
    1. while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    2.     print("It's not yet 19:30:20 of 2090.8.20")
The loop above will print out the string inside print() over and over again until the 20th of August, 2090.


