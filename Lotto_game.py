import random


# User drawing numbers
def get_numbers():

    user_numbers = []
    move = 0

    while len(user_numbers) < 6:
        try:
            number = int(input("Give your number: "))
            if number in range(1, 50) and number not in user_numbers:
                user_numbers.append(number)
                move += 1
            elif number in user_numbers:
                print("Number cannot repeat. Please put another number.")
            elif number not in range(1, 50):
                print("Number must be in range 1 -49. Please put another number.")
        except ValueError:
            print('Only digits allowed. Please enter valid number.')
    user_numbers.sort()
    return user_numbers


# Computer drawing numbers
def generate_numbers():
    computer_numbers = set()  # set to avoid doubled
    while len(computer_numbers) < 6:
        number = random.randint(1, 50)
        computer_numbers.add(number)
    return sorted(list(computer_numbers))


def find_common_numbers(user_numbers, computer_numbers):
    common_numbers = set(user_numbers) & set(computer_numbers)
    return common_numbers


def lotto():
    user_numbers = get_numbers()
    print(f'Your numbers: {user_numbers}')

    computer_numbers = generate_numbers()
    print(f'Computer drawn numbers: {computer_numbers}')

    return user_numbers, computer_numbers


# Function returning both lists
user_numbers, computer_numbers = lotto()    # unpacking - 2 values returned assigned to 2 variables
matching_numbers = len(find_common_numbers(user_numbers, computer_numbers))

print(f'You guessed: {matching_numbers} numbers')

if matching_numbers >= 3:
    print('Congratulations! You won!')
else:
    print("Try next time. Good luck!")
