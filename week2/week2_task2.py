s1 = "Python903"

digits = []

for character in s1:
    if character.isdigit():
        digits.append(int(character))

total = sum(digits)
average = total / len(digits)

print("Sum of the digits in the given string:", total)
print("Average of the digits in the given string:", average)