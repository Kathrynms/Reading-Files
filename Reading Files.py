
# opens file to read
employee_file = open("employees.txt", "r")

# To check to see if file is readable
print(employee_file.readable())

# to read the file
print(employee_file.read())

# to read a line of the file
print(employee_file.readline())

# to read the lines of the file
print(employee_file.readlines())

# to close the file
employee_file.close()

# opens file to write
# open("employees.txt", "w")

# opens file to append
# open("employees.txt", "a")

# opens file to read and write
# open("employees.txt", "r+")

