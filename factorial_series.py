def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
        return f
n=int(input("Enter number of terms:"))
series_sum=0
for i in range(1,n+1):
    term=(i**3)/fact(i)
    series_sum+=term
print("Sum of the series:",series_sum)
