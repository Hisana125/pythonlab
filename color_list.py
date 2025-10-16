color_list1=input("Enter colors for list 1 (comma-separated):").split(',')
color_list2=input("Enter colors for list 2 (comma-separated):").split(',')
result=[color.strip() for color in color_list1 if color.strip() not in map(str.strip,color_list2)]
print("Colors in list1 not in list2:",result)
