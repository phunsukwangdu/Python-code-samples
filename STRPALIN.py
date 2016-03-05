for i in range(int(raw_input())):
    x=raw_input()
    y=raw_input()
    z=0
    for i in x:
        if i in y:
            z+=1
    if z>=1:
        print "Yes"
    else:
        print "No"
         
