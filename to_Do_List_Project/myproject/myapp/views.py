from django.shortcuts import render
from django.http import HttpResponse
import csv
import requests

from .models import *

# Create your views here.


def myview(request):
    message = "OnTask To-do List"
    statement = "Write down anything you don't want to forget!"
    return render(request, "home.html", {"message": message, "statement": statement})
    #return HttpResponse("Hello world")

def notes(request):
    response = request.get("http://127.0.0.1:8000/").html()
    return render(request,"home.html", {"response": response})

def writeFile(request):
    #zero = str(request.GET["container0"])
    #one = str(request.GET["container1"])
    #two = str(request.GET["container2"])
    #three = str(request.GET["container3"])
    #four = str(request.GET["container4"])
    #five = str(request.GET["container5"])
    #six = str(request.GET["container6"])


    with open("C:\\Sdev220GitStuff\\to_Do_List_Project\\myproject\\container.csv", "w") as toFile:
        zero = ["Container0",str(request.POST["Container0"])]
        one = ["Container1",str(request.POST["Container1"])]
        two = ["Container2",str(request.POST["Container2"])]
        three = ["Container3",str(request.POST["Container3"])]
        four = ["Container4",str(request.POST["Container4"])]
        five = ["Container5",str(request.POST["Container5"])]
        six = ["Container6",str(request.POST["Container6"])]
        containers = [zero,one,two,three,four,five,six]


        writer = csv.writer(toFile)
        for i in containers:
            writer.writerow(i)
        return None
            

def readFile(request):
    inputs = {}
    with open("C:\\Sdev220GitStuff\\to_Do_List_Project\\myproject\\container.csv", "r") as fromFile:
        reader = csv.reader(fromFile)

        for row in reader:
            if row[0] == "Container0":
                inputs["Container0"] = row[1]
            elif row[1] == "Container1":
                inputs["Container1"] = row[1]
            elif row[2] == "Container2":
                inputs["Container2"] = row[1]
            elif row[3] == "Container3":
                inputs["Container3"] = row[1]
            elif row[4] == "Container4":
                inputs["Container4"] = row[1]
            elif row[5] == "Container5":
                inputs["Container5"] = row[1]
            elif row[6] == "Container6":
                inputs["Container6"] = row[1]
            inputs = {"Container0": row[1], "Container1": row[1], "Container2": row[1], "Container3": row[1], "Container4": row[1], "Container5": row[1], "Container6": row[1] }
            return render(request,"homeResponse.html", inputs)


    
    








