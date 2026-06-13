# calculator.py
def add(a, b):
    return a + b

# NEW CODE HERE
def subtract(a, b):
    return a - b
# END NEW CODE

# NEW CODE HERE
def multiply(a, b):
    return a * b
# END NEW CODE

if __name__ == "__main__":
    result = add(5, 3)
    print(f"The result of addition is: {result}")
    # NEW CODE HERE
    result_sub = subtract(10, 4)
    print(f"The result of subtraction is: {result_sub}")
    # NEW CODE HERE
    result_mul = multiply(6, 7)
    print(f"The result of multiplication is: {result_mul}")