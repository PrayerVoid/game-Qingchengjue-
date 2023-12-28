def getcard(leftcards,handcards):
    if not(leftcards):
        return
    handcards.append(leftcards.pop())
    return

from random import randint
class card1:
    def __init__(self):
        self.name='落红尘'
        self.mp=1
        self.able='消耗1行动力，失去两点生命，获得五点护甲'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        HP1-=2
        LP1+=5
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)


class card2:
    def __init__(self):
        self.name='花间舞'
        self.mp=1
        self.able='消耗1行动力，抽两张牌'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        getcard(myleftcards,myhandcards)
        getcard(myleftcards,myhandcards)
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)


class card3:
    def __init__(self):
        self.name='林中风'
        self.mp=0
        self.able='不消耗行动力，获得等于自己当前行动力的护甲(至少获得一点护甲)'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        LP1+=MP1
        if MP1==0:
            LP1+=1
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)

class card4:
    def __init__(self):
        self.name='若无意'
        self.mp=2
        self.able='消耗2点行动力，对方失去2点生命，你自己的护甲翻倍'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=2
        LP1*=2
        HP2-=2
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)

class card5:
    def __init__(self):
        self.name='总相逢'
        self.mp=0
        self.able='清空你的行动力，每1点行动力造成3点伤害(至少造成3点伤害)'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1=max(MP1,1)
        if LP2>3*MP1:
            LP2-=MP1
        else:
            HP2-=(3*MP1-LP2)
            LP2=0    
        MP1=0
        myhandcards.remove(self)       
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card6:
    def __init__(self):
        self.name='斩'
        self.mp=1
        self.able='消耗一点行动力，造成3点伤害'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        if LP2>3:
            LP2-=3
        else:
            HP2-=(3-LP2)
            LP2=0     
        myhandcards.remove(self)      
        return (HP1,MP1,LP1,HP2,MP2,LP2)

class card7:
    def __init__(self):
        self.name='伤'
        self.mp=1
        self.able='消耗1点行动力，失去3点生命，造成5点伤害'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        HP1-=3
        if LP2>5:
            LP2-=5
        else:
            HP2-=(5-LP2)
            LP2=0       
        myhandcards.remove(self)    
        return (HP1,MP1,LP1,HP2,MP2,LP2)

class card8:
    def __init__(self):
        self.name='影'
        self.mp=1
        self.able='消耗1点行动力，获得1点行动力，如果对方护甲>0则你额外获得1点行动力'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        if LP2>0:
            MP1+=1
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)

class card9:
    def __init__(self):
        self.name='疾'
        self.mp=1
        self.able='消耗1点行动力，抽一张牌，获得2点护甲'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        LP1+=2
        getcard(myleftcards,myhandcards)
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)

class card10:
    def __init__(self):
        self.name='破'
        self.mp=2
        self.able='消耗2点行动力，造成你已损生命值五分之一（向上取整）的伤害，若未能破甲则随机弃置对方一张手牌'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=2
        hurt=(54-HP1)//5
        if LP2>=hurt:
            if itshandcards:
              s=randint(0,len(itshandcards)-1)
              itshandcards.pop(s)
            LP2-=hurt
        else:
            HP2-=(hurt-LP2)
            LP2=0
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)

class card11:
    def __init__(self):
        self.name='扶摇直上'
        self.mp=1
        self.able='消耗1点行动力，回复3点生命，过量回复的转变为造成伤害'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        HP1+=3
        if HP1>25:
            delta=HP1-25
            HP1=25
            if LP2>delta:
                LP2-=delta
            else:
                HP2-=(delta-LP2)
                LP2=0
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)

class card12:
    def __init__(self):
        self.name='长风破浪'
        self.mp=2
        self.able='消耗2点行动力，抽2张牌，造成3点伤害'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=2
        getcard(myleftcards,myhandcards)
        getcard(myleftcards,myhandcards)
        if LP2>3:
            LP2-=3
        else:
            HP2-=(3-LP2)
            LP2=0
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)

class card13:
    def __init__(self):
        self.name='飞流直下'
        self.mp=0
        self.able='不消耗行动力，获得等同于你行动力的护甲，抽一张牌'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        LP1+=MP1
        getcard(myleftcards,myhandcards)
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)

class card14:
    def __init__(self):
        self.name='直上青云'
        self.mp=1
        self.able='消耗1点行动力，随机造成1~6点伤害'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        s=randint(1,6)
        if LP2>s:
            LP2-=s
        else:
            HP2-=(s-LP2)
            LP2=0
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)

