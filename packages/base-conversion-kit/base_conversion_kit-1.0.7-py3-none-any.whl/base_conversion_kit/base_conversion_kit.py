#
def convert_to_base_n(decimal_number, to_base):
    """
    :param decimal_number: int:  the decimal number that you want to convert to another base
    :param to_base: int: the base you want to convert this number to
    :return: string: Converted number to another base
    It is a helper function to convert a decimal number to another base
    """
    if decimal_number == 0:
        return "0"

    result = ""
    while decimal_number > 0:
        remainder = decimal_number % to_base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        decimal_number //= to_base

    return result


def convert_base(number, from_base, to_base):
    """
    :param number: string: the number you want to convert to another base
    :param from_base: int: the base you want to convert th number from
    :param to_base: int: the base you want to convert the number to
    :return: string: the number converted to the required base
    """
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        raise ValueError("Base must be between 2 and 36 inclusive.")
    # Convert the number to base 10
    decimal_number = int(str(number), from_base)

    # Convert the decimal number to the desired base
    result = convert_to_base_n(decimal_number, to_base)

    return result


# function to add 2 numbers of the same base
def add_numbers(a, b, base):
    """
    :param a: string: first number to add
    :param b: string: second number to add
    :param base: int: the base the numbers are in
    :return: string: the result in the required base
    """
    # Convert the numbers to base 10
    decimal_a = int(str(a), base)
    decimal_b = int(str(b), base)

    # Add the decimal numbers
    result = decimal_a + decimal_b

    # Convert the result back to the original base
    result_in_base = convert_to_base_n(result, base)

    return result_in_base


# function to subtract 2 numbers on the same base
def subtract_numbers(a, b, base):
    """
    :param a: string: first number to add
    :param b: string: second number to add
    :param base: int: the base the numbers are in
    :return: string: the result in the required base
    """
    # Convert the numbers to base 10
    decimal_a = int(str(a), base)
    decimal_b = int(str(b), base)

    # Ensure a is greater than or equal to b to avoid negative results
    if decimal_a < decimal_b:
        raise ValueError("Subtraction would result in a negative number.")

    # Subtract the decimal numbers
    result = decimal_a - decimal_b

    # Convert the result back to the original base
    result_in_base = convert_to_base_n(result, base)

    return result_in_base


def multiply_numbers(num1, num2, base):
    """
    :param num2: string: first number to add
    :param num1: string: second number to add
    :param base: int: the base the numbers are in
    :return: string: the result in the required base
    """
    # Convert the numbers to integers in the specified base
    int_num1 = int(num1, base)
    int_num2 = int(num2, base)

    # Perform multiplication
    result = int_num1 * int_num2

    # Convert the result to the original base
    result_str = convert_to_base_n(result, base)

    return result_str
