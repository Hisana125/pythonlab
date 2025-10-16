nums=input("Enter comma-separated integers:").split(',')
nums=[int(n.strip()) for n in nums]
odd_nums=[n for n in nums if n%2!=0]
print("List after removing even numbers:",odd_nums)
