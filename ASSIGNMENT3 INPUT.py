#ASSIGNMENT3
#___________________________________________________________________________________________________________________________________
#Q1
#count number of characters
statement=input("Enter a string: ")
statement=statement.strip()        #so that initial and final spaces are not counted
if ' ' in statement:               #this means entered string is a sentence.
     statement=statement+' '
     while len(statement)>0:
           print(statement[0:statement.find(' ')+1],statement.count(statement[0:statement.find(' ')]))
           statement=statement.replace(statement[0:statement.find(' ') + 1], '')
else:
     while len(statement)>0:
          print(statement[0], statement.count(statement[0]))
          statement=statement.replace(statement[0], '')
#____________________________________________________________________________________________________________________________________
#Q2
#python script to print next date of input date
#using if-elif
date=int(input('Enter a date: '))
month=int(input('Enter a month: '))
year=int(input('Enter a year:'))
if 1<=date<=31 and 1<=month<=12 and 1800<=year<=2025:
    if date==31 and month==12:
        print('Date: ',"1/","1/",year+1)
    elif date==31 and month in [1,3,5,7,8,10]:
        print('Date: ',"1/",month+1,year)
    elif date==30 in month [4,6,9,11]:
        print('Date:',"1/",month+1,year)
    elif date==29 in month==2 in year//4==0:
        print('Date:',"1/","3/",year)
    elif date==28 in month ==2 in year//4 !=0:
        print('Date:',"1/","3/",year)
    else:
        print('Date:',date+1,"/",month,"/",year)
else:
    print("INVALID!,KINDLY ENTER A VALID DATE")
#_______________________________________________________________________________________________________________________________________
#Q3
list = []
elements=int(input('Enter number of elements: '))
for i in range(0,elements):
    enter_elements=int(input())
    list.append(enter_elements)
print('list:',list)
list_of_tuples=[]
for i in list:
    list_of_tuples.append((i,i**2))
print("Output:",list_of_tuples)
print("FINISH!")
#_________________________________________________________________________________________
#Q4
Grade_point=int(input("Enter the grade:- "))
if(Grade_point==4):
    print("Your Grade is 'D' and Poor performance.")
elif(Grade_point==5):
    print("Your Grade is 'C' and Below Average performance.")
elif(Grade_point==6):
    print("Your Grade is 'C+' and Average performance.")
elif(Grade_point==7):
    print("Your Grade is 'B' and Good Performance.")
elif(Grade_point==8):
    print("Your Grade is 'B+' and Very Good performance.")
elif(Grade_point==9):
    print("Your Grade is 'A' and Excellent performance.")
elif(Grade_point==10):
    print("Your Grade is 'A+' and Outstanding performance.")
else:
    print("Error-Grade entered does not matches the given criteria.")
print("Done!")
#___________________________________________________________________________________________
#Q5
#forming a pattern
characters="ABCDEFGHIK"
for i in range(1,7):
    print(characters[0:2*(6-i)+1].center(11))
#____________________________________________________________________________________________
#Q6
dictionary_of_student_detail={}
while 1:
    LOOP=input("enter Y to continue ,enter N to exit ")
    if LOOP=='Y':
        SID=int(input("Enter SID "))   #do not enter same sid for two or more students.
        name=input("Enter name ")
        dictionary_of_student_detail.update({SID:name})
    elif LOOP=="N":
        break
    else:
        print("INVALID!! Enter only Y or N:")    
if len(dictionary_of_student_detail):
#a)
    print("STUDENT DETAILS:",dictionary_of_student_detail)         
#b)
    names=[]
    for LOOP in dictionary_of_student_detail.values():
      names.append(LOOP)
    names.sort()
    print("LIST SORTED BY NAMES:")
    for a in names:
      for b in dictionary_of_student_detail:
        if a==dictionary_of_student_detail[b]:
           print(b,dictionary_of_student_detail[b])

#c)
    SID=[]
    print("SORTED SID:")
    for LOOP in dictionary_of_student_detail.keys():
       SID.append(LOOP)
    SID.sort()
    for a in SID:
      print(a,dictionary_of_student_detail[a])

#d)
    SID = int(input("Enter the SID: "))
    if SID in dictionary_of_student_detail.keys():
        print (dictionary_of_student_detail[SID])
    else:
        print('NO RESULT FOUND!')
else:
     print("NO DATA AVAILABLE!")

#_____________________________________________________________________________________________
#Q7
numb1=1
numb2=1
numb3=0
Series=int(input("enter number of terms of fibonacci series "))
sum=0
count=0
print(numb1)
print(numb2)
for i in range(3,Series+1):
    numb3=numb2+numb1      #fibonaaci series is a3=a2 + a1
    print(numb3)
    numb1=numb2
    numb2=numb3
    sum+=numb3
    count+=1
average=sum/count
print("Average is:",average)

#____________________________________________________________________________________________
#Q8
Set1 = {1,2,3,4,5}
Set2 = {2,4,6,8}
Set3 = {1,5,9,13,17}
#a.
New_Set = Set1^Set2
print('NEW SET',New_Set)
#b
New_Set = Set1^(Set2^Set3)
print('NEW SET',New_Set)
#c
New_Set = (Set1&Set2)|(Set2&Set3)|(Set3&Set1)
print('NEW SET',New_Set)
#d
Set={1,2,3,4,5,6,7,8,9,10}
New_Set = Set-Set1
print('NEW SET',New_Set)
#e
Set={1,2,3,4,5,6,7,8,9,10}
New_Set = Set-(Set1|Set2|Set3)
print('NEW SET',New_Set)

print('FINISH!')
#___________________________________________________________________________________________

