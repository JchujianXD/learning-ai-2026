# Ask user for their name remove whitespace from str and capitalize user's name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {name}")
feat: 完成CS50P第0周练习
