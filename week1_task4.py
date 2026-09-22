random_number = int(input("Type a random number:"))

factorial_number = 1

for i in range(1, random_number+1):
    factorial_number = factorial_number * i

print("Factorial of", random_number, "is", factorial_number)