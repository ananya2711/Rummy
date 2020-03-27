import pygame
import random


#cards access
pack= ["1_clubs","2_clubs","3_clubs","4_clubs","5_clubs","6_clubs",
           "7_clubs","8_clubs","9_clubs","10_clubs","11_clubs","12_clubs",
           "13_clubs","1_spades","2_spades","3_spades","4_spades",
           "5_spades","6_spades","7_spades","8_spades","9_spades","10_spades",
           "11_spades","12_spades","13_spades","1_hearts","2_hearts",
           "3_hearts","4_hearts","5_hearts","6_hearts","7_hearts","8_hearts",
           "9_hearts","10_hearts","11_hearts","12_hearts","13_hearts",
           "1_diamonds","2_diamonds","3_diamonds","4_diamonds","5_diamonds",
           "6_diamonds","7_diamonds","8_diamonds","9_diamonds","10_diamonds",
           "11_diamonds","12_diamonds","13_diamonds"]
#card value access
valcard={"1_clubs":1,"2_clubs":2,"3_clubs":3,"4_clubs":4,"5_clubs":5,"6_clubs":6,
           "7_clubs":7,"8_clubs":8,"9_clubs":9,"10_clubs":10,"11_clubs":11,"12_clubs":12,
           "13_clubs":13,"1_spades":1,"2_spades":2,"3_spades":3,"4_spades":4,
           "5_spades":5,"6_spades":6,"7_spades":7,"8_spades":8,"9_spades":9,"10_spades":10,
           "11_spades":11,"12_spades":12,"13_spades":13,"1_hearts":1,"2_hearts":2,
           "3_hearts":3,"4_hearts":4,"5_hearts":5,"6_hearts":6,"7_hearts":7,"8_hearts":8,
           "9_hearts":9,"10_hearts":10,"11_hearts":11,"12_hearts":12,"13_hearts":13,
           "1_diamonds":1,"2_diamonds":2,"3_diamonds":3,"4_diamonds":4,"5_diamonds":5,
           "6_diamonds":6,"7_diamonds":7,"8_diamonds":8,"9_diamonds":9,"10_diamonds":10,
           "11_diamonds":11,"12_diamonds":12,"13_diamonds":13}
comp4=[]#grp of 4 cards
comp4c=False
comp31=[]#grp of 3 cards1
comp31c=False
comp32=[]#grp of 3 cards 2
comp32c=False

result=False
take=False
discard=False
myturn=False
compturn=False

newmypack=[]
#my pack of cards
mypack=[]

#computers pack of cards
comppack=[]

#cards not in either hand
rest=[]

# images of the cards
card_dict = {}

#present on discarded ine
present=''

                                                

