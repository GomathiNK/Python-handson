class multiplefunc():
    
    def Subfields():
        print("Sub-fields in AI are:")
        lists=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        for temp in lists:
            print(temp)

    def Oddeven():
        num=int(input("Enter a number"))
        if((num%2)==0):
            print(num,"is Even number")
            temp="Even number"
        else:
            print(num,"is Odd number")
            temp="Even number"
        return temp 

   
    def Eligible():
        Gender=input("your Gender")
        Age=int(input("Your Age"))
        if(Gender=="Male" and Age>=21):
            print("Elegible")
            temp="Elegible"
        elif(Gender=="Female" and Age>=18):
            print("Elegible")
            temp="Elegible"
        else:
            print("Not Elegible")
            temp="Not Elegible"
        return temp

    def percentage(Sub1,Sub2,Sub3,Sub4,Sub5):
        print("Subject1=",Sub1)
        print("Subject2=",Sub2)
        print("Subject3=",Sub3)
        print("Subject4=",Sub4)
        print("Subject5=",Sub5)
        Tot=Sub1+Sub2+Sub3+Sub4+Sub5
        Per=Tot/5
        print("Total:",Tot)
        temp="Tot"
        print("Percentage:",Per)
        temp="Percentage"
        return temp

    def triangle():
        H=int(input("Height:"))
        B=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        Area=(H*B)/2
        print("Area of Triange:", Area)
        H1=int(input("Height1:"))
        H2=int(input("Height2"))
        B1=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter=H1+H2+B1
        print("Perimeter of Triangle:",perimeter)