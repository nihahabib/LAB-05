print('Rushan Rafiq')
print('18b-087-CS')
print('Practise Problem no 10')
print("Table for generating`values for trigonometric functions")
import math
def table(range1,range2,step):
    sin=[]
    cos=[]
    tan=[]
    degrees_lst=[]
    for degrees in range(range1,range2+1,step):
        sinx = math.sin(math.radians(degrees))
        sinx = float("{0:.4f}".format(sinx))
        sin.append(sinx)
        cosx = math.cos(math.radians(degrees))
        cosx = float("{0:.4f}".format(cosx))
        cos.append(cosx)
        tanx = math.tan(math.radians(degrees))
        tanx = float("{0:.4f}".format(tanx))
        tan.append(tanx)
        degrees_lst.append(degrees)
    print('Degree: %-15s'%(degrees_lst))
    print('Sinx : %-15s' % (sin))
    print('Cosx : %-15s' % (cos))
    print('Tanx : %-15s' % (tan))
    
    
range1 = int(input("Please enter starting value in degrees: "))
range2 = int(input("Please enter ending value in degrees : "))        
step   = int(input("Please enter the step between these values: "))

table(range1,range2,step)
