# Problem: Write function that takes list value as an argument and
# returns a string with all items separated by a comma and a space
# with the word 'and' before the last item
# Ex. spam = ['apples', 'bananas', 'tofu', and 'cats'] should be
# returned as 'apples, bananas, tofu, and cats'


# define the function
def commaConvert(userEntry):
    converted = "" # establish a blank string variable

    for i in userEntry[:-1]: # for all items in the list (excluding last item)
        converted = converted + i + ", " # loop to add list value with comma space
    converted = converted + "and " + userEntry[-1] # add the 'and' and final list value
    print(converted) # print the result
    return converted # return the result

# define the input list and call the function
userEntry = ['apples', 'bananas', 'tofu', 'cats'] # list is defined here
commaConvert(userEntry) # call the function with the list argument
