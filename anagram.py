s="rat"
t="car"
dict1={}
for char in s:
    if char  not in dict1:
        dict1[char]=1
    else:
        dict1[char]= dict1[char]+1
dict2={}
for char in t:
    if char not in dict2:
        dict2[char]=1
    else:
        dict2[char]= dict2[char]+1
print(dict1)
print(dict2)
if(dict1==dict2):
    print("TRUE")
else:
    print("FALSE")
