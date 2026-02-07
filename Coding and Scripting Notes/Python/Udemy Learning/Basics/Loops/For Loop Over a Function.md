A for loop can also be used to execute a function multiple times. For example, below we are executing celsius_to_kelvin three times since there are three items in the iterating list:


1. def celsius_to_kelvin(cels):
2.     return cels + 273.15
3.  
4. for temperature in [9.1, 8.8, -270.15]:
5.     print(celsius_to_kelvin(temperature))

The output of that would be:
282.25
281.95
3.0
So, in the first iteration celsius_to_kelvin(9.1) was executed, in the second celsius_to_kelvin(8.8) and in the third celsius_to_kelvin(-270.15).

