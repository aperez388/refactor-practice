shopping_list = ["apples", "bananas", "carrots"]

def Add():
    shopping_list.append("dates")

def Remove():
    shopping_list.remove("bananas")

def PrintAll():
    for item in shopping_list:
        print(item)