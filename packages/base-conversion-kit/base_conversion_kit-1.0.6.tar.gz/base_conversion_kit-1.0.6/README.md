# Base Conversion Kit

[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/porfanid)

The Base Conversion Kit is a Python package designed to simplify number operations across different bases. Whether you're working with binary, octal, decimal, or hexadecimal numbers, this package provides convenient functions for conversions and basic arithmetic operations.

## Installation

You can install the Base Conversion Kit using `pip`:

```bash
pip install base-conversion-kit
```

## Usage

### Converting Numbers

The package offers a flexible function for converting numbers from any base to another:

```python
from base_conversion_kit import convert_to_base_n, convert_base

# Convert a decimal number to binary
binary_result = convert_to_base_n(42, 2)
print(f"Binary representation: {binary_result}")

# Convert a hexadecimal number to octal
octal_result = convert_base("1A", 8, 16)
print(f"Octal representation: {octal_result}")
```

### Performing Arithmetic Operations

Performing arithmetic operations on numbers from different bases is seamless:

```python
from base_conversion_kit import multiply_numbers, add_numbers, subtract_numbers

# Multiply two binary numbers
result_binary = multiply_numbers("101", "110", 2)
print(f"Binary multiplication result: {result_binary}")

# Add two decimal numbers
result_addition = add_numbers(15, 7, 10)
print(f"Decimal addition result: {result_addition}")

# Subtract two hexadecimal numbers
result_subtraction = subtract_numbers("1A", "B", 16)
print(f"Hexadecimal subtraction result: {result_subtraction}")
```

## Examples

### Example 1: Adding Binary Numbers

```python
from base_conversion_kit import add_numbers

result = add_numbers("101", "110", 2)
print(f"Binary addition result: {result}")
```

### Example 2: Converting and Adding

```python
from base_conversion_kit import convert_to_base_n, add_numbers

# Convert decimal numbers to binary and add
binary_sum = add_numbers(
    convert_to_base_n(10, 2),
    convert_to_base_n(5, 2),
    2
)
print(f"Binary sum: {binary_sum}")
```

# Read The Docs

More info can be found [here](https://base-conversion-kit.readthedocs.io)

## Contributing

Feel free to contribute to the development of the Base Conversion Kit. If you encounter issues, have suggestions, or want to add features, please submit a pull request or open an issue on the [GitHub repository](https://github.com/porfanid/base-conversion-kit).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/porfanid/base-conversion-kit/blob/master/LICENSE) file for details.