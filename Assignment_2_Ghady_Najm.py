# Exercise 1:

# def calculateFactorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# integer = int(input("Enter a non-negative integer: "))

# print(calculateFactorial(integer))



# Exercise 2:

# def findDivisors():
#     number = int(input("Enter a number: "))
#     divisors = [i for i in range(1, number + 1) if number % i == 0]
#     return divisors

# print(findDivisors())



# Exercise 3:

# def reverseString():
#     userInput = input("Enter a string: ")
#     reversed_string = ""
#     for i in range(len(userInput) - 1, -1, -1):
#         reversed_string += userInput[i]
#     return reversed_string


# print(reverseString())



# Exercise 4:

# def sortEvenNumber():
#     UserInput = input("Enter a list of integers: ")
#     num = [int(x) for x in UserInput.split()]
#     evenNumbers = []
#     for numbers in num:
#         if numbers % 2 == 0:
#             evenNumbers.append(numbers)
#     return evenNumbers


# print(sortEvenNumber())



# Exercise 5:

# def check_password_strength():
#     userInput = input("Enter a password: ")
#     if len(userInput) < 8:
#         return "Weak password"
#     hasUppercase = any(char.isupper() for char in userInput)
#     hasLowercase = any(char.islower() for char in userInput)
#     hasDigit = any(char.isdigit() for char in userInput)
#     hasSpecialChar = any(char in "#?!" for char in userInput)
#     if hasUppercase and hasLowercase and hasDigit and hasSpecialChar:
#         return "Strong password"
#     else:
#         return "Weak password"

# print(check_password_strength())



# Exercise 6:

# def isValid_IPv4_address():
#     userInput = input("Enter an IPv4 address: ")
#     parts = userInput.split(".")
#     if len(parts) != 4:
#         return "Invalid IPv4 address"
#     for part in parts:
#         if not part.isdigit():
#             return "Invalid IPv4 address"
#         if int(part) > 255 or int(part) < 0:
#             return "Invalid IPv4 address"
#         if len(part) > 1 and part[0] == "0":
#             return "Invalid IPv4 address"
#     return "Valid IPv4 address"

# print(isValid_IPv4_address())