class card15:
    def __init__(self):
        self.name='九天揽月'
        self.mp=1
        self.able='消耗1点行动力，随机产生战青云的另一种牌的效果（不额外消耗行动力）'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):        
        MP1-=1
        MPnow=MP1
        t=randint(0,3)
        rand=[card11(),card12(),card13(),card14()]
        myhandcards.append(rand[t])
        HP1,MP1,LP1,HP2,MP2,LP2=rand[t].ability(myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2)
        MP1=MPnow
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card16:
    def __init__(self):
        self.name='一筒'
        self.mp=1
        self.num=1
        self.able='消耗1点行动力，抽一张牌，再随机获得一张雀儿的牌，然后(杠-对方失10生命，吃-5点伤害，碰-得6护甲)'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        myhandcards.remove(self)
        getcard(myleftcards,myhandcards)
        st=randint(0,4)
        cc=[card16(),card17(),card18(),card19(),card20()]
        myhandcards.append(cc[st])
        myhandcards.sort(key=lambda x:x.num)
        if len(myhandcards)>3:
            for i in range(len(myhandcards)-3):
                if myhandcards[i].num==myhandcards[i+1].num==myhandcards[i+2].num==myhandcards[i+3].num:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    HP2-=10
                    break
        if len(myhandcards)>2:
            for i in range(len(myhandcards)-2):
                if myhandcards[i].num==myhandcards[i+1].num-1==myhandcards[i+2].num-2:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    if LP2>=5:
                        LP2-=5
                    else:
                        HP2-=(5-LP2)
                        LP2=0
                    break
            for i in range(len(myhandcards)-2):
                if myhandcards[i].num==myhandcards[i+1].num==myhandcards[i+2].num:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    LP1+=6
                    break
            
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card17:
    def __init__(self):
        self.name='二筒'
        self.mp=1
        self.num=2
        self.able='消耗1点行动力，抽一张牌，再随机获得一张雀儿的牌，然后(杠-对方失10生命，吃-5点伤害，碰-得6护甲)'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        myhandcards.remove(self)
        getcard(myleftcards,myhandcards)
        st=randint(0,4)
        cc=[card16(),card17(),card18(),card19(),card20()]
        myhandcards.append(cc[st])
        myhandcards.sort(key=lambda x:x.num)
        if len(myhandcards)>3:
            for i in range(len(myhandcards)-3):
                if myhandcards[i].num==myhandcards[i+1].num==myhandcards[i+2].num==myhandcards[i+3].num:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    HP2-=10
                    break
        if len(myhandcards)>2:
            for i in range(len(myhandcards)-2):
                if myhandcards[i].num==myhandcards[i+1].num-1==myhandcards[i+2].num-2:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    if LP2>=5:
                        LP2-=5
                    else:
                        HP2-=(5-LP2)
                        LP2=0
                    break
            for i in range(len(myhandcards)-2):
                if myhandcards[i].num==myhandcards[i+1].num==myhandcards[i+2].num:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    LP1+=6
                    break
            
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card18:
    def __init__(self):
        self.name='三筒'
        self.mp=1
        self.num=3
        self.able='消耗1点行动力，抽一张牌，再随机获得一张雀儿的牌，然后(杠-对方失10生命，吃-5点伤害，碰-得6护甲)'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        myhandcards.remove(self)
        getcard(myleftcards,myhandcards)
        st=randint(0,4)
        cc=[card16(),card17(),card18(),card19(),card20()]
        myhandcards.append(cc[st])
        myhandcards.sort(key=lambda x:x.num)
        if len(myhandcards)>3:
            for i in range(len(myhandcards)-3):
                if myhandcards[i].num==myhandcards[i+1].num==myhandcards[i+2].num==myhandcards[i+3].num:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    HP2-=10
                    break
        if len(myhandcards)>2:
            for i in range(len(myhandcards)-2):
                if myhandcards[i].num==myhandcards[i+1].num-1==myhandcards[i+2].num-2:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    if LP2>=5:
                        LP2-=5
                    else:
                        HP2-=(5-LP2)
                        LP2=0
                    break
            for i in range(len(myhandcards)-2):
                if myhandcards[i].num==myhandcards[i+1].num==myhandcards[i+2].num:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    LP1+=6
                    break
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card19:
    def __init__(self):
        self.name='四筒'
        self.mp=1
        self.num=4
        self.able='消耗1点行动力，抽一张牌，再随机获得一张雀儿的牌，然后(杠-对方失10生命，吃-5点伤害，碰-得6护甲)'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        myhandcards.remove(self)
        getcard(myleftcards,myhandcards)
        st=randint(0,4)
        cc=[card16(),card17(),card18(),card19(),card20()]
        myhandcards.append(cc[st])
        myhandcards.sort(key=lambda x:x.num)
        if len(myhandcards)>3:
            for i in range(len(myhandcards)-3):
                if myhandcards[i].num==myhandcards[i+1].num==myhandcards[i+2].num==myhandcards[i+3].num:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    HP2-=10
                    break
        if len(myhandcards)>2:
            for i in range(len(myhandcards)-2):
                if myhandcards[i].num==myhandcards[i+1].num-1==myhandcards[i+2].num-2:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    if LP2>=5:
                        LP2-=5
                    else:
                        HP2-=(5-LP2)
                        LP2=0
                    break
            for i in range(len(myhandcards)-2):
                if myhandcards[i].num==myhandcards[i+1].num==myhandcards[i+2].num:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    LP1+=6
                    break
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card20:
    def __init__(self):
        self.name='五筒'
        self.mp=1
        self.num=5
        self.able='消耗1点行动力，抽一张牌，再随机获得一张雀儿的牌，然后(杠-对方失10生命，吃-5点伤害，碰-得6护甲)'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        myhandcards.remove(self)
        getcard(myleftcards,myhandcards)
        st=randint(0,4)
        cc=[card16(),card17(),card18(),card19(),card20()]
        myhandcards.append(cc[st])
        myhandcards.sort(key=lambda x:x.num)
        if len(myhandcards)>3:
            for i in range(len(myhandcards)-3):
                if myhandcards[i].num==myhandcards[i+1].num==myhandcards[i+2].num==myhandcards[i+3].num:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    HP2-=10
                    break
        if len(myhandcards)>2:
            for i in range(len(myhandcards)-2):
                if myhandcards[i].num==myhandcards[i+1].num-1==myhandcards[i+2].num-2:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    if LP2>=5:
                        LP2-=5
                    else:
                        HP2-=(5-LP2)
                        LP2=0
                    break
            for i in range(len(myhandcards)-2):
                if myhandcards[i].num==myhandcards[i+1].num==myhandcards[i+2].num:
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    myhandcards.pop(i)
                    LP1+=6
                    break
        return (HP1,MP1,LP1,HP2,MP2,LP2)

