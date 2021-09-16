import datetime


def gettime():
    return datetime.datetime.now()


def take(a):
    if a == 1:
        b = int(input("Enter 1 for food and 2 for exercise\n"))
        if b == 1:
            value = input("Enter the food name which u eat.\n")
            with open("Daniel_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Record recorded successfully.\n")
        elif b == 2:
            value = input("Enter the exercise u done.\n")
            with open("Daniel_exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Record recorded successfully.\n")

    elif a == 2:
        b = int(input("Enter 1 for food and 2 for exercise\n"))
        if b == 1:
            value = input("Enter the food name which u eat.\n")
            with open("Kein_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Record recorded successfully.\n")
        elif b == 2:
            value = input("Enter the exercise u done.\n")
            with open("Kein_exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Record recorded successfully.\n")

    elif a == 3:
        b = int(input("Enter 1 for food and 2 for exercise\n"))
        if b == 1:
            value = input("Enter the food name which u eat.\n")
            with open("Chris_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Record recorded successfully.\n")
        elif b == 2:
            value = input("Enter the exercise u done.\n")
            with open("Chris_exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Record recorded successfully.\n")

    else:
        print("Please Enter a valid input :- 1(Daniel), 2(Kein), 3(Chris)\n")


def retrieve(a):
    if a == 1:
        b = int(input("Enter 1 for food and 2 for exercise\n"))
        if b == 1:
            with open("Daniel_food.txt") as op:
                for i in op:
                    print(i, end="")
        elif b == 2:
            with open("Daniel_exercise.txt") as op:
                for i in op:
                    print(i, end="")

    elif a == 2:
        b = int(input("Enter 1 for food and 2 for exercise\n"))
        if b == 1:
            with open("Kein_food.txt") as op:
                for i in op:
                    print(i, end="")
        elif b == 2:
            with open("Kein_exercise.txt") as op:
                for i in op:
                    print(i, end="")

    elif a == 3:
        b = int(input("Enter 1 for food and 2 for exercise\n"))
        if b == 1:
            with open("Chris_food.txt") as op:
                for i in op:
                    print(i, end="")
        elif b == 2:
            with open("Chris_exercise.txt") as op:
                for i in op:
                    print(i, end="")

    else:
        print("Please Enter a valid input :- 1(Daniel), 2(Kein), 3(Chris)\n")


print("Health Management System")

while (True):
    a = int(input("Press 1 for log and 2 for retrieve\n"))
    if a == 1:
        b = int(input("Enter 1(Daniel), 2(Kein), 3(Chris)\n"))
        take(b)
    elif a == 2:
        b = int(input("Enter 1(Daniel), 2(Kein), 3(Chris)\n"))
        retrieve(b)
