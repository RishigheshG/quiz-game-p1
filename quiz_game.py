print("Welcome to my quiz game!")
score = 0

playing = input("Do you want to play? ").lower()
if playing != "yes":
  quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does FPS stand for? ").lower()
if answer == "frames per second":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

  print("You got " + str(score) + " questions correct!")
  print("Hope you enjoyed the game!")
