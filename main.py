import random

print("Totally Random One-Million-to-One")

attempt = 1
randomNumber = random.randint(1, 100000)
print(randomNumber)
while True:
  guessNumber = int(input("pick a number between 1 and 100000: "))

  if guessNumber < randomNumber:
    print("too low")
    attempt += 1
  elif guessNumber > randomNumber:
    print("too high")
    attempt += 1
    continue 
  elif guessNumber == randomNumber:
    print("Awesome. Correct number! 🥳")
    break
    exit()
  else:
    print("number is not in range")
print("it took you", attempt, "attempt(s) to get the correct answer.")