import random

class Card():
    
    def __init__(self,value,sign):
        self.value=value
        self.sign=sign

    def __str__(self):
        return "{}-{}".format(self.value, self.sign)

    def get_value(self):
        return self.value

class Deck():

    signs = ["heart" , "diamond" , "spade" , "clubs" ]
    special = ["A", "J", "Q", "K"]

    def __init__(self):

        self.deck=[]
        self.total=52
        
        for i in range(2,11,1):
            for j in Deck.signs:
                card = Card(i,j)
                self.deck.append(card)

        for i in Deck.special:
            for j in Deck.signs:
                card = Card(i, j)
                self.deck.append(card)

    def __str__(self):
        s=""
        for i in self.deck:
            s += " {} \n".format(i)

        return s

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.total-=1
        return self.deck.pop()

    def isEmpty(self):
        if(self.total==0):
            return False
        else: return True

class Player():

    def __init__(self, deck):
        self.deck = deck
        self.my_cards = []
        self.my_val = 0
        self.aces = 0
        self.my_chips = 100
        self.my_bet=0
        self.continuee=True

    def other_player(self, other):
        self.other = other
        
    def getCards(self):

        if(self.my_chips==0):
            self.continuee=False
        else:
            card = self.deck.deal()
            self.my_cards.append(card)
            
            if(card.get_value() in ["J", "Q" , "K" ]):
                self.my_val +=10
            elif(card.get_value() =="A"):
                self.my_val+=11
                self.aces+=1
            else:
                self.my_val += card.get_value()
                
            card = self.deck.deal()
            self.my_cards.append(card)
            
            if(card.get_value() in ["J", "Q" , "K" ]):
                self.my_val +=10
            elif(card.get_value() =="A"):
                self.my_val+=11
                self.aces+=1
            else:
                self.my_val += card.get_value()

            while self.my_val>21 and self.aces >0:
                self.my_val-=11
                self.my_val+=1
                self.aces -=1

            print("Your cards are:")
            for i in self.my_cards:
                print(i)
                
            while True:
                pom = input("How many chips do you bet? ")
                pom = int(pom)
                if(self.my_chips>=pom):
                    self.my_chips-=pom
                    self.my_bet = pom
                    break
        
    def getCard(self):
        card = self.deck.deal()
        self.my_cards.append(card)

        print("NOVA KARTA JE: {}".format(card))
        if(card.get_value() in ["J", "Q" , "K"]):
            self.my_val +=10
        elif(card.get_value() =="A"):
            self.my_val+=11
            self.aces+=1
        else:
            self.my_val += card.get_value()

        while self.my_val>21 and self.aces >0:
            self.my_val-=11
            self.my_val+=1
            self.aces -=1


    def want_more(self):
        odluka = ""
        blabla=""
        while(odluka!="N" and self.deck.isEmpty()):

            print("U RUCI IMAM {}".format(self.my_val))
            
            if(self.my_val>21):
                odluka="N"
                blabla="/"
            else:
                odluka = input("Do you want to continue? Press Y for YES and N for NO ")

                if(odluka=="Y"):
                    self.getCard()
                    pom = input("Would you like to raise?")
                    if(pom=="Y"):
                        while True:
                            pom = input("How many chips do you want to raise?")
                            pom = int(pom)
                            if(self.my_chips>=pom):
                                self.my_chips-=pom
                                self.my_bet = pom
                                break

            if(blabla!="/"):
                blabla=""
                print("Your cards are:")
                for i in self.my_cards:
                    print(i)

    def want_more_2(self):
        if(self.other==21):
            return "FIRST WON"
        elif(self.other>21):
            return "SECOND WON"
        
        odluka = ""
        blabla=""
        while(odluka!="N" and self.deck.isEmpty() and self.my_val<21 and (self.my_val<=self.other and self.my_val<21)):

            print("U RUCI IMAM {}".format(self.my_val))
            
            if(self.my_val>21):
                odluka="N"
                blabla="/"
            else:
                odluka = input("Do you want to continue? Press Y for YES and N for NO ")

                if(odluka=="Y"):
                    self.getCard()

            if(blabla!="/"):
                blabla=""
                print("Your cards are:")
                for i in self.my_cards:
                    print(i)

        pom = input("Would you like to raise?")
        if(pom=="Y"):
            while True:
                pom = input("How many chips do you want to raise?")
                pom = int(pom)
                if(self.my_chips>=pom):
                    self.my_chips-=pom
                    self.my_bet = pom
                    break
 
        if(self.my_val>21):
            return "FIRST WON"
        elif(self.my_val<=21 and self.my_val<self.other):
            return "FIRST WON"
        elif(self.my_val<=21 and self.my_val>self.other):
            return "SECOND WON"
        else:
            return "ILLEGAL"

class Dealer():

    def __init__(self, deck):
        self.deck = deck
        self.my_cards = []
        self.my_val = 0
        self.aces = 0
        self.players_val=0
        
    def getCards(self):
        card = self.deck.deal()
        self.my_cards.append(card)
        
        if(card.get_value() in ["J", "Q" , "K" ]):
            self.my_val +=10
        elif(card.get_value() =="A"):
            self.my_val+=11
            self.aces+=1
        else:
            self.my_val += card.get_value()
            
        card = self.deck.deal()
        self.my_cards.append(card)
        
        if(card.get_value() in ["J", "Q" , "K" ]):
            self.my_val +=10
        elif(card.get_value() =="A"):
            self.my_val+=11
            self.aces+=1
        else:
            self.my_val += card.get_value()

        while self.my_val>21 and self.aces >0:
            self.my_val-=11
            self.my_val+=1
            self.aces -=1

        print("One of dealers cards is {} ".format(self.my_cards[0]))
        
    def getCard(self):
        card = self.deck.deal()
        self.my_cards.append(card)

        #print("NOVA KARTA JE: {}".format(card))
        
        if(card.get_value() in ["J", "Q" , "K"]):
            self.my_val +=10
        elif(card.get_value() == "A"):
            self.my_val+=11
            self.aces+=1
        else:
            self.my_val += card.get_value()

        while self.my_val>21 and self.aces >0:
            self.my_val-=11
            self.my_val+=1
            self.aces -=1

    def players_value(self,val):
        self.players_val=val

    def want_more(self):

        if(self.players_val==21):
            return "PLAYER WON"
        elif(self.players_val>21):
            return "DEALER WON"
        
        while(self.my_val<21 and self.deck.isEmpty() and (self.my_val<=self.players_val and self.my_val<21)):

            if(self.my_val>21):
                break
            else:    
                self.getCard()
                print("Dealer has these cards:")
                for i in self.my_cards:
                    print(i)

        if(self.my_val>21):
            return "PLAYER WON"
        elif(self.my_val<=21 and self.my_val>self.players_val):
            return "DEALER WON"
        else:
            return "ILLEGAL"


d = Deck()
d.shuffle()
p = Player(d)
p1 = Player(d)
dealer = Dealer(d)

a = input("Do you want to play versus a person or versus a PC? A for person, B for PC ")
if(a=="B"):

    while(d.isEmpty() and p.continuee==True):

        print(d.total)
        
        dealer.getCards()
        p.getCards()

        p.want_more()
        igrac = p.my_val
        dealer.players_value(igrac)
        pom = dealer.want_more()
        print(pom)
        if (pom=="PLAYER WON"):
            p.my_chips+=(2*p.my_bet)
        
        p.my_cards=[]
        p.my_val=0
        p.my_bet=0
        p.aces=0
        dealer.my_cards=[]
        dealer.my_val=0
        dealer.aces=0
        dealer.players_val=0
        
        if(d.total<4):
            break
else:

    while(d.isEmpty() and p1.continuee==True and p.continuee==True ):

        print(d.total)
        
        p.getCards()

        p.want_more()
        igrac = p.my_val

        for i in range(38):
            print()
                
        p1.getCards()
        p1.other_player(igrac)

        if(igrac>21):
            p.my_cards=[]
            p.my_val=0
            p.my_bet=0
            p.aces=0
            p1.my_cards=[]
            p1.my_val=0
            p1.aces=0
            p1.players_val=0
            print("SECOND WON")
        else:

            
            pom = p1.want_more_2()
            print(pom)
            
            if (pom=="FIRST WON"):
                p.my_chips+=(p.my_bet+p1.my_bet)
            else:
                p1.my_chips+=(p.my_bet+p1.my_bet)
                
            p.my_cards=[]
            p.my_val=0
            p.my_bet=0
            p.aces=0
            p1.my_cards=[]
            p1.my_val=0
            p1.aces=0
            p1.players_val=0
        
        if(d.total<4):
            break

    
print("Kraj!")

    
        
        









    
        






        
