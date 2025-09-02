##First Python Program
print("Hello World!")
##If you want to print the name of five countries, you can write:
print("India")
print("USA")
print("China")
print("Japan")
print("Russia")

### How to print blank lines:
##Sometimes you need to print one blank line in your Python program. Following is an example to perform this task using Python print format.
#Let us print 8 blank lines:
print(8*"\n") #or print ("\n\n\n\n\n\n\n\n\n")
print("This is how we can print blank line")

### Print end command
##By default, print function in Python ends with a newline. This function comes with a parameter called ‘end.’ The default value of this parameter is ‘\n,’ i.e., the new line character. You can end a print statement with any character or string using this parameter. This is available in only in Python 3+
#Example:
print("Welcome to", end=" ")
print("Learning Platform", end="! \n") # or print("Learning Platform!")
#Example2:
print("Welcome to", end="\t")
print("Learning Platform", end="!")
#Example3:
print("Welcome to", end=" ")
print("Learning Platform!")

print("Welcome to", end="\t")
print("Learning Platform", end="!")