print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer=input("what does HDD stand for ?")
if answer.lower()=="hard disk drive":
    print('Correct !')
    score += 1
else:
    print("Incorrect")
answer =input("what does SSD Stand for ?")
if answer.lower()=="solid state drive":
    print('correct')
    score += 1
else:
    print("Incorrect")
answer=input("what does DPI stand for ? ")
if answer.lower()=="dot per inches":
    print('Correct')
    score += 1
else:
    print("Icorrect")
answer=input("what does http stand for ? ")
if answer.lower()== "hyper text terminal protocol":
    print('Correct')
    score += 1
else:
    print("Wrong one")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 8) * 100) + "%.")