user_input = input('type here: ')
for letter in user_input:
    if letter.lower() in [ 'a', 'e', 'i', 'o', 'u']:
        user_input = user_input.replace(letter, '')
print(user_input)