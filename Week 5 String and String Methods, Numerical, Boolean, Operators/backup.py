import tkinter
import serial

print("Hello World Double Quote")
print('Hello World Single Quote')
print('Leonel Said "Hello World Single Quote!!!"')
print("Leonel Said 'Hello World Single Quote!!!'")
print("Leonel Said \"Hello World Single Quote!!!\"")

print(input("Enter your PIN number : "))

#string "!@#$%^&*()_asdfghjk123456789"

firstName = input("Enter your First Name : ")
lastName = input("Enter your Last Name : ")

print("Your Full name is : " + firstName + " " + lastName)

print("First Line")
print("Second Line")
print("Third Line")
print("Fourth Line")
print("Fifth Line")
print("Sixth Line")
print("Seventh Line")


#java
#45 integer
#45.1 float
#45213421312321312 long
#45.21312321312323123123 double
#"hello" string
#'h' char
myNum1 = 45
myNum2 = 45.5
myNum3 = 45123213213123123216545454676576567456456456435645475456535435654765465354354654635435432543634564654653543463465465
myNum4 = 45.123123123123232

myString = "hello world !@#$%^&*() 12312312327"
age1 = "21"
age2 = "25"
sum = age1 + age2
print(sum)

myString1 = "Hello"
myString2 = " World"
sum = myString1 + myString2
print(sum)

#this is a single line comment
print("hello world")

'''
this is
a
multi
line
comment
'''

a = input("Enter first number : ")
b = input("Enter second number : ")
c = input("Enter third number : ")

mySum = int(a) + int(b) + int(c)

print(mySum)



#convert to int -> int(variable)
#convert to string -> str(variable)
#fstring or formatted string

myAge = 45
myName = "Leonel Calderon"

#print("I am : " + myName + " and my age is : " + myAge)
print("I am : " + myName + " and my age is : " + str(myAge))
print(f"I am : {myName} and my age is : {myAge}")



strFullName = "Leonel Calderon"
intLength = len(strFullName)
print(intLength)
print(strFullName[0])
print(strFullName[5])
print(strFullName[intLength - 1])
#print(strFullName[15]) #string index out of range

strInputFromUser = "Jose Rizal"

strFullName = strInputFromUser
print(strFullName)
intLength = len(strFullName)
print(intLength)



strFullName = "Leonel Calderon"
#upper
newValue = strFullName.upper()
print(newValue)

#count
newValue = strFullName.count("e")
print(newValue)

#split
newValue = strFullName.split(" ")
print(newValue)
newValue = strFullName.split("e")
print(newValue)
newValue = strFullName.split("ald")
print(newValue)

#replace
newValue = strFullName.replace("Leonel", "Jun Mar")
print(newValue)

#join
strFirstName = "Leonel"
strMiddleName = "Co"
strLastName = "Calderon"
strFullName = "_".join([strFirstName, strMiddleName, strLastName])
print(strFullName)

newValue = strFullName.isnumeric()
print(newValue)

#Leonel_Co_Calderon #substring
newValue = strFullName[2:9] #[included:excluded]
print(newValue)
newValue = strFullName[2:9:2] #[included:excluded:step]
print(newValue)
#return the lowest index available
print(strFullName.index("e"))
print(strFullName.index("e", 2,9))

strInput = "27131283128leon2312031290el2312039 321093210392calde138293ron"

newString = ""
for char in strInput:
    if not char.isnumeric():
        newString = newString + char

print(newString)


import math
import mathplot

#Numerical integer (-3,0,562) float (23.23252) complex number (45 + 25i)
#i = ampere, j = imaginary resistance 25 + j25 = impedance
myIntegerA = 25
myIntegerB = 15
myIntegerC = 5
myFloatA = 25.45
myFloatB = 14.55
myComplexA = 25 - 3j
myComplexB = 10 - 12j
#+, -, /, *
mySum = myIntegerA + myIntegerB
print(mySum)
myDiff = myIntegerA - myIntegerB
print(myDiff)
myProd = myIntegerA * myIntegerB
print(myProd)

result = 2 ** 6 #exponent
print(result)

