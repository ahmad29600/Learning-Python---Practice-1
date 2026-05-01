#Number Guessing Game

# import random
# random_number = random.randint(1, 10)

# guess = 0

# while guess != random_number:
#     guess = int(input("Guess the number: "))
#     if guess < random_number:
#         print("Too Low! Guess Again...")
#     elif guess > random_number:
#         print("Too High! Guess Again...")
#     else:
#         print("Congratulations! You have guessed correct number.")



# Calculator

# Creating Functions

# Function for Addition
# def addition (number_one, number_two):
#     add_numbers = number_one + number_two
#     print("The sum of your two number is:", add_numbers)


# # Function for Multiplication
# def multiplication (number_one, number_two):
#     multi_numbers = number_one * number_two
#     print("The sum of your two number is:", multi_numbers)


# # Function for Substraction
# def substract (number_one, number_two):
#     minus_numbers = number_one - number_two
#     print("The sum of your two number is:", minus_numbers)


# # Function for Division
# def division (number_one, number_two):
#     divide_numbers = number_one / number_two
#     print("The sum of your two number is:", divide_numbers)

# # Functions Finished    

# while True:

#     number_one = float(input("Enter Your 1st Number: "))
#     number_two = float(input("Enter Your 2nd Number: "))
#     operation_done = input("What operation you want to do: ")

#     if operation_done == "+":
#         addition (number_one, number_two)
#     elif operation_done == "*":
#         multiplication (number_one, number_two)
#     elif operation_done == "/":
#         division (number_one, number_two)
#     elif operation_done == "-":
#         substract (number_one, number_two)
#     else:
#         print(""""You can only do these operations: "+", "-", "/" and "*" """)

#     user_choice = input("Do you want to continue? (y/n): ").lower()
#     if user_choice != "y":
#         print("You quit.")
#         break




# Quiz Game

# score = 0

# while True:
#     question1  = input("What is the capital city of Pakistan?: ").lower()
#     question2  = input("What is the national flower of Pakistan?: ").lower()
#     question3  = input("What is the national sport of Pakistan?: ").lower()
    

#     if question1 == "islamabad":
#         score += 1
#         if question2 == "jasmine":
#             score += 1
#             if question3 == "hockey":
#                 score += 1
#             else:
#                 print("Wrong answer for question 3! Game Over... and score is:", score)
#         else:
#             print("Wrong answer for question two! Game Over... and score is:", score)
#     else:
#         print("Wrong answer for question one! Game Over... and score is:", score)

#     choice = input("Do you want to continue? (y/n): ").lower()
#     if choice != "y":
#           break



# Student Result System
# def get_marks(subject):
#     while True:
#         try:
#             value = int(input(f"Enter marks for {subject} (0-100): "))
#             if 0 <= value <= 100:
#                 return value
#             else:
#                 print("Marks must be between 0 and 100.")
#         except ValueError:
#             print("Invalid input")

# English = get_marks("Enlish")
# Math = get_marks("Math")
# Science = get_marks("Science")
# Urdu = get_marks("Urdu")

# English = int(input("Enter the marks for English (1-100): "))
# Math = int(input("Enter the marks for Math (1-100): "))
# Science = int(input("Enter the marks for Science (1-100): "))
# Urdu = int(input("Enter the marks for Urdu (1-100): "))

# total = English + Math + Science + Urdu
# average = total / 4

# if average >= 90:
#     grade = "A+"
# elif average >= 80:
#     grade = "A"
# elif average >= 70:
#     grade = "B"
# elif average >= 60:
#     grade = "C"
# elif average >= 50:
#     grade = "D"
# else: 
#     grade = "F"

# print(f"Your obtained {total} marks. \nGrade is: {grade}")



# Kon Bane Ga Crore Pati

prize = 0

while True:
    question1 = input("What is the capital of Pakistan?: ").lower()

    if question1 == "islamabad":
        prize += 1
        print(f"You won {prize} crore.")

        question2 = input("What is the first capital of Pakistan?: ").lower()

        if question2 == "karachi":
            prize += 1
            print(f"You won {prize} crore.")
        else:
            print("Wrong answer!")
            break
    else:
        print("Wrong answer!")
        break

    break  # stops after completing both questions