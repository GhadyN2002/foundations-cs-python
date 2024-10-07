def count_digits(n):
    count = 0
    if n == 0:
        return 1
    elif n < 0:
        n = -n
    while n > 0:
        count += 1
        n = n // 10
    return count

def find_max(lst):
    max_val = 0
    for val in lst:
        if val > max_val:
            max_val = val
    return max_val

def count_tags(html, tag):
    count = 0
    while True:
        if html.find('<' + tag + '>') != -1:
            count += 1
            html = html.replace('<' + tag + '>', '', 1)
        if html.find('</' + tag + '>') != -1:
            count += 1
            html = html.replace('</' + tag + '>', '', 1)
        if html.find('<' + tag + '>') == -1 and html.find('</' + tag + '>') == -1:
            break
    return count

def main():
    html_code = """
<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>
"""

    while True:
        print("1. Count Digits")
        print("2. Find Max")
        print("3. Count Tags")
        print("4. Exit")
        choice = int(input("Enter a choice: "))

        if choice == 1:
            num = int(input("Enter an integer: "))
            print("Number of digits:", count_digits(num))
        elif choice == 2:
            lst = list(map(int, input("Enter a list of integers (separated by space): ").split()))
            print("Maximum value:", find_max(lst))
        elif choice == 3:
            tag = input("Enter a tag: ")
            print("Number of occurrences of the tag:", count_tags(html_code, tag))
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()