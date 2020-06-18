import random
wining= random.randint(1,100)

print("enter a guess number")

for i in range(1,100):
    n=int(input())
    if n==wining:
        print(f"you are win, and you guessed this numer {i} times")
        break
    elif n<wining:
        print("your guess is low")
    else:
        print("your guess  is high") 
    print(" again , guess  and the number")
    i+=1

