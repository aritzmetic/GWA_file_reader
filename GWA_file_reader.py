# Delera, Aritz B.

# Write a Python program that read a file containing the name of 20 students together with their GWA. 
# The program will outputs the name of the student who got the highest GWA (including the GWA).

# create a student_name&gwa_record.txt and open it
with open('student_name&gwa_record.txt', 'r') as record_file:
    for line in record_file:
        print(line.strip())

# create the lists of students with their gwa to the text file
# set variables for highest gwa and person with highest gwa
# use for loop to iterate the file
# split the name of the student and their gwa
# convert the gwa into float
# create condition to update the file
# output the result