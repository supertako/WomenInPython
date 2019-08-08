# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:12:44 2019

@author: tseng
"""

# The Basics

'''
Data Types --> string int
Variable
operators symbols ---> =, ==, !=, <=, >=, <, >, and, or, not  
Class
object
list
For loop
while loop
if else statement

'''

# build blackjack Card Game

suits_name = ['Spades', 'Hearts','Diamonds', 'Clubs']
suits_symbols = ['♠','♥','♦','♣']
suits = ['\u2660','\u2665','\u2666','\u2663']

# setup Playing cards

class Card:

    card_values = {
        'A': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10,'K': 10
    }
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.points = self.card_values[rank]
        
    def printCard(self):
        return self.rank + self.suit
    
    def getCardValue(self):
        return self.card_values[self.rank]

suits = ['\u2660','\u2665','\u2666','\u2663']
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = []
    
# Create and populate 1 deck of cards
for s in suits:
    for r in ranks:
        card = Card(s, r)
        deck.append(card)

''' 
for i in range(len(suits)):
    for j in range(len(ranks)):
        card = Card(suits[i], ranks[j])
        deck.append(card)
'''

# checking if the cards are created correctly by print out
def showCardList(cardlist):
    for i in range(len(cardlist)):
        if (i+1) % 13 != 0:           
            print(cardlist[i].printCard(), end='')
        else:
            print(cardlist[i].printCard())

#showCardList(deck)

deck = 5*deck
totalCards = len(deck)

# Shuffle Cards
import random
# Shuffle Cards
def shuffleCards(CardDeck):
    for i in range(totalCards): # 要交换的数量
        rCardPos1 = random.randint(0, totalCards-1) #生成第一个随机位置 （用于deck列表的位置）
        rCardPos2 = random.randint(0, totalCards-1) #生成第二个随机位置 （用于deck列表的位置）
        temp = CardDeck[rCardPos1] #创造一个临时变量 来保存第一个随机挑选的卡牌
        CardDeck[rCardPos1] = CardDeck[rCardPos2] #deck列表的第一个随机 现在可以被第二个随机位取代
        CardDeck[rCardPos2] = temp #deck列表的第二个随机位 现在可以被 临时保存的第一个随机卡牌取代
            
    return CardDeck;

deck = shuffleCards(deck)
#showCardList(deck)

# game logic

''' Initialize the variables we need 初始化我们需要的变量 '''
PlayerHand = []
DealerHand = []

cardIndex = 0 #deck中发牌之后的位置
playertotal = 0
dealertotal = 0

# initial round dealer get 1 card player get 2 cards
# every time draw a card cardIndex increase by 1
''' 第一局我们可以固定发牌顺序 '''
PlayerHand.append(deck[cardIndex])
cardIndex += 1 # 每发一次牌 deck中的牌位就会加 1 
DealerHand.append(deck[cardIndex])
cardIndex += 1
PlayerHand.append(deck[cardIndex])
cardIndex += 1

''' 自定义功能函数 将列表中的卡牌相加 '''
def sumUp(list1):
    total = 0
    list1.sort(key=lambda x: x.points) # 利用排序功能 排序小到大 
    list1.reverse() # 相反功能 排序大到小
    for i in list1:
        if total < 11 and i.rank=='A': # 卡片 ‘A’ 可为 1 或 11
            total += i.getCardValue()+10
        else:
            total += i.getCardValue()
        
    return total

''' 自定义功能函数 将列表中的卡牌l列印出来 '''
def showHand(cardlist):
    total = 0
    for card in cardlist:
        if total < 11 and card.rank=='A':
            total += card.getCardValue()+10
        else:
            total += card.getCardValue()
        print(card.printCard() + " ", end='')
     
    print("\t--> " + str(total))

print('Dealer: ',end='')
showHand(DealerHand)
print('Player: ',end='')
showHand(PlayerHand)

userCall = input("Hit or Stay: ")

''' 当玩家没有输入’STAY‘ 就持续循环，输入hit就发一张牌给Player'''
while userCall.upper() != "STAY":
    if userCall.upper() == "HIT": # 发一张牌给Player
        PlayerHand.append(deck[cardIndex])
        cardIndex += 1
    
    playertotal = sumUp(PlayerHand)
    if playertotal > 21: #如果Player列表的牌超过21，那就爆了
        print("Player busted at " + str(playertotal) + " !!!! Dealer Wins")
        break
    
    print('Player: ', end='')
    showHand(PlayerHand)
    userCall = input("Hit or Stay: ") # 再次问player是否要牌 （防止无限循环）

''' 当庄家的点数没有到大于等于17 就持续循环 '''
while dealertotal < 17:
    DealerHand.append(deck[cardIndex])# 发一张票给庄家
    cardIndex += 1
    print('Dealer: ', end='')
    showHand(DealerHand)
    dealertotal = sumUp(DealerHand)
    if dealertotal > 21: #如果点数超过21 那就爆了
        if playertotal <= 21:
            print("Dealer busted at " + str(dealertotal) + " !!!! Player Wins")
        break

''' 如果玩家和庄家的点数都在21之内: 那就要对比谁比较大'''
if playertotal <= 21 and dealertotal <= 21:
    if playertotal > dealertotal:
        print("Player Win")
    elif playertotal < dealertotal:
        print("Player lose")
    else:
        print("Dealer: "+str(dealertotal)+ " Player: "+ str(playertotal) +" --->Draw")


''' Future Upgrades examples (Food for thoughts)

1） 让玩家可以选择持续玩下一局
   Let player have the option to continue playing the game
2） 模拟10000局，算出输赢的比例，拿到21的几率，达到两种相同的牌的概率
   Simulate 10000 rounds, calculate the winning rate, the rate of geting 21, the rate of getting a pair
3） Multiple players 多个玩家
4） Bargaining chips 筹码
5） 第一局的时候玩家直接拿到21点，庄家拿到'A'时，是否可以选择even money直接赢 | 
   when player get 21 in the 1st round, dealer got an 'A'. player should have the option to choose even money
   第一局的时候玩家直接拿到21点，直接赢1.5倍 |
   when player get 21 in the 1st round, win the round with 1.5 times the bet
6） 当玩家拿到两张相同的牌 是否可以split | Option to split if player got a pair
7） 提升算法效率 | making algorithm more efficent
'''
