def main():
    print_column(3)
    print_row(4)
    print_square(3)


def print_column(height):
    print("#\n" * height, end="")


def print_row(width):
    print("#\n" * width)


def print_square(size):
    for i in range(size):
        print("#" * size)

        # for j in range(size):
        #     print("#", end="")
        # print()

        # 或定义一个函数print_row(width):print("#"*width)


main()
