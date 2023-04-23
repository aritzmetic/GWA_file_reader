# Delera, Aritz B.

# Import modules
import pyfiglet
import time
import random

opening = pyfiglet.figlet_format("= O.O.P =", font="starwars")
print(opening)

# Create an introduction
print("=" * 61)
print(" Welcome to AritzMetic's GWA Reader! ".center(60, "+"))
print("=" * 61)

# Ask the name of the user to create a greeting
name = input("\033[30mHi Smart Pipol! what is your name?: \033[0m")
print()
print("\033[40mHi", name, "! AritzMetic is here to help you in reading the Highest GWA!!\033[0m")

# create a student_name&gwa_record.txt and open it
with open('student_name&gwa_record.txt', 'r') as record_file:
    # set variables for highest gwa and person with highest gwa
    highest_student_name = ''
    highest_gwa = 5.0
# use for loop to iterate the file
    for record in record_file:
        # split the name of the student and their gwa
        student_name, gwa = record.split()
        # convert the gwa into float
        gwa = float(gwa)
        # create condition to update the file
        if gwa < highest_gwa:
            highest_student_name = student_name
            highest_gwa = gwa
            
# output the result
    print()
    print("Calculating results...")
    time.sleep(3)
    print()
    print(f'Congratulations to {highest_student_name} for having the highest GWA of {highest_gwa}!')
    time.sleep(3)

# Before exiting the application, include some pauses and random message prompts.
print()
print("loading...")
time.sleep(3)
print()
print(random.choice(["Thank you for using AritzMetic's GWA Reader!", "Goodbye and have a nice day!", "Stay curious and keep learning!"]))
time.sleep(2)
closing = pyfiglet.figlet_format(" = THE END = ", font="doom")
print(closing)