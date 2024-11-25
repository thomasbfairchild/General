
print("Welcome to my Marine Corps quiz!")

playing = input("Would you like to play? " )
score = 0
if playing.lower() != "yes":
    quit()
else:
    print("Okay! Let's get started! ")

question1 = (input("What is the Marine Corps motto? "))
if question1.lower() == "semper fidelis":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question2 = (input("What year was the Marine Corps founded? "))
if question2 == "1775":
    print("Correct!")
    score += 1
else:
     print("Incorrect!")

question3 = (input("What is the Marine Corps emblem? "))
if question3.lower() == "eagle, globe and anchor" or 'ega':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question4 = (input("Where was the Marine Corps founded? "))
if question4.lower() == "tunn tavern":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question5 = (input("Who is the most decorated Marine? "))
if question5.lower() == "chesty puller":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " out of 5 correct!")
print("Your score is " + str((score / 5) * 100) + "%!")
