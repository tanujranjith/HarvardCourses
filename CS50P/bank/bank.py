answer = input("greetings ")
new_answer = answer.lower().strip()
if 'hello' in new_answer:
    print("$0")
elif 'h' == new_answer[0]:
    print("$20")
else:
    print("$100")