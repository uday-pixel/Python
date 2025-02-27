def avgmarks(hindi,eng,maths,science,sanskrit):
    return hindi+eng+maths+science+sanskrit/5
output=avgmarks(60,60,70,100,90)
print(output)

if(output>300):
    print("he is tooper",output)
else:
    print("he is passed",output)
#avgmarks