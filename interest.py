def get_interest_rate(age):
    """Return interest rate based on age."""
    if age>=60:
        return 12
    else:
        return 10
def calculate_simple_interest(principal,time,age):
    """Calculate and return simple interest."""
    rate=get_interest_rate(age)
    interest=(principal*rate*time)/100
    return interest
P=float(input("Enter principal amount:"))
T=float(input("Enter time(in years):"))
age=int(input("Enter age of customer:"))
SI=calculate_simple_interest(P,T,age)
print(f"\nSimple Interest={SI:.2f}")

