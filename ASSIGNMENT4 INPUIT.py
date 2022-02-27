#ASSIGNMENT4
#Q1
def TowerOfHanoi(n, rod1, rod3, rod2):
    if n==0:
         return
    TowerOfHanoi(n - 1, rod1, rod2, rod3)
    print("MOVE DISK", n, "FROM ROD", rod1,"TO ROD", rod3)
    TowerOfHanoi(n - 1, rod2, rod3, rod1)

n=3
TowerOfHanoi(n,'A','C','B')
#____________________________________________________________________________________
#Q2
from math import factorial

n = int(input('Enter number of rows: '))

print("USING ITERATIVE PROCEDURE")

for i in range(n):
    for j in range(n - i + 1):
        print(end=" ")
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()

print("USING RECURSSIONS")

def pascal(n, originalength=n):
    if n == 0:
        return
    pascal(n - 1, originalength)
    print('  ' * (originalength - n), end='')

    start = 1
    for i in range(1, n + 1):
        print(start, end='   ')

        start = start * (n - i) // i
    print()


pascal(n)
#______________________________________________________________________________________________
#Q3
number1= int(input("Enter first integer: "))
number2= int(input("Enter second integer: "))
QUOTIENT= number1/number2
REMAINDER= number1%number2
#a)
print(callable(QUOTIENT))
print(callable(REMAINDER))
#b)
if QUOTIENT == 0:
    print("QUOTIENT IS ZERO")
else:
    print("QUOTIENT IS NOT EQUAL TO ZERO")
if REMAINDER == 0:
    print("REMAINDER IS ZERO")
else:
    print("REMAINDER IS NOT EQUAL TO ZERO")
#c)
updated_list=[QUOTIENT+4,REMAINDER+4,QUOTIENT+5,REMAINDER+5,QUOTIENT+6,REMAINDER+6]
outcome = []
for i in range(len(updated_list)):
    if updated_list[i]>4:
        outcome.append(updated_list[i])
print("REQUIRED LIST IS:",outcome)
#d)
SET = set(outcome)
print("SET DATATYPE",SET)
#e)
IMMUTABLE_SET=frozenset(SET)
print('IMMUTABLE SET IS: ',IMMUTABLE_SET)
#e)
MAXIMUM_VALUE_AND_ITS_HASH_VALUE= hash(max(IMMUTABLE_SET))
print("MAXIMUM VALUE AND ITS HASH VALUE IS:",MAXIMUM_VALUE_AND_ITS_HASH_VALUE)
#_______________________________________________________________________________________
#Q4
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def __del__(self):
        print("OBJECT DESTROYED!")

Student_1 = Student("ARSH SHARMA",21103057)
print("OBJECT CREATED!")
print(f"STUDENT'S NAME IS {Student_1.name} AND ROLL NUMBER IS {Student_1.roll_number}.")
del Student
print("DONE")
#________________________________________________________________________________________
#Q5
class EmployeeDetails:
    def __init__(self, NAME, SALARY):
        self.NAME = NAME
        self.SALARY = SALARY
EMPLOYEE_1 = EmployeeDetails("MEHAK", 40000)
EMPLOYEE_2 = EmployeeDetails("ASHOK", 50000)
EMPLOYEE_3 = EmployeeDetails("VIREN", 60000)
#a)
EMPLOYEE_1.SALARY = 70000
print(f"SALARY OF {EMPLOYEE_1.NAME} INCREASED TO {EMPLOYEE_1.SALARY}")
print("SALARY UPDATED!")
#b)
print("Record of VIREN deleted!")
del EMPLOYEE_3
#________________________________________________________________________________________
#Q6
WORD = input("Enter any word: ")
WORD = WORD.lower()

NEW_WORD = input("Enter a new according to game rules: ")
NEW_WORD = NEW_WORD.lower()


def DICTIONARY(word):
    recheck = {}
    LIST = list(word)

    n = len(LIST)
    for i in range(n):
        if LIST[i] in recheck:
            recheck[LIST[i]] += 1
        else:
            recheck[LIST[i]] = 1
    return recheck

def INPUT():
    if DICTIONARY(WORD) != DICTIONARY(NEW_WORD):
        print("The letters do not match, FAKE FRIENSHIP!!")
        return
    TEST = input("IS IT A MEANINGFUL WORD? (y/n )")

    if TEST == 'y':
        print("THEY PASS!!")
    elif TEST == 'n':
        print("THEY FAILED!!,FAKE FREIENSHIP")
    else:
        print("Invalid input,try again with y/n")
        INPUT()


INPUT()
#_____________________________________________________________________________________________________

