
############
#Exercise 1:
############

# def tuplesSum(tuple1, tuple2):
#     result = [0] * len(tuple1)
#     for i, elem in enumerate(tuple1):
#         result[i] += elem
#     for i, elem in enumerate(tuple2):
#         result[i] += elem
#     return tuple(result)


# def writeJSON(d, file):
#     with open(file, "w") as f:
#         f.write("{\n")
#         for key, value in d.items():
#             f.write(f'"{key}": {value}, \n')
#         f.write("}\n")


# def readJSON(filename):
#     with open(filename, 'r') as f:
#         jsonData = f.read()
#     jsonData = jsonData.replace('\n', '').replace(' ', '')
#     objects = jsonData[1:-1].split('},{')
#     dictionaries = {}
#     for obj in objects:
#         dictionary = {}
#         pairs = obj.split(',')
#         for pair in pairs:
#             if ':' in pair:
#                keyValue= pair.split(':', 1)
#                key = keyValue[0].strip().strip('"')  
#                value = keyValue[1].strip()
#             dictionaries[key] = value


#     return dictionaries



# def main():
#     while True:
#         print("1. Sum Tuples")
#         print("2. Export JSON")
#         print("3. Import JSON")
#         print("4. Exit")
#         choice = input("Enter a choice: ")

#         if choice == "1":
#             tuple1 = tuple(
#                 map(int, input("Enter tuple 1 (seperated by spaces): ").split())
#             )
#             tuple2 = tuple(
#                 map(int, input("Enter tuple 2 (seperated by spaces): ").split())
#             )
#             result = tuplesSum(tuple1, tuple2)
#             print("Result", result)

#         elif choice == "2":
#             d = {}
#             numOfItems = int(input("Enter the number of items in the dictionary: "))
#             for i in range(numOfItems):
#                 key = input(f"Enter key {i+1}: ")
#                 value = int(input(f"Enter value {i+1}: "))
#                 d[key] = value
#             file = input("Enter the file name: ")
#             writeJSON(d, file)
#             print("JSON File Exported Successfully!!!")

#         elif choice == "3":
#             file = input("Enter the file name: ")
#             dictionaries = readJSON(file)
#             print("Dictionaries Imported From JSON File: ")
#             for i, d in enumerate(dictionaries):
#                 print(f"Dictionary {i+1}: {d}")

#         elif choice == "4":
#             print("Exiting Program....")
#             break
#         else:
#             print("Invalid Choice! Please Try Again!")


# main()


############
#Exercise 2:
############


# def factorial(N):
#     result = 1
#     for i in range(1, N + 1):
#         result *= i
#     return result


# def log(N):
#     result = 0
#     while N > 1:
#         N /= 2
#         result += 1
#     return result


# def a(N):
#     return 1 / 6 * N + 8000 * N**3 + 24


# def b(N):
#     return 1 / 6 * N**3


# def c(N):
#     1 / 6 * factorial(N) + 200 * N**4


# def d(N):
#     return N * log(N) + 1000


# def e(N):
#     return log(N) + N


# def f(N):
#     return 1 / 2 * N * (N - 1)


# def g(N):
#     return N**2 + 200 * N ** log(N * 2) + 3 * N + 9000


# def h(N):
#     return factorial(N) + 3 * N + 2 * N + N**3 + N**2


# def main():
#     N = 10

#     print("a(N) =", a(N))
#     print("b(N) =", b(N))
#     print("c(N) =", c(N))
#     print("d(N) =", d(N))
#     print("e(N) =", e(N))
#     print("f(N) =", f(N))
#     print("g(N) =", g(N))
#     print("h(N) =", h(N))

# main()