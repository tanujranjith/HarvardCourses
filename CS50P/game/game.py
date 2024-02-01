import random
while True:
    try:
        level=int(input("Level:"))
        if level >= 1 and level <= 999999999:
            level=random.randint(1, 10)
            guess=int(input("Guess:"))
            try:
                if guess >= 1:
                    if guess < level:
                        print("too small!")
                    elif guess >level:
                        print("too large!")
                    elif guess == level:
                        print("just right!")
                    break
            except:
                continue
    except ValueError :
        pass