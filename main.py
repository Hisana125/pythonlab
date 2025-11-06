import Armstrong
low=int(input("Enter lower limit:"))
high=int(input("Enter upper limit:"))
print(f"Armstrong numbers between {low} and {high} are:")
for num in range(low,high+1):
    if Armstrong.is_armstrong(num):
        print(num)
