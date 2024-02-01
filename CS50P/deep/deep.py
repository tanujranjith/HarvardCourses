answer=input("what is the answer to the great question of life, the universe and everything?")

if answer.strip() == "42":
    print("Yes")

elif answer.lower().strip() == "forty-two":
    print("Yes")
elif answer.lower().strip() == "forty two":
    print("Yes")

else:
    print("No")