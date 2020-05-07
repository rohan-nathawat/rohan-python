# Program takes user inputs for the length and width of 
# a rectangle and prints its area and perimeter.
# To take user input: Run => Run Without Debugging
# =====================================================

# Enter length of the rectangle in feet
strLength = input("Enter the rectangle length in feet: ")
strWidth = input("Enter the rectangle width in feet: ")

# Convert length and width to float from string
rectLength = float(strLength)
rectWidth = float(strWidth)

# Compute and print area
area = rectLength * rectWidth
print("The area of rectangle is ", area, " square feet.")

# Compute and print perimeter
perimeter = 2* (rectLength + rectWidth)
print("The perimeter of rectangle is ", perimeter, 
" feet.")
