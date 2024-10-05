# Exercise 1:

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# max_value = a

# if b > max_value:
#     max_value = b

# if c > max_value:
#     max_value = c

# print("Maximum Value:", max_value)


# Exercise 2:

# positive_int = int(input("Enter a positive integer: "))

# product = 1
# i = 1

# while i <= positive_int:
#     if i % 2 != 0:
#         product *= i
#     i += 1

# if product > 100:
#     print("Multiplication exceeded")
# else:
#     print("Final Product:", product)
    
    
# Exercise 3:

# scores = []
# count = 0
# while True:
#     score = float(input("Please enter score: "))
#     if score == -1:
#         if count == 0:
#             print("No scores were entered.")
#         else:
#             average = sum(scores) / count
#             print("The score average is:", average)
#     else:
#         scores += [score]
#         count += 1


# Exercise 4:

# num = int(input("Enter a four-digit number: "))

# a = num // 1000
# b = (num // 100) % 10
# c = (num // 10) % 10
# d = num % 10

# if a + b == c + d:
#     print("F")
# else:
#     print("U")