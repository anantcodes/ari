#10 Coins puzzle
#1 represents head and O represents tail
import random
P1=[]
P2=[]
for i in range(5):
    P1.append(random.randint(0,1))
print("P1",P1)
count1=0;
count0=0;
for i in P1:
    if(i==0):
        count0=count0+1
    else:
        count1+=1
for i in range(5-count0):
    P2.append(0)
for i in range(5-count1):
    P2.append(1)
print("P2",P2)
for i in range(5):
    if P2[i]==0:
        P2[i]=1
    else:
        P2[i]=0
print("After flipping P2",P2)

cnt=0
for i in range(5):
    if P2[i]==0:
        cnt+=1
print("Number of heads in P1 and P2 are equal:", cnt==count0);
