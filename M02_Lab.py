# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Danny Contreras
# M02 Lab
# The program will accept the first and last names of students as well
# as their gpa and check it against parameters

# Program goals
#input of students first name and last name , gpa 
#quit processing if input is equal to 'ZZZ'
#if student gpa is => 3.5 print student made Deans list
#if student gpa is => 3.25 <3.4 print student made honor roll
#must use five students

deans_List = 3.5
honor_Roll = 3.25

#error = "ZZZ" , "zzz"



student1_Fname = input("Enter the first name: ") 
while student1_Fname == "ZZZ" or student1_Fname == "zzz":
    student1_Fname = input("Please enter a valid first name: ")

student1_Lname = input("Enter the last name: ")
while student1_Lname == "ZZZ" or student1_Lname == "zzz":
    student1_Lname = input("Please enter a valid last name: ")
    
student1_Name = student1_Fname + " " + student1_Lname + ": "
student1_Gpa = float(input("Enter the Gpa for "+ (student1_Name)))

if student1_Gpa >= deans_List:
    print(student1_Fname, student1_Lname, "made the Dean's list. ")
else:
    if student1_Gpa >= honor_Roll or student1_Gpa < deans_List:
        print(student1_Fname, student1_Lname, "made honor roll.")
    