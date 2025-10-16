colors=input("Enter comma-separated color names:").split(',')
colors=[color.strip() for color in colors]
print("First color:",colors[0])
print("Last color:",colors[-1])
