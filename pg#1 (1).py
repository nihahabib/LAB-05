print('Rushan Rafiq')
print('18b-087-CS')
print('Lab No#5')
print('Programming Exercise#1')
def area():
    import math
    radius = eval(input('Enter value of radius in metres(m)= ' ))
    height = eval(input('Enter value for height in metres(m)= '))
    area = (2*math.pi*radius*height) + (2*math.pi*radius**2)
    print('The area of the cylinder is {0:{1}f}cm\u00b2'.format(area,height))
def volume():
    import math
    radius2= eval(input('Enter value of radius for calculating volume in metres(m)= '))
    height2= eval(input('Enter value of height for calculating volume in metres(m)= '))
    volume = (math.pi*radius2**2*height2)
    print("The volume of the cylinder is {0:{1}f}cm\u00b3".format(volume,height2))