def showend(screen):#function for the end of the game
    """displays my final set,asks for order and displays score"""
    myfont=pygame.font.Font(None,40)
    screen.fill((255,255,255))
    text=myfont.render("select a run first,followed by sets of 3 ",1,(0,0,0))
    screen.blit(text,(400,440))
    pygame.display.update()       
    pygame.time.delay(3000)
    #my cards on screen
    pygame.display.update()
    pygame.draw.rect(screen,(0,0,0),[20,600,71,96])
    screen.blit(card_dict[mypack[0]],[20,600])
    pygame.draw.rect(screen,(0,0,0),[120,600,71,96])
    screen.blit(card_dict[mypack[1]],[120,600])
    pygame.draw.rect(screen,(0,0,0),[220,600,71,96])
    screen.blit(card_dict[mypack[2]],[220,600])
    pygame.draw.rect(screen,(0,0,0),[320,600,71,96])
    screen.blit(card_dict[mypack[3]],[320,600])
    pygame.draw.rect(screen,(0,0,0),[420,600,71,96])
    screen.blit(card_dict[mypack[4]],[420,600])
    pygame.draw.rect(screen,(0,0,0),[520,600,71,96])
    screen.blit(card_dict[mypack[5]],[520,600])
    pygame.draw.rect(screen,(0,0,0),[620,600,71,96])
    screen.blit(card_dict[mypack[6]],[620,600])
    pygame.draw.rect(screen,(0,0,0),[720,600,71,96])
    screen.blit(card_dict[mypack[7]],[720,600])
    pygame.draw.rect(screen,(0,0,0),[820,600,71,96])
    screen.blit(card_dict[mypack[8]],[820,600])
    pygame.draw.rect(screen,(0,0,0),[920,600,71,96])
    screen.blit(card_dict[mypack[9]],[920,600])
    pygame.draw.rect(screen,(0,0,0),[1020,600,71,96])
    pygame.display.update()

    #displaying cards of computer
    x=20
    for i in range(len(comppack)):
        pygame.draw.rect(screen,(0,0,0),[x,20,71,96])
        screen.blit(card_dict[comppack[i]],[x,20])
        x+=100
        
    for i in range(len(comp4)):
        pygame.draw.rect(screen,(0,0,0),[x,20,71,96])
        screen.blit(card_dict[comp4[i]],[x,20])
        x+=100
        
    for i in range(len(comp31)):
        pygame.draw.rect(screen,(0,0,0),[x,20,71,96])
        screen.blit(card_dict[comp31[i]],[x,20])
        x+=100
    for i in range(len(comp32)):
        pygame.draw.rect(screen,(0,0,0),[x,20,71,96])
        screen.blit(card_dict[comp32[i]],[x,20])
        x+=100

    pygame.display.update()

    
    a=0
    selected = [False,False,False,False,False,False,False,False,False,False]
    while a!=10:
      event=pygame.event.wait()
      if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==1:
            
            x,y=pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]
            if 20<=x<=91 and 600<=y<=300+396 and selected[0]==False:
                newmypack.append(mypack[0])
                pygame.draw.rect(screen,(0,0,0),[20,600,71,96])
                pygame.display.update()
                selected[0]=True
                a+=1
                
            elif 20<=x<=91 and 600<=y<=300+396:
                pass
            elif 120<=x<=191 and 600<=y<=300+396 and selected[1]==False:
                newmypack.append(mypack[1])
                pygame.draw.rect(screen,(0,0,0),[120,600,71,96])
                selected[1]=True
                a+=1
                
            elif 120<=x<=191 and 600<=y<=300+396:
                pass
            elif 220<=x<=291 and 600<=y<=300+396 and selected[2]==False:
                newmypack.append(mypack[2])
                pygame.draw.rect(screen,(0,0,0),[220,600,71,96])
                pygame.display.update()
                selected[2]=True
                a+=1
                
            elif 220<=x<=291 and 600<=y<=300+396:
                pass
            elif 320<=x<=391 and 600<=y<=300+396 and selected[3]==False:
                newmypack.append(mypack[3])
                pygame.draw.rect(screen,(0,0,0),[320,600,71,96])
                pygame.display.update()
                selected[3]=True
                a+=1
                
            elif 320<=x<=391 and 600<=y<=300+396:
                pass
            elif 420<=x<=491 and 600<=y<=300+396 and selected[4]==False:
                newmypack.append(mypack[4])
                pygame.draw.rect(screen,(0,0,0),[420,600,71,96])
                pygame.display.update()
                selected[4]=True
                a+=1
            elif 420<=x<=491 and 600<=y<=300+396 :
                pass
            elif 520<=x<=591 and 300+300<=y<=300+396 and selected[5]==False:
                newmypack.append(mypack[5])
                pygame.draw.rect(screen,(0,0,0),[520,600,71,96])
                pygame.display.update()
                selected[5]=True
                a+=1
            elif 520<=x<=591 and 300+300<=y<=300+396 :
                pass
            elif 620<=x<=691 and 300+300<=y<=300+396 and selected[6]==False:
                newmypack.append(mypack[6])
                pygame.draw.rect(screen,(0,0,0),[620,600,71,96])
                selected[6]=True
                a+=1
                
            elif 620<=x<=691 and 300+300<=y<=300+396:
                pass
            elif 720<=x<=791 and 300+300<=y<=300+396 and selected[7]==False:
                newmypack.append(mypack[7])
                pygame.draw.rect(screen,(0,0,0),[720,600,71,96])
                pygame.display.update()
                selected[7]=True
                a+=1
                
            elif 720<=x<=791 and 300+300<=y<=300+396:
                pass
            elif 820<=x<=891 and 300+300<=y<=300+396 and selected[8]==False:
                newmypack.append(mypack[8])
                pygame.draw.rect(screen,(0,0,0),[820,600,71,96])
                pygame.display.update()
                selected[8]=True
                a+=1
                
            elif 820<=x<=891 and 300+300<=y<=300+396 :
                pass
            elif 920<=x<=991 and 300+300<=y<=300+396 and selected[9]==False:
                newmypack.append(mypack[9])
                pygame.draw.rect(screen,(0,0,0),[920,600,71,96])
                pygame.display.update()
                selected[9]=True
                a+=1
                
            elif 920<=x<=991 and 300+300<=y<=300+396:
                pass
            elif 1020<=x<=1091 and 300+300<=y<=300+396 and selected[10]==False:
                newmypack.append(mypack[10])
                pygame.draw.rect(screen,(0,0,0),[1020,600,71,96])
                pygame.display.update()
                selected[10]=True
                a+=1
                
            elif 1020<=x<=1091 and 300+300<=y<=300+396 :  
                pass  
            else:
                print("Error")
            pygame.display.update()

            
    countable=[]#cards to consider for scores in mypack
    #checking if cards satisfy the given conditions
    s=newmypack[0]
    a=s.find('_')
    no=int(s[0:a])
    suit=s[a+1:]
    if not(str(no+1) in newmypack[1] and str(no+2) in newmypack[2] and str(no+3) in newmypack[3] and suit in newmypack[1] and suit in newmypack[2] and suit in newmypack[3]):
           countable.extend(newmypack[:4])
    
    s=newmypack[4]
    a=s.find('_')
    no=int(s[0:a])
    if not(str(no) in newmypack[5] and str(no) in newmypack[6]):
           countable.extend(newmypack[4:7])
    s=newmypack[7]
    a=s.find('_')
    no=int(s[0:a])
    if not(str(no) in newmypack[8] and str(no) in newmypack[9]):
           countable.extend(newmypack[7:10])
    myscore=0       
    if len(countable)==0:
              myscore=0
    else:
           for i in countable:
               myscore+=valcard[i]
    compscore=0
    if len(comppack)==0:
            compscore=0
    else:
            print(comppack)
            for i in comppack:
                compscore+=int(valcard[i])
                
    pygame.time.delay(110)
        
    screen.fill((255,255,255))
    myfont=pygame.font.Font(None,40)
    text1="your score is: "+str(myscore)
    text=myfont.render(text1,1,(100,100,0))
    screen.blit(text,(400,400))
    pygame.time.delay(3000)
    text2="computers score is : "+str(compscore)
    pygame.display.update()

    text=myfont.render(text2,1,(0,0,0))
    screen.blit(text,(400,440))
    pygame.display.update()       
    pygame.time.delay(3000)
    screen.fill((255,255,255))
    if compscore<myscore:
        text=myfont.render("Computer wins",1,(100,100,100))
        screen.blit(text,(400,400))
        pygame.display.update()  
        pygame.time.delay(3000)
    else:
        text=myfont.render("You win",1,(100,100,100))
        screen.blit(text,(400,400))
        pygame.time.delay(3000)
        
        
    screen.fill((255,255,255))
    text=myfont.render("thank you for playing.Hope you like it :)",1,(100,100,100))
    screen.blit(text,(400,400))
    pygame.display.update()  
    pygame.time.delay(3000)
    
               
