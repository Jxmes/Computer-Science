import time

t = 0
while 0 < 1:
    time.sleep(1)
    t = t + 1

name = input("Welcome! What is Your Name? ")
answer = ""
score = 0
one = "17*3"
two = "25/5"
three = "70+50"
four = "3*5"
five = "(10+10)/2"
six = "8*6"
seven = "(7+5)*2"
eight = "(14+9)*3"
nine = "5+10+(6*3)"
ten = "2+2"

time.sleep(1)

print("Welcome To The Maths Quiz",name,)

time.sleep(1)

print("Question 1:\n What is",one,"?")

answer = int(input( ))

if answer == 51:
    print("Correct!")
    score = score+1
else:
    print("Wrong!")

time.sleep(1)

print("Question 2:\n What is",two,"?")

answer = int(input( ))

if answer == 5:
    print("Correct!")
    score = score+1
else:
    print("Wrong!")

time.sleep(1)    

print("Question 3:\n What is",three,"?")

answer = int(input( ))

if answer == 120:
    print("Correct!")
    score = score+1
else:
    print("Wrong!")

time.sleep(1)    

print("Question 4:\n What is",four,"?")

answer = int(input( ))

if answer == 15:
    print("Correct!")
    score = score+1
else:
    print("Wrong!")
    
time.sleep(1)

print("Question 5:\n What is",five,"?")

answer = int(input( ))

if answer == 10:
    print("Correct!")
    score = score+1
else:
    print("Wrong!")     

time.sleep(1)

print("Question 6:\n What is",six,"?")

answer = int(input( ))

if answer == 48:
    print("Correct!")
    score = score+1
else:
    print("Wrong!")

time.sleep(1)

print("Question 7:\n What is",seven,"?")

answer = int(input( ))

if answer == 24:
    print("Correct!")
    score = score+1
else:
    print("Wrong!")

time.sleep(1)

print("Question 8:\n What is",eight,"?")

answer = int(input( ))

if answer == 69:
    print("Correct!")
    score = score+1
else:
    print("Wrong!")      

time.sleep(1)

print("Question 9:\n What is",nine,"?")

answer = int(input( ))

if answer == 33:
    print("Correct!")
    score = score+1
else:
    print("Wrong!")

time.sleep(1)

print("Question 10:\n What is",ten,"?")

answer = int(input( ))

if answer == 4:
    print("Correct!")
    score = score+1
else:
    print("Wrong!")

time.sleep(2)

print("Congratulations",name, "Your Score is",score,)

time.sleep(5)
    
