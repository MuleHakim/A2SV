n = int(input())
s = [int(x)for x in input().split()]
zeros = []
posatives = []
negatives =[]
for i in range(n):
    if s[i]>0:
        posatives.append(s[i])
    elif s[i]== 0:
        zeros.append(s[i])
    else:
        negatives.append(s[i])
cost =0
for i in range(len(posatives)):
    cost+=posatives[i]-1
for i in range(len(negatives)):
    cost+=(-1-negatives[i])
if len(zeros)>0:
    cost+=len(zeros)
elif len(negatives)%2 ==1:
    cost+=2
print(cost)
