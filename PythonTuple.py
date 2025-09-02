###Tuple Syntax, Also Tuple indices begin at 0
Tup = ('Jan','feb','march')
print(Tup)
##To write an empty tuple
tup1 =()
print(tup1)
##For writing tuple for a single value, you need to include a comma, even though there is a single value. Also at the end you need to write semicolon as shown below.
tup2 = (50);
print(tup2)

##Tuple Assignment: Python has tuple assignment feature which enables you to assign more than one variable at a time. In here, we have assigned tuple 1 with the persons information like name, surname, birth year, etc. and another tuple 2 with the values in it like number (1,2,3,….,7).
# Example1:
tup4 = ('Anu','30','Tester','HR');
tup5 = (1,2,3,4,5,6,7,8,9)
print(tup4[0])
print(tup5[1:4])

##Packing and Unpacking : In packing, we place value into a new tuple while in unpacking we extract those values back into variables.
# Example2:
a = ("Anu", 40 , "Tester") #Packing
print(a)
(Name, Age , Profession) = a #Unpacking
print(Name)
print(Age)
print(Profession)