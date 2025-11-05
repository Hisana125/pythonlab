def fibonacci(num):
    """Return the nth Fibonacci number using Recursion."""
    if num<=1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)
n=int(input("Enter the number of terms:"))
print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i),end=" ")
