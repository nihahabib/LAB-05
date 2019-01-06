print('Rushan Rafiq')
print('18b-087-CS')
print('Practise Problem no 3')
def arithmetic_sq():
    n = int(input("Please enter the number of the term you want to find: "))
    a= int(input("Please enter the first term: "))
    d= int(input("Please enter the common difference: "))
    an = a+((n-1)*d)
    print("The",str(n),"th term in the given sequence is: ",str(an))
    user=input("\nDo you want to find another term (Press 'yes' to continue, 'exit' to quit): ")
    while user=='yes':
        arithmetic_sq()
    else:
        print("Okay,Thanks...!")
