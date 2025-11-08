def roman_to_int(roman: str) -> int:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Идём справа налево
    for symbol in reversed(roman):
        value = values[symbol]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total


# ======== Примеры ========

if __name__ == "__main__":
    examples = ["MCMLXXXIV", "MCCXXXIV", "MCMXC"]
    for r in examples:
        print(f"{r} → {roman_to_int(r)}")