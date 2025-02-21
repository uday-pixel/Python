data = [10,20,30,90]
max =0
smax =0

for i in range(0,len(data)):
    if(data[i]>max):
        smax=max 
        max = data[i]
    elif(data[i]>smax):
        smax=data[i]
print(max,smax)