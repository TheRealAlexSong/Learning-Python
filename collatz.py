# Collatz Sequence from Automate the Boring Stuff chapter 3

# define the collatz function
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return (number // 2)
    elif number % 2 == 1:
        print(3 * number + 1)
        return (3 * number + 1)

# prompt user to input number
print('Type a number:')

# take input, convert to int, store in var 'n', with error handling
try:
    n = int(input())
# create loop to perform collatz until the result is 1
    while n != 1:
        n = collatz(int(n))
except ValueError:
    print('Value must an integer')