def makemypack():#makes my pack from pack elements
    for i in range(10):
        l=len(pack)
        a=random.randint(0,l-1)
        mypack.append(pack[a])
        del pack[a]

def makecomppack():#makes computers pack from pack elements
    for i in range(10):
        l=len(pack)
        a=random.randint(0,l-1)
        comppack.append(pack[a])
        del pack[a]

def compreturn(b):#returns card from computers cards
    """takes name of card  as argument"""
    global present
    pygame.display.update()  
    pygame.time.delay(2000)
    pack.append(present)
    present=comppack[comppack.index(b)]
    del comppack[comppack.index(b)]
    screen.blit(card_dict[present],[350,300])

def returncard(ind):#returns cards from my set of cards
    """takes indexof card as argument"""
    global present
    pack.append(present)
    present=mypack[ind]
    del mypack[ind]
    screen.blit(card_dict[present],[350,300])
    pygame.time.delay(100) 
    
def comppickpresent():
    """pick from exposed stack"""
    global present
    comppack.append(present)
    present=''
    
def comppickstack():
    """pick card from stack"""
    x=random.randint(0,len(pack)-1)
    comppack.append(pack[x])
    del pack[x]
   

    
def drawcardstack():
    x=random.randint(0,len(pack)-1)
    mypack.append(pack[x])
    del pack[x]
    screen.blit(card_dict[mypack[-1]],[1020,600])
    
