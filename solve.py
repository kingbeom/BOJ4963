a=int(input())
p=list(map(int, input().split()))
b,c=map(int, input().split())
cnt=0
for i in range(len(p)):
    p[i]-=b
    cnt+=1
for i in range(len(p)):
    if p[i]<=0:
        continue
    elif p[i]<=c:
        cnt+=1
    elif p[i]>c:
        if p[i]%c==0:
            cnt+=p[i]//c
        elif p[i]%c!=0:
            cnt+=(p[i]//c)+1
print(cnt)