myQo = myIntegerA / myIntegerB
print(myQo)
myRoundedQo = round(myQo, 2)
print(myRoundedQo)
remainder = myIntegerA % myIntegerC #modulus
print(remainder)
remainder = myIntegerA % myIntegerB #modulus
print(remainder)
#PARENTHESIS, MULTIPLICATION, DIVISION, ADDITION, SUBTRACTION
myComProd = myComplexA * myComplexB
print(myComProd)
print(5*4*3*2*1)
print(math.factorial(5))
cos_90_deg = math.cos(math.radians(60))
print(cos_90_deg)


isPresent = False #boolean
isExist = True  #boolean
isAvailable = "True"  #string
isValid = 1  #integer
isOkay = 0 #integer
isNumeric = False  #boolean
myChar = "5"
isNumeric = myChar.isnumeric()
strIsNumeric = str(myChar.isnumeric())
print([isNumeric])
print([strIsNumeric])
#Comparison Operator
# ==, >=, > , <=, <, !=
a = 5
b = 6
isEqual = (a == b) #False
print(isEqual)
isGTE = (a >= b)  #False
print(isGTE)
isLTE = (a <= b)  #True
print(isLTE)

#membership AND identity operator
#in, not in, is, is not
isIn = (5 in [25, 45, 23, 12, 5, 27])
print(isIn) #True
isIn = (5 in [25, 45, 23, 12, 27])
print(isIn) #False
isIn = ("hello" in  "hello world hi eath")
print(isIn) #True

isIS = ("hello" is "hello")
print(isIS) #True
isIS = ("hello" is "hi hello")
print(isIS) #False

#LOGICAL OPERATOR
#AND OR NOT NAND NOR ---------- EXOR, EXNOR

isOkay = (5 in [25, 45, 23, 12, 5, 27]) and (5 in [25, 45, 23, 12, 27])
print(isOkay) #False
isOkay = (5 in [25, 45, 23, 12, 5, 27]) or (5 in [25, 45, 23, 12, 27])
print(isOkay) #True




intLength = len(strFullName) #len for length
#function call - ( )
#range or index - [ ]
#list [ ]
print(strFullName)
print(intLength)
print(strFullName[0])
print(strFullName[5])
print(strFullName[6])
print(strFullName[14])
print(strFullName[intLength-1])

mySubString = strFullName[2:5:1]  #[start included, end excluded, step]
print(mySubString) #substring or slicing

#print(strFullName[25]) IndexError: string index out of range
strFullName = strFullName + "a"
print(strFullName)



strFullName = "LeoNel CaldeRon"

#String methods

newValue = strFullName.upper()
print(newValue)
newValue = strFullName.lower()
print(newValue)
newValue = strFullName.capitalize()
print(newValue)

newValue = strFullName.split(" ")
print(newValue)
newValue = strFullName.split("eo")
print(newValue)

newValue = strFullName.replace("e", "a")
print(newValue)
newValue = strFullName.replace("eoNel", "olobron")
print(newValue)
newValue = strFullName.replace("e", "")
print(newValue)

myFirstName = "Leonel"
myMiddleName = "Co"
myLastName = "Calderon"

myFullNameList = [myFirstName, myMiddleName, myLastName]

print("POGI".join([myFirstName, myMiddleName, myLastName]))
print("POGI".join(myFullNameList))

newValue = strFullName.count("e")
print(newValue)

myChar = strFullName[2]
print(myChar)
intIndex = strFullName.index("o")
print(intIndex)


#STRING
import math
import graphlib
import mathplot
#NUMERIC TYPE
#INTEGER -10, 0, 2324
#FLOAT 25.2323
#COMPLEX 25 + 47j  #i ampere, j impendance -> resistance + reactance
intA = 25
intB = 15
intC = 5
#aritmetic operations
intSum = intA + intB + intC
print(intSum)
intDiff = intA - intB
print(intDiff)
intProd = intA * intB
print(intProd)
intQu = intA / intB
print(intQu)
intResult = intA ** intB
print(intResult)

intA = 555
intB = 4
intC = 5

