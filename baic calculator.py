#basic calculator 
m=int(input("enter the number"))
n=int(input("enter the number"))
choice=input("enter your choice,'add','substract','multiply','divide'")
if(choice=='add'):
    a=m+n
    print("the addition of number:",a)
elif(choice=='substrsct'):
    s=m-n
    print("the substraction of number:",s)
elif(choice=='multiply'):
    f=m*n
    print("the number is multiplied:",f)
elif(choice=='divide'):
    d=m//n
    print("the number is divided:",d)
else:
    print("wrong choice")