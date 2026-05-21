#conditions in python
#condition allows 
#simple if statement
#symtax :
     #if condition:
#         statement
#if comdition is false -> nothing runs

# example:
age = int (input("enter your age:"))

if age >= 18:
    print("you are eligible to vote")

#once again example:
age = int (input("enter your age:"))
if age >=18:
    print("you can drive the car")

#if-else statement
#syntax:
#if condition:
#   statement:
# else:
#   statement

#example:
age = 26
age = int (input("enter your age:"))
if age >=18:
    print("you can eligible to vote")
else:
    print("you are not eligible to vote")


#once again exmaple:
age = int (input("enter your age:"))
if age >=18:
    print("you can drive the car")
else:
    print("you can not drive the car")

#if-elif-else
# syntax:
#    if condition1:
#         statement
#    elif condition2:
#        statement
#    elif condition3:
#        statement
#    else:
#        statement

# marks = 1-40 = fail
# marks = 41-60 = c grade
# marks = 60-80 = b grade
# marks = 80 above = a grade
# marks = 89

marks = int(input("enter your marks:")) 
if marks >=80:
    print("grade a")   
elif marks >=60:
    print("grade c")
elif marks >=80:
    print("grade b")
else:
    print("fail")    

# simple if
#  check if a number is positive

number = int (input("enter a number:"))
if number > 0:
    print("the number is positive")

#check if a number is greater than 50
number = int (input("enter a number:"))
if number > 50:
    print("the number is greater than 50") 

#check if a number is even or odd
number = int (input("enter a number:"))
if number %2 == 0:
    print("the number is even")

#check if a person age is 18 or above
age = int (input("enter your age:"))
if age >= 18:
    print("you are eligible to vote")

#print "hello" only if the user enter 'pyhton
language = input("enter a programming language:")
if language == "python":
    print("hello")

# if-else
#check if a number is even or odd.

number = int (input("enter a number:"))
if number %2 == 0:
    print("the number is even")
else:
    print("the number is odd")

#check if a number is postive or negative.
number = int(input("enter a number:"))
if number > 0:
    print("the number is postive")
else:
    print("the number is negative")

#check if a student is pass or fail (pass if marks>=40).
marks = int(input("enetr your marks:"))
if marks >= 40:
    print("you are pass")
else:
    print("you are fail")

#check if a number is divisible by 5.
number = int(input("enter a number:"))
if number % 5 == 0:
    print("the number is divisible by 5")
else:
    print("the nummber is not divisible by 5")

# if-elif-else
#print grade based on marks: 90+->a, 75+->b, 60+->c, else->fail.
marks = int(input("enter your marks:"))
if marks >= 90:
    print("grade a")
elif marks >= 75:
    print("grade b")
elif marks >= 60:
    print("grade c")
else:
    print("fail")

#check the traffic light color: red->stop, yellow->ready, green->go.
light= input("enter the traffic light color:")
if light == "red":
    print("stop")
elif light == "yellow":
    print("ready")
elif light == "green":
    print("go")
else:
    print("invalid traffic light color")

#check temperature:>30->hot, 15-30->warm, <15->cold.
temperature = int(input("enter the temperature:"))
if temperature > 30:
    print("its hot today")
elif temperature <= 20:
    print("its normally today") 
else:
    print("its cold today")  

#nested 
