def func(d):

    s = 0
    e = 4
    a =0
    while(s<=e):
        if(d[s]!=d[e]):
            a=1
            break
        s+=1
        e-=1
    if(a==0):
        print("palindrome")
    else:
        print("not palindrome")
func("saras")
