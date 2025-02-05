number=10
new_no=number


while new_no !=1:
    sum=0
    for i in str(new_no):

        sum+=int(i)**2
        print(sum)
        
    new_no=sum

if new_no==1:
    print(number," is  a happy number")
else:
    print(number, "is not a happy number")    
