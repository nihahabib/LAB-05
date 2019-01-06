print('Rushan Rafiq')
print('18b-087-CS')
print('Practise Problem no 5')

def marksheet():
    name = input("Name: ")
    father_name = input("Father's name: ")
    subject ="Subject"
    marks = "Marks"
    subject_1 = input("Name of Subject: ")
    marks_1 = input("Total marks obtained in subject: ")
    subject_2 = input("Name of Subject: ")
    marks_2 = input("Total marks obtained in subject: ")
    subject_3 = input("Name of Subject: ")
    marks_3 = input("Total marks obtained in subject: ")
    subject_4 = input("Name of Subject: ")
    marks_4 = input("Total marks obtained in subject: ")
    subject_5 = input("Name of Subject: ")
    marks_5 = input("Total marks obtained in subject: ")

    print ("\n")
    print ("Name: %-15s" %(name))
    print ("Father's Name: %-15s" %(father_name))
    print ("%-15s %-15s" %(subject, marks))
    print ("%-15s %-15s" %(subject_1, marks_1))
    print ("%-15s %-15s" %(subject_2, marks_2))
    print ("%-15s %-15s" %(subject_3, marks_3))
    print ("%-15s %-15s" %(subject_4, marks_4))
    print ("%-15s %-15s" %(subject_5, marks_5))
