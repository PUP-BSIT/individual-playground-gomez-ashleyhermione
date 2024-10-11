# Program to determine the quadrant of a coordinate

# Take the x and y coordinates from the user
x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

# Check which quadrant the point belongs to
if x > 0 and y > 0:
    print("The coordinate is in the first quadrant.")
elif x < 0 and y > 0:
    print("The coordinate is in the second quadrant.")
elif x < 0 and y < 0:
    print("The coordinate is in the third quadrant.")
elif x > 0 and y < 0:
    print("The coordinate is in the fourth quadrant.")
elif x == 0 and y == 0:
    print("The coordinate is at the origin.")
else:
    print("The coordinate is on the x-axis or y-axis.")
