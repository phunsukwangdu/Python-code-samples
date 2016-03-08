x,y=map(int,raw_input().split())
z=0
for i in range (x):
    m=int(raw_input())
    if m%y==0:
        z+=1
print z   
     
