#creating a mobile bank app
age = int(input("please enter your age"))
if age ==18:
    print("you are eligble for this account")
elif age > 20:
    print("yes")
    country =input("please enter your country")
    if country =="Nigeria":
     print("you can sign up")
    
    elif country == "ghana":
        print("you have a grace")
elif age <=18:
        print("you can't sign up")



    
else:
    print("non of the above")


