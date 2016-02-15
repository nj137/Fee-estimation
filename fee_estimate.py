#Program to estimate the fees for a course

print "Fees to be paid:"

#List of fees to be paid
fees=['application fees','exam fees']

#Exam fee structure
exam_fees={'Nationality':['Indian','Foreign','NRI','SAARC'],'Courses':['Ayurveda','Dental','Medical'],'Level':['UG','UG-Diploma','PG']}

#Application fee structure
application_fees={'Nationality':['Indian','Foreign'],'Courses':['Ayurveda','Dental','Medical'],'Level':['UG','UG-Diploma','PG']}

print "1."+fees[0]+"\n"+"2."+fees[1]

#select fees to be paid
select=int(raw_input("Select the type:"))

#j - initialization variable used for printing
j=0
if select == 2:

  #Exam fees
  #select nationality and print the choices
  
    for i in exam_fees['Nationality']:
        j=j+1
        print str(j)+"."+str(i)
    nation=int(raw_input("Select the type:"))
    j=0
    
  #select course and print the choices
    for i in exam_fees['Courses']:
        j=j+1
        print str(j)+"."+str(i)
    j=0
    
  #select level and print the choices
    course=int(raw_input("Select:"))
    for i in exam_fees['Level']:
        j=j+1
        print str(j)+"."+str(i)
    level=int(raw_input("Select the type:"))
    if nation == 1 :
        amount=400
    elif nation == 2:
        amount=100
    elif nation == 3:
        amount=600
    else:
        amount=600
    print "Exam fees to be paid:"+str(amount)
    
elif select == 1:

  #Application fees
  #select nationality and print the choices
  
    for i in application_fees['Nationality']:
        j=j+1
        print str(j)+"."+str(i)
    nation=int(raw_input("Select the type:"))
    j=0
    if nation == 1:
      #Indian
      #select course and print the choices
        for i in exam_fees['Courses']
          j=j+1
          print str(j)+"."+str(i)
          
        course=int(raw_input("Select:"))
        j=0
      #select level and print the choices
        for i in exam_fees['Level']:
          j=j+1
          print str(j)+"."+str(i)
          
        level=int(raw_input("Select the type:"))
        if level == 1:
          amount=200
        elif level == 2:
           amount=300
        else:
           amount=500
    else:
    
      #Foreign
      #select course and print the choices
      
        for i in exam_fees['Courses']:
          j=j+1
          print str(j)+"."+str(i)
        course=int(raw_input("Select:"))
        j=0
        
      #select level and print the choices
        for i in exam_fees['Level']:
          j=j+1
          print str(j)+"."+str(i)
        level=int(raw_input("Select the type:"))
        if level == 1:
          amount=400
        elif level == 2:
           amount=400
        else:
           amount=700
           
    print "Application fees to be paid is:"+str(amount)
else:

    #Invalid choice
    #Start selection again
    
    print "Invalid choice made.Start selection again!"
      
    


