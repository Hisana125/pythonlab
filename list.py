nums=input("Enter integers separated by space:").split()
result=['over' if int(x)>100 else int(x) for x in nums]
print(result)
