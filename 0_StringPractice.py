# Problem 1: Hello World!
# Given the following lines of code, work with your group members to place the lines in order and write and call your first Python function!

# a. print("Hello world!")
# b. def hello_world():
# c. hello_world()

def hello_world():
    print("Hello world!")


# Problem 2: Today's Mood
# The following function uses a variable, mood to print out "Today's mood: 😎". Copy this code to your Replit and update the mood variable to print out your mood for today.

def todays_mood():
    mood = "🥱"
    print("Today's mood: " + mood)

# Problem 3: Lunch Menu
# The following function accepts one parameter menu. Copy this code to your Replit and add a function call so that "Lunch today is: 🍕" is printed to the console.

def print_menu(menu):
    print("Lunch today is: " + menu)
    
    
# Problem 4: Sum of Two Integers
# The following function returns the sum of two integers: a and b.

def sum(a, b):
    return a + b
# Use the sum() function to calculate the sum of 13 and 27. Then, double the calculated sum and print the result to the console.

# Problem 5: Product of Two Integers
# Write a function product() that returns the product of two integers, a and b.

def product(a,b):
    return a * b

# Example Input: 22 and 7
# Example Result: 154


# Problem 6: Classify Age
# Write a function classify_age() that takes an integer age as a parameter and returns "child" if the age is less than 18, and returns "adult" otherwise.

# Example Usage:

# output = classify_age(18)
# print(output)
# output = classify_age(7)
# print(output)
# output = classify_age(50)
# print(output)
# Output:

# adult
# child
# adult

def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"

# Problem 7: What time is it?
# Let's put what we learned in Problems 1-4 all together! Write a function named what_time_is_it() that takes an integer hour as a parameter.
# If hour is 2, the function should return "taco time 🌮".
# If hour is 12, the function should return "peanut butter jelly time 🥪”.
# Otherwise, the function should return "nap time 😴".

# Example Usage:

# time = what_time_is_it(2)
# print(time)
# time = what_time_is_it(7)
# print(time)
# time = what_time_is_it(12)
# print(time)
# Output:

# taco time 🌮
# nap time 😴
# peanut butter jelly time 🥪

def what_time_is_it():
    final_ans = 0
    for num in range (1,6):
        final_ans += num
    return final_ans 

if __name__ == "__main__":
    print(what_time_is_it())