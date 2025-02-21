for n in range(140,160):
    n = int(input("enter the no"))
    orignal = n
    sum = 0
    while(n!=0):
        rem = n%10
        n = n//10
        sum = sum + rem**3

    if(orignal == sum):
        print("armstrong",orignal)
    else:
        print("not armstrong",orignal) 