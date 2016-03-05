for i in range(int(raw_input())):
    x,y=raw_input().split()
    
    z=0
    for i in x:
        if i in y:
            z+=1
    if z>=1:
        print "Yes"
    else:
        print "No"
         
