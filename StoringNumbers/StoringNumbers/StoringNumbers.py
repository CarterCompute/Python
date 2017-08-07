area = 0
height = 10
width = 20

#Calculate the area od a triangle
area = (width * height)/2

print("The area of the triangle would be", area)
#Print Decimal
print("The area of the triangle would be %d" % area)
#Print decimal with formatting fixed width(pushes alignment to right)
print("The area of the triangle would be %6d" % area)
#Print Float
print("The area of the triangle would be %f" % area)
#Print float with specific decimal place
print("The area of the triangle would be %.2f" % area, "\n")

#formatting {0:f} = placeholder for float number
print("The area of the triangle would be {0:f}".format(area))



###########################

