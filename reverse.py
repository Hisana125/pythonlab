n=int(input("Enter a number:"))
rev=0
temp=n
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("Reverse of",temp,"is",rev)
