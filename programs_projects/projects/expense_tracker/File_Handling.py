# # The open() function takes two parameters; filename, and mode. and function returns a file objec
# # There are four different methods (modes) for opening a file:
# #     "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# #     "a" - Append - Opens a file for appending, creates the file if it does not exist
# #     "w" - Write - Opens a file for writing, creates the file if it does not exist
# #     "x" - Create - Creates the specified file, returns an error if the file exists
# # In addition you can specify if the file should be handled as binary or text mode
# #     "t" - Text - Default value. Text mode
# #     "b" - Binary - Binary mode (e.g. images)

file_open = open("programs_projects\projects\expense_tracker\expense_data_1.csv", "r")

# # read() method for reading the content of the file which  returns the whole text
# print(file_open.read())

# # But We can also specify how many characters you want to return:
# print(file_open.read(50)) # Return the 50 first characters of the file:

# # readline() method for reading the one line of the file
# print(file_open.readline()) # reading the 1st line
# print(file_open.readline()) # reading the 2nd line
# print(file_open.readline()) # reading the 3rd line

# # It is a good practice to always close the file when you are done with it.
# file_open.close()


# # Can also use the 'with' statement when opening a file, and also do not have to worry about closing the files 
with file_open as f:
    # print(file_open.read())
    
    # # By looping through the lines of the file, you can read the whole file, line by line: 
    for x in f:
        print(x)