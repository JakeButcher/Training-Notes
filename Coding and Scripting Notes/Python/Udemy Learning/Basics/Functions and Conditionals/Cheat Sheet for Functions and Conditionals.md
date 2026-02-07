In this section, you learned to:

    • Define functions:

1. def cube_volume(a):
2.     return a * a * a



    • Write if-else conditionals:

1. message = "hello there"
2.  
3. if "hello" in message:
4.     print("hi")
5. else:
6.     print("I don't understand")




    • Write if-elif-else conditionals:

1. message = "hello there"
2.  
3. if "hello" in message:
4.     print("hi")
5. elif "hi" in message:
6.     print("hi")
7. elif "hey" in message:
8.     print("hi")
9. else:
10.     print("I don't understand")




    • Use the and operator to check if both conditions are True at the same time:

1. x = 1
2. y = 1
3.  
4. if x == 1 and y==1:
5.     print("Yes")
6. else:
7.     print("No")




    • Use the or operator to check if at least one condition is True:

1. x = 1
2. y = 2
3.  
4. if x == 1 or y==2:
5.     print("Yes")
6. else:
7.     print("No")




    • Check if a value is of a particular type with isinstance:

1. isinstance("abc", str)
2. isinstance([1, 2, 3], list)
or directly:

1. type("abc") == str
2. type([1, 2, 3]) == lst
