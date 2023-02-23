import random
num = int(random.randint(1,100))
print(num)
print("Enter a number between 1 and 100 : ")
guess_count = int(1)
guess = int(input("Guess a number! "))
greater_Stute = abs(num + 5)
less_Stute = abs(num - 5)
while guess != num:
    guess_count = guess_count + 1    
    if guess > num < greater_Stute:
        print("Farther!")
    if guess < num > less_Stute:
        print("Closer!")    
    if guess <= 0:
        print("Out of Bounds. Try again.")
    if guess > 100:
        print("Out of Bounds. Try again.")
    guess = int(input("Guess again: "))
if guess == num:
    print("You've won! It took you %d tries, but you got it. " % (guess_count))
