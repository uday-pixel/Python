mylist=[10,20,25,30]
out=list(filter(lambda num: num%2==0,mylist))
print(out)


mylist=[10,20,25,30]
out=list(map(lambda num: num%2==0,mylist))
print(out)