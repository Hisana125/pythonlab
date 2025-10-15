str1=input("Enter first string:")
str2=input("Enter second string:")
if len(str1)<2 or len(str2)<2:
    print("Both strings must have at least 2 characters.")
else:
    new_str1=str1[0]+str2[1]+str1[2:]
    new_str2=str2[0]+str1[1]+str2[2:]
    str3=new_str1+" "+new_str2
    print("Result:",str3)

