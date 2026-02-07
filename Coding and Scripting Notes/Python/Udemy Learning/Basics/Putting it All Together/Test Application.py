## Creating an app that:
##	- Prompts and takes multiple user inputs (string)
##	- Capitalizes and adds suffix to the inputs
##	- Outputs the user inputs with the amendments once the user types "end"
##



# 1. Defining Sentence Maker (capitalizing and adding suffix) 
def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interrogatives = ("how", "what", "why", "who", "where", "when")
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


# 2. Adding User Input (for loop) 
results = []
while True:
    user_input = input("Say something: ")
    if user_input == "end":
        break
    else:
        results.append(sentence_maker(user_input))


# 3. Merging Strings to Output only String and Not a List
print(" ".join(results))




## Notable bugs:
##	- If user capitalizes an interrogative, a "?" will not be applied