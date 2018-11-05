from sys import argv # added import of argv

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input() # added variable and input
print("How much do you weigh?", end=' ') # added closing bracket
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filename) # corrected spelling of 'filename'

print("Here's your file {filename}:")
print(txt.read()) # corrected spelling of 'txt'

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read()) # corrected parameter (or is it argument?)


print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.') # split into two lines for formatting

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") # correctly enclosed in quotes
print(poem)
print("--------------") # correctly enclosed in quotes


five = 10 - 2 + 3 - 6 # added '6' to correct the issue
print(f"This should be five: {five}") # added closing parentheses

def secret_formula(started): # added colon
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 # added '/' operator
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # added 'crates' argument

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # added underscore to start_point
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30 # corrected spelling of 'cats'
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!") # added parentheses

if people > cats: # corrected operator from less than to greater than
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # added colon
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: # added colon
    print("People are less than or equal to dogs.") # added final quote


if people == dogs: # changed from '=' to '==' for operator comparison operator
    print("People are dogs.")