times=0  
class card21:
    def __init__(self):
        self.name='九尾'
        self.mp=1
        global times
        self.able='消耗1行动力，若该牌已打出至少9次，造成9点伤害，否则抽一张牌，获得1行动力（当前已打出'+str(times)+'次）'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        global times
        self.able='消耗1行动力，若该牌已打出至少9次，造成9点伤害，否则抽一张牌，获得1行动力（当前已打出'+str(times)+'次）'
        if times!=9:
            times+=1
            getcard(myleftcards,myhandcards)
            MP1+=1
        else:
            if LP2>9:
                LP2-=9
            else:
                HP2-=(9-LP2)
                LP2=0
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card22:
    def __init__(self):
        self.name='白狐'
        self.mp=1
        self.able='消耗1行动力，将牌堆中随机一张牌变成《九尾》，抽一张牌'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1 
        if myleftcards:
            s=randint(0,len(myleftcards)-1)
            myleftcards[s]=card21()
        getcard(myleftcards,myhandcards)
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card23:
    def __init__(self):
        self.name='魅惑'
        self.mp=0
        self.able='不消耗行动力，随机将对方一张手牌放回牌堆'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        if itshandcards:
            s=randint(0,len(itshandcards)-1)
            itsleftcards.append(itshandcards.pop(s))
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card24:
    def __init__(self):
        self.name='舔舐'
        self.mp=0
        self.able='不消耗行动力，双方各获得3点护甲'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        LP1+=3
        LP2+=3
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card25:
    def __init__(self):
        self.name='玉焚'
        self.mp=2
        self.able='消耗2行动力，敌方生命值减少五分之一（向下取整）'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=2
        hurt=HP2//5
        HP2-=hurt
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card26:
    def __init__(self):
        self.name='华山剑法'
        self.mp=0
        self.able='不消耗行动力，将你的护甲清零，并对对方造成等量伤害（清除负护甲则会令对方获得等量护甲）'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        if LP2>=LP1:
            LP2-=LP1
        else:
            HP2-=(LP1-LP2)
            LP2=0
        LP1=0
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card27:
    def __init__(self):
        self.name='泰山剑法'
        self.mp=1
        self.able='消耗1行动力，失去2点护甲（护甲可以为负），造成3点伤害'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        LP1-=2
        if LP2>=3:
            LP2-=3
        else:
            HP2-=(3-LP2)
            LP2=0
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card28:
    def __init__(self):
        self.name='嵩山剑法'
        self.mp=1
        self.able='消耗1行动力，获得对方生命值五分之一（向上取整）的护甲'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=1
        LP1+=(HP2+4)//5
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card29:
    def __init__(self):
        self.name='恒山剑法'
        self.mp=2
        self.able='消耗2点行动力，对对方造成2x点伤害（x为对方当前的护甲且至多为6，若x为负数则反而会增加对方护甲）'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        MP1-=2
        hurt=min(2*LP2,12)
        if LP2>hurt:
            LP2-=hurt
        else:
            HP2-=(hurt-LP2)
            LP2=0
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
class card30:
    def __init__(self):
        self.name='衡山剑法'
        self.mp=0
        self.able='不消耗行动力，抽等于你当前行动力数量的牌，然后失去等量护甲（护甲可以为负）'
    def ability(self,myhandcards,myleftcards,itshandcards,itsleftcards,HP1,MP1,LP1,HP2,MP2,LP2):
        LP1-=MP1
        for i in range(MP1):
            getcard(myleftcards,myhandcards)
        myhandcards.remove(self)
        return (HP1,MP1,LP1,HP2,MP2,LP2)
    
