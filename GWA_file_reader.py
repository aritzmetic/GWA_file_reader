# Delera, Aritz B.

# Write a Python program that read a file containing the name of 20 students together with their GWA. 
# The program will outputs the name of the student who got the highest GWA (including the GWA).

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
print(f'Congratulations to {highest_student_name} for having the highest GWA of {highest_gwa}!')