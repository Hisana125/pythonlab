def check_even_odd(n):
    """Return whether the number is even or odd."""
    if n%2==0:
        return "Even"
    else:
        return "Odd"
number=int(input("Enter a number:"))
result=check_even_odd(number)
print(f"The number {number} is {result}.")
