In this section, you learned that:
    • Functions can have more than one parameter:

1. def volume(a, b, c):
2.     return a * b * c




• Functions can have default parameters (e.g. coefficient):

1. def converter(feet, coefficient = 3.2808):
2.     meters = feet / coefficient
3.     return meters
4.  
5. print(converter(10))
Output: 3.0480370641306997
Arguments can be passed as non-keyword (positional) arguments (e.g. a) or keyword arguments (e.g. b=2 and c=10):

1. def volume(a, b, c):
2.     return a * b * c
3.  
4. print(volume(1, b=2, c=10))




• An *args parameter allows the  function to be called with an arbitrary number of non-keyword arguments:

1. def find_max(*args):
2.     return max(args)
3. print(find_max(3, 99, 1001, 2, 8))
Output: 1001
    • A **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:

1. def find_winner(**kwargs):
2.     return max(kwargs, key = kwargs.get)
3.  
4. print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
Output: Sim







    • Here's a summary of function elements:

