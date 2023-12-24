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