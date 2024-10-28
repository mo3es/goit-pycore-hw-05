import re

"""
    This programm parses given text and return the sum of finded in this text numbers.
    It provides by using function sum_profit, that iterate by numbers and calculate their sum.
    For iterating, uses function generator_numbers, that splits given text by ' ' as a separator and checks result on matching with real-number pattern using re.match function
"""


def generator_numbers(text: str) -> float:

    inword = text.split()
    for word in inword:
        if re.match(r"\d+(?:\.\d+)?", word.strip()):
            yield float(word)


def sum_profit(text: str, generator_numbers: callable) -> float:
    sum = 0
    for number in generator_numbers(text):
        sum += number
    return sum


def main():
    text = input("Input text:  ")
    total_income = sum_profit(text, generator_numbers)
    print((f"Загальний дохід: {total_income}"))


if __name__ == "__main__":
    main()
