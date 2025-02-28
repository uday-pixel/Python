nums=[1,2,3,1]
mydict={}
for i in nums:
    if i not in mydict:
        mydict[i]=1
    else:
        print("true")
else:
    print("false")
print(mydict)