for i in range(int(raw_input())):
    z=int(raw_input())
    x=z
    k=z
    while z>1:
        x=x*(z-1)
        z=z-1
    if k==0:
        print '1'
    else:
        print x  
