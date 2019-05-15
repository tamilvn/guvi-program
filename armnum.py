n=int(input())
q=int(input())
for val2 in range(n,q+1):
    sum=0
    temp=val2
    while(temp>0):
        dig=temp%10
        sum=sum+dig**3
        temp=temp//10
    if(val2==sum):
        print(val2)
