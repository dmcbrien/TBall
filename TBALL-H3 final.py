#Duncan McBrien
#TBall-H3
#It works
import random
#the two batting orders for the 2 teams

def battername(batternumber):
    if batternumber==1:
        return('Duncan McBrien')
    if batternumber==2:
        return('Alex Verdugo')
    if batternumber==3:
        return('JD Martinez')
    if batternumber==4:
        return('Bobby Dalbec')
    if batternumber==5:
        return('Xander Bogaerts')
    if batternumber==6:
        return('Rafael Devers')
    if batternumber==7:
        return('Christian Vazquez')
    if batternumber==8:
        return('David Ortiz')
    if batternumber==9:
        return('Andrew Benintendi')
    
def batternameTwo(batternumber):
    if batternumber==1:
        return('Mike Trout')
    if batternumber==2:
        return('Chirs Sale')
    if batternumber==3:
        return('Coco Crisp')
    if batternumber==4:
        return('Brett Gardner')
    if batternumber==5:
        return('Manny Machado')
    if batternumber==6:
        return('Cy Young')
    if batternumber==7:
        return('Barry Bonds')
    if batternumber==8:
        return('Hank Aaron')
    if batternumber==9:
        return('Bryce Harper')
#gives the result for one batter, outputs the results of the at bat as 0 for out, 1 for single, 2 for double, 3 for triple, 4 for homerun, 5 for walk
    
def oneBatterResult():
    retry='yes'
    balltotal=0
    striketotal=0
    
    while retry=='yes':
        pitch=random.randint(1,15)
        #pitch=5
        #print('pitch',pitch)
        if pitch ==1 or pitch==10 or pitch==11:
            #single
            retry='no'
            field=random.randint(1,5)
            #print('field',field)
            if field==1 or field==2:
                print(" Base hit")
                totalbase=1
            else:
                print(' The batter is out')
                totalbase=0
        elif pitch ==2 or pitch==12:
            #double
            retry='no'
            field=random.randint(1,5)
            #print('field',field) 
            if field==1 or field==2:
                print(" Double")
                totalbase=2
            else:
                print(' The batter is out')
                totalbase=0
        elif pitch ==3 or pitch==13 :
            #triple
            retry='no'
            field=random.randint(1,5)
            #print('field',field)
            if field==1 or field==2:
                print(" Triple")
                totalbase=3
            else:
                print(' The batter is out')
                totalbase=0
        elif pitch==14:
            #homerun
            retry='no'
            print(' HOME RUN')
            totalbase=4
        elif pitch ==4 or pitch ==5 or pitch ==6 or pitch ==7 or pitch ==8 or pitch ==9:
            #strike
            print(' Strike')
            striketotal=striketotal+1
            if striketotal<3:
                retry='yes'
            else:
                retry='no'
                print(' Strike Out')
                totalbase=0
        elif pitch ==15:
            #ball
            print(' Ball')
            balltotal=balltotal+1
            if balltotal<4:
                rerty='yes'
            else:
                retry='no'
                print(' Walk')
                totalbase=5
    return totalbase
#team nanme inputs
team1=input("What is the name of team one?")
team2=input("What is the name of team two?")
     
