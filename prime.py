val2=int(input())
if(val2>1):
    for i in range(2,val2):
        if(val2%i==0):
            print("no")
            break
        else:
            print("yes")
            break
