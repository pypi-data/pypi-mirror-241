a = 2
b = 3


def linear_equation(x):
    """
    a linear equation that takes x and return ax+b.

    :param x: input of the linear equation
    :type x: int

    :return: the value of the linear equation for x
    :rtype: int

    """
    return a * x + b


def main():
    y = linear_equation(2)
    print(y)


if __name__ == "__main__":
    main()
