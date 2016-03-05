x=[]
for i in range(int(raw_input())):
    x=map(int,raw_input().split())
    x.sort()
    print x[1]
