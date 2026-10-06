def convert_to_arabic(number):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    for i in range(len(number)):
        if i < len(number) - 1 and roman[number[i]] < roman[number[i + 1]]:
            result -= roman[number[i]]
        else:
            result += roman[number[i]]

    return result

def convert_to_roman(number):
    roman = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    result = ""
    for value in reversed(roman):
        while number >= value:
            result += roman[value]
            number -= value

    return result