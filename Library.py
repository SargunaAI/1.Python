class multiplefunctions():
    def OddEven():
        a=int(input("Enter a number:"))
        if(a%2)==1:
            print(a,"is Odd number")
            Variable="a,is Odd number"
        else:
            print(a,"is Even Number")
            Variable=("a,is Even Number")
        return Variable
    
    def Eligibility():
        Gender=input("Your Gender:")
        Age=int(input("Your age :"))
        if(Age<21):
            print("NOT ELIGIBLE")
            Variable="NOT ELIGIBLE"
        else:
            print("ELIGIBLE")
            Variable="ELIGIBLE"
        Gender=input("Your Gender:")
        Age=int(input("Your age :"))
        if(Age<18):
            print("NOT ELIGIBLE")
            Variable="NOT ELIGIBLE"
        else:
            print("ELIGIBLE")
            Variable="ELIGIBLE"
        return Variable
    
    def Percentage():
        Subj1=int(input("Subject1:"))
        Subj2=int(input("Subject2:"))
        Subj3=int(input("Subject3:"))
        Subj4=int(input("Subject4:"))
        Subj5=int(input("Subject5:"))
        Add=(Subj1+Subj2+Subj3+Subj4+Subj5)
        Perc=((Add/500)*100)
        print("Total:",Add)
        Variable="Total:",Add
        print("Percentage=",Perc)
        Variable="Percentage=",Perc
        return Variable
    
    def triangle():
        Ht=int(input("Height:"))
        Br1=int(input("Breadth:"))
        AreaTri=((Ht*Br1)/2)
        print("Area formula: (Height*Breadth)/2")
        Variable="Area formula: (Height*Breadth)/2"
        print("Area of Triangle:",AreaTri)
        Variable="Area of Triangle:",AreaTri
        Ht1=int(input("Height1:"))
        Ht2=int(input("Height2:"))
        Br2=int(input("Breadth1:"))
        PeriTri=(Ht1+Ht2+Br2)
        print("Perimeter formula: Height1+Height2+Breadth")
        Variable="Perimeter formula: Height1+Height2+Breadth"
        print("Area of Perimeter:",PeriTri)
        Variable="Area of Perimeter:",PeriTri
        return Variable
    
    def BMI():
        BMI=int(input("Enter the BMI Index:"))
        if(BMI<=18.4):
            print("Under weight")
            variable="Under weight"
        elif(BMI<24.9):
            print("Normal")
            variable="Normal"
        elif(BMI<39.9):
            print("Very Over Weight")
            variable="Very Over Weight"
        else:
            print("Obese")
            variable="Obese"
        return variable

    def Agecategory():
        if(age<18):
            print("children")
            variable="Children"
        elif(age<35):
            print("Adult")
            variable="Adult"
        elif(age<59):
            print("Citizen")
            variable="Citizen"
        else:
            print("Senior citizen")
            variable="Senior citizen"
        return variable