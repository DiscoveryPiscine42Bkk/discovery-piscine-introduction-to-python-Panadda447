#to25.py
number = int(input("Enter a number less than 25\n"))
if number > 25:
    print("Error")
else:
    while number <= 25:
        print(f"Inside the loop, variable is {number}")
        number += 1
