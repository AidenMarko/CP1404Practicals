"""
CP1404/CP5632 - Practical
Do-from-scratch: Files
"""

# Question 1
out_file = open('name.txt', 'w')
name_input = input("Enter your name: ")
print(name_input, file=out_file)
out_file.close()
# ----------

# Question 2
in_file = open('name.txt', 'r')
name_output = in_file.read()
print("Your name is {}".format(name_output.title()))
in_file.close()
# ----------

# Question 3
in_file = open('numbers.txt', 'r')
first_line = in_file.readline()
second_line = in_file.readline()
result = int(first_line) + int(second_line)
print("The result is: {}".format(result))
in_file.close()
# ----------

# Question 4
in_file = open('numbers.txt', 'r')
file_total_value = 0
line_value = 0
while True:
    try:
        line_value = in_file.readline()
        file_total_value += int(line_value)
    except ValueError:
        break
print('output: {}'.format(file_total_value))
in_file.close()
# ----------
