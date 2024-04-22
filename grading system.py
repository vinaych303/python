#grading system 
name=input("enter the name of student")
s1=int(input("enter the first subject marks"))
s2=int(input("enter the second subject marks"))
s3=int(input("enter the marks of third subject"))
s4=int(input("enter the marks of forth subject"))
s5=int(input("enter the marks of fifth subject"))
t=s1+s2+s3+s4+s5
percentage=t/5
print("your percentage is:",percentage)
if(s1>100 or s2>100 or s3>100 or s4>100 or s5>100 or s1<0 or s2<0 or s3<0 or s4<0 or s5<0):
    print("enter the wrong marks criteria")
elif(percentage==100):
    print("grade==O")
elif(percentage>=90):
    print("grade==A+")
elif(percentage>=80):
    print("grade==B+")
elif(percentage>=70):
    print("grade==B")
elif(percentage>=60):
    print("grade==C")
elif(percentage>=50):
    print("grade==D")
else:
    print("the student is fail")

