# Compute and display area and circumference of a circle
# Format the output as a floating point number with two
# digits to the right of decimal point.
#=======================================================

# Specify the value of PI
PI = 3.14

# Take user input for radius
radius = float(input("Enter radius of circle: "))

# Compute and print area
area = PI * radius * radius
print("Area of circle is %0.2f" %area)

# Compute and print circumference
circumferenc = 2 * PI * radius
print("Circumference of circle is %0.2f" %circumferenc)