def drawcardpresent():
    global present
    mypack.append(present)
    present=''
    screen.blit(card_dict[mypack[-1]],[1020,600])
    
def presentallot():
    #alloting present for start of program only
    global present
    x=random.randint(0,len(pack)-1)
    present=pack[x]
    del pack[x]
    screen.blit(card_dict[present],[350,300])

def shift(x,y,ind):
    for i in range(ind,len(mypack)):
        screen.blit(card_dict[mypack[i]],[x,y])
        x+=100
    pygame.draw.rect(screen,(0,0,0),[1020,600,71,96])

def comparrange3():
    """returns 3,3 if everyset made
    1,not imp card name 1:pick from present
    2,not important card name 2:Pick from stack
    0,comppack[0] pick from stack and return any card"""
    global comp31c
    global comp32c
    global comp4c
    comppack=sorted(comppack)
    triples=[]#triples already made
    important=[]#cards required to make 3s 2 already present
    needed=[]#3rd card needed to make complete set of 3
    for i in range(len(comppack)-2):#checked if a triple already exists
        if '1' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
        if '2' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
        if '3' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
        if '4' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
        if '5' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
        if '6' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
        if '7' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
        if '8' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
        if '9' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
        if '10' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
        if '11' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
        if '12' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
        if '13' in comppack[i] and comppack[i+1] and comppack[i+2]:
            triples.append(comppack[i])
            triples.append(comppack[i+1])
            triples.append(comppack[i+2])
    if len(triples)==6:
        comp31=triples[:3]
        comp32=triples[3:]
        comp31c=True
        comp32c=True
        del comppack[comppack.index(triples[0])]
        del comppack[comppack.index(triples[1])]
        del comppack[comppack.index(triples[2])]
        del comppack[comppack.index(triples[3])]
        del comppack[comppack.index(triples[4])]
        del comppack[comppack.index(triples[5])]
    elif len(triples)==3:
        comp31=triples[:3]
        comp31c=True
        del comppack[comppack.index(triples[0])]
        del comppack[comppack.index(triples[1])]
        del comppack[comppack.index(triples[2])]
    else:
      for i in range(len(comppack)-1):
        if '1' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1])
            for j in pack:
                if j not in important and "1" in j:
                    needed.append(j)
        if '2' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1])
            for j in pack:
                if j not in important and "2" in j:
                    needed.append(j)
        if '3' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1])
            for i in pack:
                if i not in important and "3" in i:
                    needed.append(i)
        if '4' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1])
            for j in pack:
                if j not in important and "4" in j:
                    needed.append(j)
        if '5' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1])
            for j in pack:
                if j not in important and "5" in j:
                    needed.append(j)
        if '6' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1])
            for j in pack:
                if j not in important and "6" in j:
                    needed.append(j)
        if '7' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1])
            for j in pack:
                if j not in important and "7" in j:
                    needed.append(j)
        if '8' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1])
            for j in pack:
                if j not in important and "8" in j:
                    needed.append(j)
        if '9' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1])
            for i in pack:
                if j not in important and "9" in j:
                    needed.append(j)
        if '10' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1])
            for j in pack:
                if j not in important and "10" in j:
                    needed.append(j)
        if '11' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1])
            for j in pack:
                if j not in important and "11" in j:
                    needed.append(j)
        if '12' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1])
            for j in pack:
                if j not in important and "12" in j:
                    needed.append(j)
        if '13' in comppack[i] and comppack[i+1]:
            important.append(comppack[i])
            important.append(comppack[i+1]) 
            for j in pack:
                if j not in important and "13" in j:
                    needed.append(j)
    if comp4c==True and comp31c==True and comp32c==True:
        global result
        result=True
        return 3,3
    elif present in needed:
        for i in comppack:
            if i not in important:
                return 1,i#pick last one in discarded pile and return not imp card
            else:
                return 1,important[0]#pick last one in discarded pile and return not imp card
    elif len(needed)!=0:
        for i in comppack:
            if i not in important:
                return 2,i#pick one from stack and return not imp card
            else:
                return 2,important[0]
    else:
        return 0,comppack[0]   #pick up from stack and return any card
    



    
