def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))


main()


def square(n):
    return n * n  # 或 n**2 或 pow(n, 2)