isDivisible = False
remainder = intA % intB #modulus or the percent sign returns the remainder
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)

isDivisible = False
remainder = intA % intC
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)

#PMDAS

intAngle = 90
result = round(math.cos(math.radians(intAngle)), 1)
print(result)
result = round(math.sin(math.radians(intAngle)), 1)
print(result)
result = round(math.tan(math.radians(intAngle)), 1)
print(result)
intAngle = 45
result = round(math.tan(math.radians(intAngle)), 1)
print(result)

intX = 5 #5! 5x4x3x2x1
facResult = math.factorial(intX)
print(facResult)

myComA = 25+5j
myComB = 10-10j
comProd = myComA * myComB
print(comProd)

#Comparison Operator
# ==, >, <, >=, <=, !=
#BOOLEAN DATATYPE True or False
#"True" 'True' - String
# 1 or 0 - Integer
intA = 5
intB = 6
isResult = intA == intB
print(isResult) #False
isResult = intA <= intB
print(isResult)  #True
isResult = intA >= intB
print(isResult)  #False
isResult = intA != intB
print(isResult)  #True
isResult = intA > intB
print(isResult)  #False
isResult = intA < intB
print(isResult)  #True



#membership operator in, not in
isResult = "e" in "madagascar"
print(isResult)  #False
isResult = "e" in "medegescer"
print(isResult)  #True
myList = ["bearbrand", "nescafe", "joy", "alcohol", "tissue", "paper cup"]
isResult = "biscuit" in myList
print(isResult)#False
myList = ["bearbrand", "nescafe", "joy", "alcohol", "tissue", "paper cup", "biscuit"]
isResult = "biscuit" in myList
print(isResult)#True
isResult = "dege" in "medegescer" #CONTAINS
print(isResult)  #True

#identity operator is, is not
isResult = "dege" is "medegescer" #EXACT
print(isResult)  #False
isResult = "medegescer" is "medegescer" #EXACT
print(isResult)  #True
isMyResult = isResult is True #EXACT
print(isMyResult)  #True


myInput = '1231hel1231312lo2313 23123231w231orld123'
myOutput = ""
for char in myInput:
    if not char.isnumeric(): #kung ang sagot mo ay hindi, pasok ka
        myOutput = myOutput + char
    else:
        print(f"Hindi pasok yan kasi yan ay: {char} ")
print(myOutput)


#LOGICAL OPERATOR
#NOT, AND, OR --------- NAND, NOR, EXOR, EXNOR
#LOGIC CIRCUITS AND SWITCHING THEORY
isGroupPassed = False
passingGrade = 85
markGrade = 75
jennyGrade = 95
arthurGrade = 86
isMarkPassed = markGrade >= passingGrade
print(isMarkPassed)
isJennyPassed = jennyGrade >= passingGrade
print(isJennyPassed)
isArthurPassed = arthurGrade >= passingGrade
print(isArthurPassed)
isGroupPassed = isMarkPassed and isJennyPassed and isArthurPassed
print(isGroupPassed)
isGroupPassed = isMarkPassed or isJennyPassed or isArthurPassed
print(isGroupPassed)

#LOGICAL OPERATOR
#NOT, AND, OR --------- NAND, NOR, EXOR, EXNOR
#LOGIC CIRCUITS AND SWITCHING THEORY
isGroupPassed = False
passingGrade = 85
markGrade = 75
jennyGrade = 95
arthurGrade = 86
isMarkPassed = markGrade >= passingGrade
print(isMarkPassed)
isJennyPassed = jennyGrade >= passingGrade
print(isJennyPassed)
isArthurPassed = arthurGrade >= passingGrade
print(isArthurPassed)
isGroupPassed = isMarkPassed and isJennyPassed and isArthurPassed
print(isGroupPassed)
isGroupPassed = isMarkPassed or isJennyPassed or isArthurPassed
print(isGroupPassed)


intA = 555
intB = 5
intC = 4

isDivisible = False #initial value
remainder = intA % intB #modulus or the percent sign returns the remainder
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)

isDivisible = False #initial value <--------------------------------------
remainder = intA % intC
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)









