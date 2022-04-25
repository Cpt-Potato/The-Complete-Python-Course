def divide(dividend: int | float, divisor: int | float):
    if divisor == 0:
        raise ValueError("The divisor cannot be zero.")
    return dividend / divisor


def multiply(*args: int | float):
    if len(args) == 0:
        raise ValueError("At least one error to multiply must be passed.")

    total = 1
    for arg in args:
        total *= arg

    return total
