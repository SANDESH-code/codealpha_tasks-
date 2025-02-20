def fibonacci_generator():
    a, b = 0, 1  # Start with first two numbers
    while True:  # Repeat forever
        yield a  # Give the number
        a, b = b, a + b  # Get next number

# Use the function
fib = fibonacci_generator()  # Create generator
for _ in range(10):  # Repeat 10 times
    print(next(fib), end=" ")  # Show number
