# 파이썬 원카드

# 공격, 수비, 조커, 등등

import random

class OneCard:
  def __init__(self):
    self.Create_game()
    
    print("게임 시작 !")
    print("\n")

    self.Every_turn()

  def Create_game(self):
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

  def Can_play(self, hand):
    can_play = []
    for i in hand:
      if i[0] == self.field[-1][0]:
        can_play.append(i)
      elif i[1] == self.field[-1][1]:
        can_play.append(i)

    return can_play

  def Every_turn(self):
    while True:
      try:
        print("컴퓨터의 차례입니다.")
        self.Show_field()
        cPlay = self.Can_play(self.cHand)
        if len(cPlay) == 0:
          print("컴퓨터가 낼 카드가 없어 한장 뽑습니다.")
          self.DrawC()
        else:
          select = random.randrange(1, len(cPlay) + 1)
          selected = cPlay[select - 1]
          self.cHand.remove(selected)
          self.field.append(selected)
          print(f"컴퓨터가 {selected}를 냈습니다.")
        print(f"남은 컴퓨터의 카드 수 : {len(self.cHand)}")
        print("\n")

        if len(self.cHand) == 0:
          print("컴퓨터의 승리! ㅜ_ㅜ")
          break

        print("플레이어의 차례입니다.")
        self.Show_field()
        print(f"당신의 패 : {self.pHand}")
        pPlay = self.Can_play(self.pHand)
        if len(pPlay) == 0:
          print("플레이어가 낼 카드가 없어 한장 뽑습니다.")
          self.DrawP()
        else:
          print(f"낼 수 있는 카드 : {pPlay}")
          select = int(input("낼 카드를 선택하세요 : "))
          selected = pPlay[select - 1]
          self.pHand.remove(selected)
          self.field.append(selected)
          print(f"플레이어가 {selected}를 냈습니다.")
        print(f"남은 플레이어의 카드 수 : {len(self.pHand)}")
        print("\n")

        if len(self.pHand) == 0:
          print("플레이어의 승리 !")
          break
          
      except:
        print("\n")
        print("덱을 섞는 중...")
        print("\n")
        temp = self.field.pop()
        self.deck = self.field
        random.shuffle(self.deck)
        self.field.append(temp)

OneCard()