print("What is your name?")
user = input()
print("Hello",user)
print("Please write all of your answers to these questions in lower case letters")
print("Do you like pizza?")
user = input()
if user == "yes":
  print("Me too!")
  print("Pizza is my favourite food")
else:
  print("Your Strange")
  print("How do you not like pizza!")
  print("What do you like then?")
  user = input()
  if user == "pizza":
    print("But I thought you didnt like pizza")
    print("Anyway,")
  else:
    print("I like that too!")
print("How old are you?")
user = input()
print("So your",user)
print("Am I correct?")
user = input()
if user == "yes":
  print("Ok I was just checking")
else:
  print("So you were lying to me!")
  print("I am hurt")
print("Do you know any spanish?")
user = input()
if user == "yes":
  print("This is an easy question,")
  print("What does Hola mean?")
  user = input()
  if user == "hello":
    print("Correct!")
  else:
    print("Incorrect. The answer was hello")
  print("Question 2")
  print("What is three in Spanish?")
  user = input()
  if user == "tres":
    print("Correct!")
  else:
    print("Sorry, thats incorrect")
    print("The correct answer was tres")
  print("Ok Final Question")
  print("What is cat in Spanish?")
  user = input()
  if user == "gato":
    print("Correct!")
  else:
      print("Incorrect")
      print("The correct answer was gato")
else:
  print("Ok. Never mind")
print("Do you have a pet?")
user = input()
if user == "yes":
  print("What pet do you have?")
  user = input()
  if user == "spider":
    print("I hate spiders")
  else:
    print("A",user) 
    print("I love them!")
else:
  print("Animals are nice. You should get one")
print("Do you have a favourite sport?")
user = input()
if user == "yes":
  print("What is it?")
  user = input()
  if user == "football":
    print("I don't really like football")
    print("I find it quite boring")
  else:
    print("I like",user)
else:
  print("Ok")
  print("My favourite sport is tennis")
print("Anyway, should we leave it here?")
user = input()
if user == "yes":
  print("Thanks")
  print("Its just that the next user for this code is waiting")
  print("Its been nice talking to you,")
  print("Goodbye")
else:
  print("Well the next user is waiting so I need to speak to them")
  print("Do you understand?")
  user = input()
  if user == "yes":
    print("Thank you so much! I'm glad you understand")
    print("Its been nice talking to you")
    print("Goodbye!")
  else:
    print("Well I really need to go")
    print("Goodbye")
