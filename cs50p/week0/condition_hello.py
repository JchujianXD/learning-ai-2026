def main():
    hello()
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()
feat: 完成CS50P第0周练习
