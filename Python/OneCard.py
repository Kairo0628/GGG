# 하나의 클래스, 사람 대 컴퓨터, 트럼프 카드, 공격, 수비, 카드 뽑기, 카드 다시 섞기, 조커 카드

import random

class OneCard:
  def __init__(self):
    self.CreateGame()
    self.Start()

  def CreateGame(self):
    self.deck = []
    
    for i in range(1, 14):
      for j in ['♠', '♥', '♣', '◆']:
        if i == 1:
          self.deck.append((j, 'A'))
        elif i == 11:
          self.deck.append((j, 'J'))
        elif i == 12:
          self.deck.append((j, 'Q'))
        elif i == 13:
          self.deck.append((j, 'K'))
        else:
          self.deck.append((j, i))
    
    random.shuffle(self.deck)

    self.pHand = []
    self.cHand = []

    for i in range(7):
      self.DrawP()
      self.DrawC()

  def DrawP(self):
    self.pHand.append(self.deck.pop())

  def DrawC(self):
    self.cHand.append(self.deck.pop())
  
  
  def Start(self):

    print(self.deck)
    print(self.pHand)


 
OneCard()