start=int(input("Enter start of range:"))
end=int(input("Enter end of range:"))
result=[]
for n in range(start,end+1):
    sqrt=int(n**0.5)
    if sqrt*sqrt==n:
        if all(int(digit)%2==0 for digit in str(n)):
            result.append(n)
print("Four-digit even-digit perfect squares:",result)
