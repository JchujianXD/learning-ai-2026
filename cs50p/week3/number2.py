def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass  # 跳过 实际可用print("x is not an integer")作为提醒


main()
