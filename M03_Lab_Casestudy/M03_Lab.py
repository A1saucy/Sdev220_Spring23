# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 07:56:32 2023

@author: mrapp
"""
if __name__== "__main__":
    pass


def Vehicle(): 
    def automobile():
        year = input("the year: ")
        make = input("the make: ")
        model = input("the model: ")
        doors = input("number of doors: ")
        roof = input("Sunroof or nothing: ")
        print( "Your car is a", str(year) , make, model, "and has", str(doors),"doors", "and a", roof + ".")
    def truck():
        print("Alright big shot")
    def plane():
        print("You are part of the mile high club")
    def boat():
        print("That's pretty swell cap")
    def broomstick():
        print("You scary")
        
    words = (input("What do you drive? "))
    if words == 'car':
        return automobile()
    elif words == 'truck':
        return truck()
    elif words == 'plane':
        return plane()
    elif words == 'boat':
        return boat()
    elif words == 'broomstick':
        return broomstick()
Vehicle()
