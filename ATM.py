x,y=map(float,raw_input().split())
if x<y-0.5 and x%5==0:
    print '{:.2f}'.format(y-x-0.5)
else:
    print '{:.2f}'.format(y)
    
     
