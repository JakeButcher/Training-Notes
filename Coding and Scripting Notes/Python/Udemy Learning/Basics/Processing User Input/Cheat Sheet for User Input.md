In this section, you learned that:
    • A Python program can get user input via the input function:
• The input function halts the execution of the program and gets text input from the user:

1. name = input("Enter your name: ")
    • The input function converts any input to a string, but you can convert it back to int or float:

1. experience_months = input("Enter your experience in months: ")
2. experience_years = int(experience_months) / 12
    • You can also format strings with:

1. name = "Sim"
2. experience_years = 1.5
3. print("Hi {}, you have {} years of experience".format(name, experience_years))
Output: Hi Sim, you have 1.5 years of experience.