def compcompare():
    """calls compcompare3() if 4c made
    1,not imp card name 1:pick from present
    2,not important card name 2:Pick from stack
    0,comppack[0] pick from stack and return any card"""
    global comp4c
    needed=[]#card required to complete set of 4
    important=[]#set of 3 already present
    club=[]
    clubv=[]
    spade=[]
    spadev=[]
    heart=[]
    heartv=[]
    diamond=[]
    diamondv=[]
    for i in comppack:
        if "clubs" in i:
            club.append(i)
        elif "spades" in i:
            spade.append(i)
        elif "hearts" in i:
            heart.append(i)
        else:
            diamond.append(i)
    for i in club:
        clubv.append(valcard[i])
    for i in spade:
        spadev.append(valcard[i])
    for i in heart:
        heartv.append(valcard[i])    
    for i in diamond:
        diamondv.append(valcard[i])
    if comp4c==False: 
     for i in range(1,11):
       if i in clubv and i+1 in clubv and i+2 in clubv and i+3 in clubv:
           a=clubv.index(i)
           b=clubv.index(i+1)
           c=clubv.index(i+2)
           d=clubv.index(i+3)
           comp4=[club[a],club[b],club[c],club[d]]
           comp4c=True
           del comppack[comppack.index(club[a])]
           del comppack[comppack.index(club[b])]
           del comppack[comppack.index(club[c])]
           del comppack[comppack.index(club[d])]
           del club[a]
           del clubv[a]
           del club[b]
           del clubv[b]
           del club[c]
           del clubv[c]
           del club[d]
           del clubv[d]
           
       elif i in spadev and i+1 in spadev and i+2 in spadev and i+3 in spadev:
           a=spadev.index(i)
           b=spadev.index(i+1)
           c=spadev.index(i+2)
           d=spadev.index(i+3)
           comp4=[spade[a],spade[b],spade[c],spade[d]]
           comp4c=True
           del comppack[comppack.index(spade[a])]
           del comppack[comppack.index(spade[b])]
           del comppack[comppack.index(spade[c])]
           del comppack[comppack.index(spade[d])]
           del spade[a]
           del spadev[a]
           del spade[b]
           del spadev[b]
           del spade[c]
           del spadev[c]
           del spade[d]
           del spadev[d]
       elif i in heartv and i+1 in heartv and i+2 in heartv and i+3 in heartv:
           a=heartv.index(i)
           b=heartv.index(i+1)
           c=heartv.index(i+2)
           d=heartv.index(i+3)
           comp4=[heart[a],heart[b],heart[c],heart[d]]
           comp4c=True
           del comppack[comppack.index(heart[a])]
           del comppack[comppack.index(heart[b])]
           del comppack[comppack.index(heart[c])]
           del comppack[comppack.index(heart[d])]
           del heart[a]
           del heartv[a]
           del heart[b]
           del heartv[b]
           del heart[c]
           del heartv[c]
           del heart[d]
           del heartv[d]
       elif i in diamondv and i+1 in diamondv and i+2 in diamondv and i+3 in diamondv:
           a=diamondv.index(i)
           b=diamondv.index(i+1)
           c=diamondv.index(i+2)
           d=diamondv.index(i+3)
           comp4=[diamond[a],diamond[b],diamond[c],diamond[d]]
           comp4c=True
           del comppack[comppack.index(diamond[a])]
           del comppack[comppack.index(diamond[b])]
           del comppack[comppack.index(diamond[c])]
           del comppack[comppack.index(diamond[d])]
           del diamond[a]
           del diamondv[a]
           del diamond[b]
           del diamondv[b]
           del diamond[c]
           del diamondv[c]
           del diamond[d]
           del diamondv[d]
    if comp4c==False:
        for i in range(1,12):
            if i in clubv and i+1 in clubv and i+2 in clubv:
                if i!=1:
                    needed.append(str(i-1)+"_clubs")
                    needed.append(str(i+3)+"_clubs")
                elif i==11:
                    needed.append(str(i-1)+"_clubs")
                else:
                    needed.append(str(i+3)+"_clubs")
                important.append(str(i)+'_clubs')
                important.append(str(i+1)+'_clubs')
                important.append(str(i+2)+'_clubs')
            if i in spadev and i+1 in spadev and i+2 in spadev:
                if i!=1:
                    needed.append(str(i-1)+"_spades")
                    needed.append(str(i+3)+"_spades")
                elif i==11:
                    needed.append(str(i-1)+"_spades")
                else:
                    needed.append(str(i+3)+"_spades")
                important.append(str(i)+"_spades")
                important.append(str(i+1)+"_spades")
                important.append(str(i+2)+"_spades")
            if i in heartv and i+1 in heartv and i+2 in heartv:
                if i!=1:
                    needed.append(str(i-1)+"_hearts")
                    needed.append(str(i+3)+"_hearts")
                elif i==11:
                    needed.append(str(i-1)+"_hearts")
                else:
                    needed.append(str(i+3)+"_hearts")
                important.append(str(i)+"_hearts")
                important.append(str(i+1)+"_hearts")
                important.append(str(i+2)+"_hearts")
            if i in diamondv and i+1 in diamondv and i+2 in diamondv:
                if i!=1:
                    needed.append(str(i-1)+"_diamonds")
                    needed.append(str(i+3)+"_diamonds")
                elif i==11:
                    needed.append(str(i-1)+"_diamonds")   
                else:
                    needed.append(str(i+3)+"_diamonds")
                important.append(str(i)+"_diamonds")
                important.append(str(i+1)+"_diamonds")
                important.append(str(i+2)+"_diamonds")
    if comp4c==True:
        return comparrange3()
    elif present in needed:
        for i in comppack:
            if i not in important:
                return 1,i
            else:
                return 1,important[0]#pick last one in discarded pile and return not imp card
    elif len(needed)!=0:
        for i in comppack:
            if i not in important:
                return 2,i#pick one from stack and return not imp card
            else:
                return 2,important[0]
    else:
        return 0,comppack[0]   #pick up from stack and return any card
    
                    
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([1150,750])
    
    
    done=False
    screen.fill((255,255,255))
    pygame.display.set_caption("Rummy")

    pygame.display.update()

    pic= pygame.image.load("ace_clubs.png").convert()
    card_dict["1_clubs"] = pic
    pic = pygame.image.load("2_clubs.png").convert()
    card_dict["2_clubs"] = pic
    pic= pygame.image.load("3_clubs.png").convert()
    card_dict["3_clubs"] = pic
    pic = pygame.image.load("4_clubs.png").convert()
    card_dict["4_clubs"] = pic
    pic = pygame.image.load("5_clubs.png").convert()
    card_dict["5_clubs"] = pic
    pic = pygame.image.load("6_clubs.png").convert()
    card_dict["6_clubs"] = pic
    pic = pygame.image.load("7_clubs.png").convert()
    card_dict["7_clubs"] = pic
    pic = pygame.image.load("8_clubs.png").convert()
    card_dict["8_clubs"] = pic
    pic = pygame.image.load("9_clubs.png").convert()
    card_dict["9_clubs"] = pic
    pic = pygame.image.load("10_clubs.png").convert()
    card_dict["10_clubs"] = pic
    pic = pygame.image.load("jack_clubs.png").convert()
    card_dict["11_clubs"] = pic
    pic= pygame.image.load("queen_clubs.png").convert()
    card_dict["12_clubs"] = pic
    pic = pygame.image.load("king_clubs.png").convert()
    card_dict["13_clubs"] = pic
    pic = pygame.image.load("ace_spades.png").convert()
    card_dict["1_spades"] = pic
    pic = pygame.image.load("2_spades.png").convert()
    card_dict["2_spades"] = pic
    pic = pygame.image.load("3_spades.png").convert()
    card_dict["3_spades"] = pic
    pic = pygame.image.load("4_spades.png").convert()
    card_dict["4_spades"] = pic
    pic = pygame.image.load("5_spades.png").convert()
    card_dict["5_spades"] = pic
    pic= pygame.image.load("6_spades.png").convert()
    card_dict["6_spades"] = pic
    pic= pygame.image.load("7_spades.png").convert()
    card_dict["7_spades"] = pic
    pic = pygame.image.load("8_spades.png").convert()
    card_dict["8_spades"] = pic
    pic = pygame.image.load("9_spades.png").convert()
    card_dict["9_spades"] = pic
    pic = pygame.image.load("10_spades.png").convert()
    card_dict["10_spades"] = pic
    pic = pygame.image.load("jack_spades.png").convert()
    card_dict["11_spades"] = pic
    pic = pygame.image.load("queen_spades.png").convert()
    card_dict["12_spades"] = pic
    pic = pygame.image.load("king_spades.png").convert()
    card_dict["13_spades"] = pic
    pic = pygame.image.load("ace_hearts.png").convert()
    card_dict["1_hearts"] = pic
    pic = pygame.image.load("2_hearts.png").convert()
    card_dict["2_hearts"] = pic
    pic = pygame.image.load("3_hearts.png").convert()
    card_dict["3_hearts"] = pic
    pic = pygame.image.load("4_hearts.png").convert()
    card_dict["4_hearts"] = pic
    pic= pygame.image.load("5_hearts.png").convert()
    card_dict["5_hearts"] = pic
    pic = pygame.image.load("6_hearts.png").convert()
    card_dict["6_hearts"] = pic
    pic = pygame.image.load("7_hearts.png").convert()
    card_dict["7_hearts"] = pic
    pic = pygame.image.load("8_hearts.png").convert()
    card_dict["8_hearts"] = pic
    pic= pygame.image.load("9_hearts.png").convert()
    card_dict["9_hearts"] = pic
    pic= pygame.image.load("10_hearts.png").convert()
    card_dict["10_hearts"] = pic
    pic = pygame.image.load("jack_hearts.png").convert()
    card_dict["11_hearts"] = pic
    pic = pygame.image.load("queen_hearts.png").convert()
    card_dict["12_hearts"] = pic
    pic = pygame.image.load("king_hearts.png").convert()
    card_dict["13_hearts"] = pic
    pic= pygame.image.load("ace_diamonds.png").convert()
    card_dict["1_diamonds"] = pic
    pic = pygame.image.load("2_diamonds.png").convert()
    card_dict["2_diamonds"] = pic
    pic = pygame.image.load("3_diamonds.png").convert()
    card_dict["3_diamonds"] = pic
    pic = pygame.image.load("4_diamonds.png").convert()
    card_dict["4_diamonds"] = pic
    pic = pygame.image.load("5_diamonds.png").convert()
    card_dict["5_diamonds"] = pic
    pic = pygame.image.load("6_diamonds.png").convert()
    card_dict["6_diamonds"] = pic
    pic = pygame.image.load("7_diamonds.png").convert()
    card_dict["7_diamonds"] = pic
    pic = pygame.image.load("8_diamonds.png").convert()
    card_dict["8_diamonds"] = pic
    pic = pygame.image.load("9_diamonds.png").convert()
    card_dict["9_diamonds"] = pic
    pic = pygame.image.load("10_diamonds.png").convert()
    card_dict["10_diamonds"] = pic
    pic = pygame.image.load("jack_diamonds.png").convert()
    card_dict["11_diamonds"] = pic
    pic = pygame.image.load("queen_diamonds.png").convert()
    card_dict["12_diamonds"] = pic
    pic= pygame.image.load("king_diamonds.png").convert()
    card_dict["13_diamonds"] = pic

    makemypack()
    makecomppack()
    mypack=sorted(mypack)
    comppack=sorted(comppack)
   
    discard=False
    
    compturn=False
    myturn=True
    take=True
    
    back = pygame.image.load("back.png").convert()
