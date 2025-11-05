def add_numbers(*args):
    total=0
    for num in args:
        total+=num
    return total
user_input=input("Enter integers separated by spaces:")
numbers=[int(x) for x in user_input.split()]
result=add_numbers(*numbers)
print("The sum is:",result)

