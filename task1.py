"""
    1.caching_fibonacci function recursively calculate n-position fibonacci number by using inner fibonacci function and return it;
    2.fibonacci function checks 3 predefined cases: case n <= 0 - return 0 as a result; case n == 1 - return 1 as a result and case n was calculated previously - return n as a result that was saved in dictionary from previouse calculations
    3. main function - utilitary function to start and test caching_fibonacci function by user input
"""


def caching_fibonacci(n: int):

    cache = dict()

    def fibonacci(n: int):

        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci(n)


def main():

    n = int(input("Input n: "))
    print(caching_fibonacci(n))


if __name__ == "__main__":
    main()
