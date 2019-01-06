print('Rushan Rafiq')
print('18b-087-CS')
print('Practise Problem no 6')

def first_law_of_motion():
    Vi= int(input('Enter the initial velocity of the body: '))
    a= int(input('Enter the accelaration of the body: '))
    t= int (input('Time taken by the body:' ))
    Vf= Vi + (a*t)
    print('The Final Velocity of the body is:',Vf, ' m/s')
def second_law_of_motion():
    Vi= eval(input('Enter the initial velocity of the body: '))
    a= eval(input('Enter the accelaration of the body: '))
    t= eval(input('Time taken by the body:' ))
    S =  Vi*t+ 1/2*(a*(t**2))
    print('The distance taken by the body is: ',str(S),'m')
def third_law_of_motion():
    vf = int(input('Enter the final velocity of the body: '))
    vi = int(input('Enter the initial velocity of the body: '))
    a2= (input("What does you want to find,Acceleration or distamce..?"))
    if a2== 'Acceleration':
        s= int(input("Enter the distance cover by body in metres(m):"))
        a= (vf**2-vi**2)/2*s
        print("The acceleration of the body at that time will be: ",a,' m/s²')
    else:
        a= int(input("Enter the accelaration of the body in m/s²:"))
        s= abs((vf**2-vi**2)/2*a)
        print('The distance covered by the body is:' , s, 'm')
