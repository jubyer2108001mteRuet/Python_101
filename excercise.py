wight=float(input("Weight: "))
unit=input("Enter unit k or lb: ")
if unit=='k':
    print("Wight in lb: "+str(wight*2.204622))

elif unit=='l':
    print("Wight in kg: "+str(wight/2.204622))
