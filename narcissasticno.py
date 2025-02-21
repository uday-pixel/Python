n =1634
orignal = n
total = 0
count = 0

while(n>0):
    count = count + 1
    n = n//10
n = orignal

while(n>0):
    rem = n%10
    n = n//10
    total = total + rem**count
print(total)

if(orignal==total):
    print("armstrong")
else:
    print("not a armstrong ")

'''
153 **3 
1634 **4
'''