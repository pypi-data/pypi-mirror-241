from setuptools import setup, find_packages

# Read the content of README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='base_conversion_kit',
    version='1.0.4',
    author="porfanid",
    author_email='pavlos@orfanidis.net.gr',

    packages=find_packages(),
    install_requires=[
        'markdown'
    ],
    python_requires='>=3.6',
    project_urls={
        'Funding': 'https://ko-fi.com/porfanid',
        'GitHub': 'https://github.com/porfanid/base-conversion-kit'
    },
    description='Perform operations with numbers in different bases',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='base, conversion, kit, base, convert, numbers, add, multiply, subtract, '
)
