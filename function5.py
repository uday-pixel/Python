def func(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    for i in range(1,num):
        for j in range(i,num):
            print("*",end=" ")
        print()
func(7)