import sys
dicts = []
with open('in.txt') as file:

    for line in file:
        dicts.append(line[:-1])  

    print(dicts)  
    for pal1 in dicts:
        for pal2 in dicts:
            diff = 0
            for i in range(0, len(pal1)):
                if( pal1[i] != pal2[i]):
                    diff+=1
            if ( diff == 1):
                print(pal1,'\t',pal2)
                print('\n')
                for i in range(0 , len(pal1)):
                    if( pal1[i] == pal2[i]):
                        print(pal1[i] , end='')
                sys.exit()
                        