#my cards on screen
    pygame.draw.rect(screen,(0,0,0),[20,600,71,96])
    screen.blit(card_dict[mypack[0]],[20,600])
    pygame.draw.rect(screen,(0,0,0),[120,600,71,96])
    screen.blit(card_dict[mypack[1]],[120,600])
    pygame.draw.rect(screen,(0,0,0),[220,600,71,96])
    screen.blit(card_dict[mypack[2]],[220,600])
    pygame.draw.rect(screen,(0,0,0),[320,600,71,96])
    screen.blit(card_dict[mypack[3]],[320,600])
    pygame.draw.rect(screen,(0,0,0),[420,600,71,96])
    screen.blit(card_dict[mypack[4]],[420,600])
    pygame.draw.rect(screen,(0,0,0),[520,600,71,96])
    screen.blit(card_dict[mypack[5]],[520,600])
    pygame.draw.rect(screen,(0,0,0),[620,600,71,96])
    screen.blit(card_dict[mypack[6]],[620,600])
    pygame.draw.rect(screen,(0,0,0),[720,600,71,96])
    screen.blit(card_dict[mypack[7]],[720,600])
    pygame.draw.rect(screen,(0,0,0),[820,600,71,96])
    screen.blit(card_dict[mypack[8]],[820,600])
    pygame.draw.rect(screen,(0,0,0),[920,600,71,96])
    screen.blit(card_dict[mypack[9]],[920,600])
    pygame.draw.rect(screen,(0,0,0),[1020,600,71,96])
                

