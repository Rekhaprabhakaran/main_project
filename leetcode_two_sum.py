li=[3,2,5,5,7]
target=10

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==target:
            print([i,j])
            