out=0
runtotal=0
runtotalTwo=0
inning=1
finalTotal=0
finalTotalTwo=0
order=1
orderTwo=1
#while loop for the whole game, starts in the first inning and end at the 6th giving 5 innings.
while inning<6:
    print('\n')
    print("Its the",inning,'inning')
    print(team1,'are up to bat')
    print('\n')
    runtotal=0
    out=0
    firstbase='empty'
    secondbase='empty'
    thirdbase='empty'
    while out<3:
        batter=battername(order)
        print(batter,'is up.')
        result=oneBatterResult()
        #print('this is what happened during the at bat',result) 
        if result==0:
            out=out+1
        #counts the runs and moves players to the right base for a single
        if result==1:
            if thirdbase=="occupied":
                runtotal=runtotal+1
                thirdbase="empty"
            if secondbase=="occupied":
                thirdbase="occupied"
                secondbase="empty"
            if firstbase=="occupied":
                secondbase="occupied"
                firstbase='empty' 
            firstbase="occupied"
        #counts the runs and moves players to the right base for a double 
        if result==2:
            if thirdbase=='occupied' and secondbase=='occupied':
                runtotal=runtotal+2
                thirdbase='empty'
                secondbase='empty'
            if thirdbase=="occupied" and secondbase=='empty':
                runtotal=runtotal+1
                thirdbase="empty"
            if secondbase=="occupied" and thirdbase=='empty':
                runtotal=runtotal+1
                secondbase="empty"
            if firstbase=="occupied":
                thirdbase="occupied"
                firstbase='empty'
            secondbase="occupied"
        #counts the runs and moves players to the right base for a triple 
        if result==3:
            if thirdbase=='occupied' and secondbase=='occupied' and firstbase=='occupied':
                runtotal=runtotal+3
                thirdbase='empty'
                secondbase='empty'
                firstbase='empty'
            if thirdbase=='occupied' and secondbase=='empty' and firstbase=='empty':
                runtotal=runtotal+1
                thirdbase='empty'
            if thirdbase=='occupied' and secondbase=='occupied' and firstbase=='empty':
                runtotal=runtotal+2
                thridbase='empty'
                secondbase='empty'
            if thirdbase=='empty' and secondbase=='occupied' and firstbase=='occupied':
                runtotal=runtotal+2
                secondbase='empty'
                firstbase='empty'
            if thirdbase=='empty' and secondbase=='occupied' and firstbase=='empty':
                runtotal=runtotal+1
                secondbase='empty'
            if thirdbase=='empty' and secondbase=='empty' and firstbase=='occupied':
                runtotal=runtotal+1
                firstbase='empty'
            thirdbase='occupied'
        #clears the bases if there is a homerune and counts the proper score base off how many were on base.
        if result==4:
            if thirdbase=="occupied":
                runtotal=runtotal+1
                thirdbase='empty'
            if secondbase=="occupied":
                runtotal=runtotal+1
                secondbase='empty'
            if firstbase=='occupied':
                runtotal=runtotal+1
                firstbase='empty' 
            runtotal=runtotal+1
        #moves the runs if there is a walk
        if result==5:
            if thirdbase=='occupied' and secondbase=='occupied' and firstbase=='occupied':
               runtotal=runtotal+1
            if secondbase=='occupied' and firstbase=='occupied':
                thirdbase='occupied'
            if firstbase=='occupied':
                secondbase=='occupied'
            firstbase='occupied'
        #used for cycling through the batting order 
        order=order+1
        if order>9:
            order=1
        #prints the score for that one half inning 
    print('The',team1, 'scored',runtotal)
    #adds the score for that inning to the total score of the team
    finalTotal=finalTotal+runtotal
    #bottom half of the inning. This is for the second team, same code as above.
    print('\n')
    print(team2,'are up to bat')
    print('\n')
    out=0
    runtotalTwo=0
    firstbase='empty'
    secondbase='empty'
    thirdbase='empty'
    while out<3:
        batterTwo=batternameTwo(orderTwo)
        print(batterTwo,'is now up.') 
        result=oneBatterResult()
        #print('this is what happened during the at bat',result) 
        if result==0:
            out=out+1
        if result==1:
            if thirdbase=="occupied":
                runtotalTwo=runtotalTwo+1
                thirdbase="empty"
            if secondbase=="occupied":
                thirdbase="occupied"
                secondbase="empty"
            if firstbase=="occupied":
                secondbase="occupied"
                firstbase='empty' 
            firstbase="occupied"
        if result==2:
            if thirdbase=='occupied' and secondbase=='occupied':
                runtotalTwo=runtotalTwo+2
                thirdbase='empty'
                secondbase='empty'
            if thirdbase=="occupied" and secondbase=='empty':
                runtotalTwo=runtotalTwo+1
                thirdbase="empty"
            if secondbase=="occupied" and thirdbase=='empty':
                runtotalTwo=runtotalTwo+1
                secondbase="empty"
            if firstbase=="occupied":
                thirdbase="occupied"
                firstbase='empty'
            secondbase="occupied"
        if result==3:
            if thirdbase=='occupied' and secondbase=='occupied' and firstbase=='occupied':
                runtotalTwo=runtotalTwo+3
                thirdbase='empty'
                secondbase='empty'
                firstbase='empty'
            if thirdbase=='occupied' and secondbase=='empty' and firstbase=='empty':
                runtotalTwo=runtotalTwo+1
                thirdbase='empty'
            if thirdbase=='occupied' and secondbase=='occupied' and firstbase=='empty':
                runtotalTwo=runtotalTwo+2
                thridbase='empty'
                secondbase='empty'
            if thirdbase=='empty' and secondbase=='occupied' and firstbase=='occupied':
                runtotalTwo=runtotalTwo+2
                secondbase='empty'
                firstbase='empty'
            if thirdbase=='empty' and secondbase=='occupied' and firstbase=='empty':
                runtotalTwo=runtotalTwo+1
                secondbase='empty'
            if thirdbase=='empty' and secondbase=='empty' and firstbase=='occupied':
                runtotalTwo=runtotalTwo+1
                firstbase='empty'
            thirdbase='occupied'
        if result==4:
            if thirdbase=="occupied":
                runtotalTwo=runtotalTwo+1
                thirdbase='empty'
            if secondbase=="occupied":
                runtotalTwo=runtotalTwo+1
                secondbase='empty'
            if firstbase=='occupied':
                runtotalTwo=runtotalTwo+1
                firstbase='empty' 
            runtotalTwo=runtotalTwo+1
        if result==5:
            if thirdbase=='occupied' and secondbase=='occupied' and firstbase=='occupied':
               runtotalTwo=runtotalTwo+1
            if secondbase=='occupied' and firstbase=='occupied':
                thirdbase='occupied'
            if firstbase=='occupied':
                secondbase=='occupied'
            firstbase='occupied'
        orderTwo=orderTwo+1
        if orderTwo>9:
            orderTwo=1 
    print('The',team2,'scored',runtotalTwo)
    finalTotalTwo=finalTotalTwo+runtotalTwo
    #moves the inning to the next inning
    inning=inning+1
#prints final score 
print('The',team1,'scored,',finalTotal,'.The',team2,'scored',finalTotalTwo) 
