###How to Declare and use a Variable
a=100 
print (a)

###Re-declare a Variable: You can re-declare Python variables even after you have declared once.
# Declare a variable and initialize it
f = 0
print (f)
# re-declaring the variable works
f = 'guru99'
print (f)

###Python String Concatenation and Variable: In Python, while declaring variables in Python requires declaring the number as string otherwise it will show a TypeError
a = "Anu"
b = "Saharan"
c = 15
print(a+b+str(c)) #Once the integer is declared as string, it can concatenate
##print(a+b+c) #TypeError: can only concatenate str (not "int") to str

###Python Variable Types: Local & Global
f = 200
print(f)
def somefunction():
    f = "Inside function it is an local variable"
    print(f)
somefunction()
print(f)

##Example2:
a = 100
print(a)
def newfunction():
    global a
    print(a)
    a = "Assigning new value to global variable"
newfunction()
print(a)

### Delete a variable: You can also delete Python variables using the command del “variable name”.
#Example3:
b = 1000
print(b)

del b
#print(b)    #NameError: name 'b' is not defined