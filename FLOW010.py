for i in range (int(raw_input())):
    x=raw_input()
    if x=='B' or x=='b':
        print 'BattleShip'
    elif x=='C' or x=='c':
        print 'Cruiser'
    elif x=='d' or x=='D':
        print 'Destroyer'
    else:
        print 'Frigate' 
