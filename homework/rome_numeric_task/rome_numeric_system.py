def roman_to_arab(roman: str) -> int:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    previous_number = 0
    almost_arab = [values[i] for i in list(roman)][::-1]

    for char in almost_arab:
        if previous_number == 0:
            previous_number = char
            result += previous_number
            continue
        elif previous_number > char:
            result -= char
            previous_number = char
            continue
        elif previous_number <= char:
            result += char
            previous_number = char
            continue
        else:
            print('Unknown error')
            break

    return result

print(roman_to_arab('MCMLXXXIV'))
# 1984

print(roman_to_arab('MCCXXXIV'))
# 1234

print(roman_to_arab('MCMXC'))
# 1990
