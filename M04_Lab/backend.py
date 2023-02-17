from fastapi import FastAPI



app = FastAPI()

inventory = {
        1: {
           "id": 1,
           "book_name": "Introducing Python, 2nd edition",
           "author": "Bill Lubanovic",
           "publisher": "O'Rielly Media,Inc"
           
        },#end of 1
        
        2: {
       "id": 2,
       "book_name": "Python Crash Course, 2nd edition",
       "author": "Eric Matthes",
       "publisher": "No Starch Press"
       
       },
        3:{
            "id": 3,
            "book_name": "Cracking Codes with Python: An Introduction to Building and Breaking Cyphers",
            "author": "Al Sweigart",
            "publisher": "No Starch Press"
            }#end of 3
        
        

    }#end of inventory

@app.get("/get-item")
def get_item():
    for i in inventory:
        return inventory