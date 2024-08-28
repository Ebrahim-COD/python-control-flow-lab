# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
# print_greeting()


# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():

    letter = input("Enter a letter: ")

    for let in letter:
        if let.isalpha() == False:
            print("Invalid input. Please enter a letter.")
            return
        
        if let.lower() in ['a', 'e', 'i', 'o', 'u']:
            print(f"The letter {let} is a vowel.")
        else:
            print(f"The letter {let} is a consonant.")


# Call the function
# check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():

    age = input("Please enter your age: ")
    
    if age.isnumeric() == False or int(age) >= 150:
        print("Invalid input. Please enter a valid age.")
        return

    age = int(age) 
    voting_age = 18

    if age <= voting_age:
        print("You are not old enough to vote.")
    else:
        print("You are old enough to vote.")


# Call the function
# check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog = input("Input a dog's age: ")

    if dog.isnumeric() == False:
        print("Invalid input! Please enter a valid age")    

    dog = int(dog)

    if dog == 1:
        dog_age = 10
    elif dog == 2:
        dog_age = 20
    else:
        dog_age = ((dog - 2) * 7) + 20


    print(f"The dog's age in dog years is {dog_age}.")
# Call the function
# calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    
    cold = input("Is it Cold: (yes/no) ")
    rain = input("Is it Raining: (yes/no) ")

    if cold.lower() == "yes" and rain.lower() == "yes":
        print("Wear a waterproof coat")
    elif cold.lower() == "yes" and rain.lower() == "no":
        print("Wear a warm coat")
    elif cold.lower() == "no" and rain.lower() == "yes":
        print("Carry an umbrella")
    elif cold.lower() == "no" and rain.lower() == "no":
        print("Wear light clothing")
    else:
        print("Please answer with yes or no")

# Call the function
# weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():

    month = input('Enter the month of the year (Jan - Dec) : ')[:3].capitalize()
    day = input('Enter the day of the month: ')

    if month not in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
        print("Please enter valid month.")
        return
    
    if day.isnumeric() == False or int(day) < 1  or int(day) > 31:
        print("Please enter valid day.")
        return
    
    if (month == "Feb" and int(day) > 29):
        print("Please enter valid day.")
        return
    
    if (month == "Apr" and int(day) > 30) or (month == "Jun" and int(day) > 30) or (month == "Sep" and int(day) > 30) or (month == "Nov" and int(day) > 30):
        print("Please enter valid day.")
        return
    
    day = int(day)

    if (month == "Dec" and 21 <= day <= 31) or (month == "Jan" and 1 <= day <= 31) or (month == "Feb" and 1 <= day <= 29) or (month == "Mar" and 1 <= day <= 19):
        season = "Winter"
    elif (month == "Mar" and 20 <= day <= 31) or (month == "Apr" and 1 <= day <= 30) or (month == "May" and 1 <= day <= 31) or (month == "Jun" and 1 <= day <= 20):
        season = "Spring"
    elif (month == "Jun" and 21 <= day <= 30) or (month == "Jul" and 1 <= day <= 31) or (month == "Aug" and 1 <= day <= 31) or (month == "Sep" and 1 <= day <= 21):
        season = "Summer"
    elif (month == "Sep" and 22 <= day <= 30) or (month == "Oct" and 1 <= day <= 31) and (month == "Nov" and 1 <= day <= 30) or (month == "Dec" and 1 <= day <= 20):
        season = "Fall"

    
    print(f'{month} {day} is in {season}.')
            
# Call the function
# determine_season()

# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():

    fixed_number = 42
    guess_number = input("Guess a number within a range(e.g, 1 to 100): ")
    guess_number = int(guess_number)
    user_tries = 1

    while user_tries < 5:
        if guess_number == fixed_number:
            print("Congratulations, you guessed correctly!")
            return
        elif guess_number < fixed_number:
            print("Guess is too low")
        else:
            print("Guess is too high")
        user_tries += 1
        if user_tries == 5:
            print("Last chance!")
        guess_number = int(input("Guess again: "))
    
    print("Sorry, you failed to guess the number in five attempts.")


# Call the function
guess_number()
