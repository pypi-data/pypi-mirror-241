from setuptools import setup, find_packages

# Read the content of README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='base_conversion_kit',
    version='1.0.7',

    author="porfanid",
    author_email='pavlos@orfanidis.net.gr',

    url='https://github.com/porfanid/base-conversion-kit',
    homepage='https://base-conversion-kit.readthedocs.io/',

    packages=find_packages(),
    install_requires=[
        'markdown'
    ],
    python_requires='>=3.6',
    project_urls={
        'Funding': 'https://ko-fi.com/porfanid',
        'Source': 'https://github.com/porfanid/base-conversion-kit',
        'Documentation': 'https://base-conversion-kit.readthedocs.io/',
        'Tracker': "https://github.com/porfanid/base-conversion-kit/issues",
        'Say Thanks!': 'https://saythanks.io/to/porfanid',
    },
    description='Perform operations with numbers in different bases',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='base, conversion, kit, base, convert, numbers, add, multiply, subtract, Number Converter, Base Conversion, Numeric Operations, Number System Converter, Decimal to Binary, Decimal to Hexadecimal, Base Conversion Tool, Number Base Calculator, Binary Math Operations, Hexadecimal Arithmetic, Binary Converter, Number Base Converter, Base Conversion App, Numeric Base Operations, Decimal Arithmetic, Hex Converter, Number Base Transform, Number Base Manipulation, Binary Subtraction, Decimal Multiplication, Base Conversion Utility, Numeric Base Transformation, Binary Calculator, Number System Manipulation, Hexadecimal Calculator, Numeric Base Math, Base Conversion Helper, Decimal to Octal, Numeric Base Conversion App, Base Arithmetic Operations'
)
