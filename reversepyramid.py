num =5
count = num*2
for i in range(1,num+1):  
    for j in range(1,i):  
        print("-", end=" ")
    
    for k in range(1,count):
        print('*',end =" ")
    
    count -=2
    print()  
