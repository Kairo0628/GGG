# 하나의 클래스, 사람 대 컴퓨터, 트럼프 카드, 공격, 수비, 카드 뽑기, 카드 다시 섞기, 조커 카드

import random

class OneCard:
  def __init__(self):
    self.CreateGame()

    print("게임 시작 !")
    print("\n")
    
    while self.End():
      self.Every_turn()

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
    self.field = []

    for i in range(7):
      self.DrawP()
      self.DrawC()
    self.field.append(self.deck.pop())

  def DrawP(self):
    self.pHand.append(self.deck.pop())

  def DrawC(self):
    self.cHand.append(self.deck.pop())

  def Show_field(self):
    print(f"현재 필드 : {self.field[-1]}")

  def End(self):
    if len(self.cHand) == 0:
      print("컴퓨터의 승리 ㅜ_ㅜ")
      return False
    elif len(self.pHand) == 0:
      print("당신의 승리!")
      return False
    else:
      return True

  def Can_play(self, hand):
    can_play = []
    for i in hand:
      if self.field[-1][0] == i[0]:
        can_play.append(i)
      elif self.field[-1][1] == i[1]:
        can_play.append(i)
    
    return can_play
  
  def Every_turn(self):
    print("컴퓨터의 차례")
    self.Show_field()

    cPlay = self.Can_play(self.cHand)
    if len(cPlay) == 0:
      self.cHand.append(self.deck.pop())
      print("컴퓨터가 낼 카드가 없어 한장 뽑습니다.")
    else:
      select = random.randint(0, len(cPlay))
      print(f"컴퓨터가 {self.cHand[select]}를 냈습니다.")
      self.field.append(self.cHand.pop(select))
    print(f"남은 컴퓨터의 카드 : {len(self.cHand)}")
    print("\n")

    print("당신의 차례")
    self.Show_field()
    print(f"당신의 패 : {self.pHand}")

    pPlay = self.Can_play(self.pHand)
    if len(pPlay) == 0:
      self.pHand.append(self.deck.pop())
      print("낼 카드가 없어 한장 뽑습니다.")
    else:
      print(f"낼 수 있는 카드 : {pPlay}")
      select = int(input("낼 카드를 고르시오 : "))
      print(f"{self.pHand[select - 1]}을 냈습니다.")
      self.field.append(self.pHand.pop(select - 1))
    print(f"당신의 남은 카드 : {len(self.pHand)}")
    print("\n")
 
OneCard()