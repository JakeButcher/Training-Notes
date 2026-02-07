
Here is an example that combines a dictionary loop with string formatting. The loop iterates over the dictionary and it generates and prints out a string in each iteration:


1. phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
2.  
3. for pair in phone_numbers.items():
4.     print(f"{pair[0]} has as phone number {pair[1]}")

And here is a better way to achieve the same results by iterating over keys and values:

1. phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
2.  
3. for key, value in phone_numbers.items():
4.     print(f"{key} has as phone number {value}")

In both cases, the output is:
John has as phone number +37682929928
Marry has as phone number +423998200919


