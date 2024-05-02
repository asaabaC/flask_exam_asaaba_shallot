import math

# Prompt the user to enter the values of X1, X2, Y1, and Y



def calculate_distance(X1, X2, Y1, Y2):
    d = math.sqrt((X1 - X2)**2 + (Y1 - Y2)**2)
    return d


X1 = float(input("Enter the value of X1: "))
X2 = float(input("Enter the value of X2: "))
Y1 = float(input("Enter the value of Y1: "))
Y2 = float(input("Enter the value of Y2: "))

# finding distance
distance = calculate_distance(X1, X2, Y1, Y2)


print("The distance d is:", distance)





# Allocating specific values to X1, X2, Y1, and Y2
X1 = 60
X2 = 30
Y1 = 160.5
Y2 = 97.7


d = math.sqrt((X1 - X2)**2 + (Y1 - Y2)**2)

print("The value of d is:", d)

