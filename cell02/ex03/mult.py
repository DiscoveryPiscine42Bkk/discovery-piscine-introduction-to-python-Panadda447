#mult.py
def multiply(a, b):
    return a * b
if  __name__ == "__main__":
    numA = float(input("Enter first number: "))
    numB = float(input("Enter second number: "))
    result = multiply(numA, numB)
    print(f"The result of multiplication is:{result}")
if result > 0:
    print("The result is positive")   
elif result < 0:
    print("The result is negative")   
else:
    print("The result is positive and negative")    
