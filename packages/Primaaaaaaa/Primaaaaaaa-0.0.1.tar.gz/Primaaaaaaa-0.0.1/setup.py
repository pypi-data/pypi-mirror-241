from setuptools import setup, find_packages

setup(
    name='Primaaaaaaa',
    version='0.0.1',
    author='Allyaaa',
    author_email='maulidallya06@gmail.com',
    description='A Python package to check if a number is prime',
    long_description='''
    Prima is a simple Python package that provides a class for checking whether a given number is prime.

    Usage:
    ```
    from Prima import Prima

    number = 17
    primality_checker = Prima(number)

    if primality_checker.is_prima():
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
    ```

    The package uses a basic algorithm to determine primality by checking divisibility up to the square root of the given number.

    For more information, please visit the GitHub repository: https://github.com/yourusername/Prima
    ''',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
