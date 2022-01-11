i = 0
while i < 3:
    print(i)
    i += 1

print()

while True:
    prompt = "What is your name? "
    # print(prompt, end='')
    user_name = input(prompt)
    if user_name.strip() == 'q':
        break   # exit loop
    if user_name.strip() == '':
        print("Please enter a name")
        continue
    print("Hello,", user_name)