#computers cards on screen
    pygame.draw.rect(screen,(0,0,0),[20,20,71,96])
    screen.blit(back,[20,20])            
    pygame.draw.rect(screen,(0,0,0),[120,20,71,96])
    screen.blit(back,[120,20]) 
    pygame.draw.rect(screen,(0,0,0),[220,20,71,96])
    screen.blit(back,[220,20])             
    pygame.draw.rect(screen,(0,0,0),[320,20,71,96])
    screen.blit(back,[320,20])              
    pygame.draw.rect(screen,(0,0,0),[420,20,71,96])
    screen.blit(back,[420,20])              
    pygame.draw.rect(screen,(0,0,0),[520,20,71,96])
    screen.blit(back,[520,20])              
    pygame.draw.rect(screen,(0,0,0),[620,20,71,96])
    screen.blit(back,[620,20])              
    pygame.draw.rect(screen,(0,0,0),[720,20,71,96])
    screen.blit(back,[720,20])              
    pygame.draw.rect(screen,(0,0,0),[820,20,71,96])
    screen.blit(back,[820,20])              
    pygame.draw.rect(screen,(0,0,0),[920,20,71,96])
    screen.blit(back,[920,20])              
   
    pygame.draw.ellipse(screen,(100,200,100),[150,250,800,200])         
