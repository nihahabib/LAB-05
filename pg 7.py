print('Rushan Rafiq')
print('18b-087-CS')
print('Practise Problem no 7')
print ('Program For Projectile Motion')
import math

def projectile(initialvelocity,angle):
    gravity = 9.8
    Height = (initialvelocity**2)*((math.sin(angle))**2) / (2*gravity)
    TotalTime = 2*initialvelocity*math.sin(angle) / gravity
    Range = (initialvelocity**2)*math.sin((2*angle)) / gravity

    print("The Maximum height reached by the object is : {0:.1f}meters".format(Height))                                                                               
    print("The Total time taken by the object is       : {0:.1f}seconds".format(TotalTime))
    print("The Horizontal Range of the object is       : {0:.1f}meters".format(Range))

initialvelocity = float(input("Please enter the initial velocity of the object    : "))
angle= float(input("Please enter the angle of projection of the object : "))
angle = math.radians(angle)
projectile(initialvelocity,angle)