#discard pile on screen
    pygame.draw.rect(screen,(0,0,0),[350,300,71,96],5)
    

 #stack on screen   
    pygame.draw.rect(screen,(0,0,0),[650,300,73,99])
    screen.blit(back,[650,300])
 
    presentallot()#allottment of present value
    while not done:
        
#draw card from stack
        
        mouse=pygame.mouse.get_pressed()
        if mouse[0]==True and take==True and myturn==True:
            x,y=pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]
            if 650<=x<=723 and 300<=y<=399:
                    drawcardstack()
                    pygame.display.update()
            elif 350<=x<=423 and 300<=y<=399:
                    drawcardpresent()
                    pygame.draw.rect(screen,(100,0,0),[350,300,71,96])
                    pygame.display.update()
            take=False
            discard=True
#return card to discard pile right side button
        
        mouse=pygame.mouse.get_pressed()
        if mouse[2]==True and discard==True and myturn==True:
            x,y=pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]
            dicard=False
            myturn=False
            
            if 20<=x<=91 and 600<=y<=696:
                returncard(0)
                shift(20,600,0)
            if 120<=x<=191 and 600<=y<=696:
                returncard(1)
                shift(120,600,1)
            if 220<=x<=291 and 600<=y<=696:
                returncard(2)
                shift(220,600,2)
            if 320<=x<=391 and 600<=y<=696:
                returncard(3)
                shift(320,600,3)
            if 420<=x<=491 and 600<=y<=696:
                returncard(4)
                shift(420,600,4)
            if 520<=x<=591 and 600<=y<=696:
                returncard(5)
                shift(520,600,5)
            if 620<=x<=691 and 600<=y<=696:
                returncard(6)
                shift(620,600,6)
            if 720<=x<=791 and 600<=y<=696:
                returncard(7)
                shift(720,600,7)
            if 820<=x<=891 and 600<=y<=696:
                returncard(8)
                shift(820,600,8)
            if 920<=x<=991 and 600<=y<=696:
                returncard(9)
                shift(920,600,9)
            if 1020<=x<=1091 and 600<=y<=696:
                returncard(10)
                shift(1020,600,10)
            compturn=True
           
#computer arrenges its cards and decides to pick present or not
        if compturn==True:
            #first a run has to be formed
            a,b=compcompare()
            compturn=False
            myturn=True
            take=True
            if a==1:
                    comppickpresent()
                    compreturn(b)
                    
            elif a==2:
                    comppickstack()
                    compreturn(b)
            elif a==3:
                showend(screen)
                done=True
            else:
                    comppickstack()
                    compreturn(b)


        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
             print("yayyyy")
             showend(screen)
             done=True
        pygame.display.update()
        
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        pygame.display.flip()
                
    pygame.quit()
    



