import random
p1=0
p2=0
while True:
  pl1=int(input("Press 1 to throw Dice (player 1): "))
  if pl1==1:
   Dice=random.randint(1,6)
   p1=p1+Dice
   print(f"Player 1 Position is {p1}")
  if(p1>=100):
    print("Player 1 Won")
    break
  pl2=int(input("Press 1 to throw Dice (player 2): "))
  if pl2==1:
    Dice2=random.randint(1,6)
    p2=p2+Dice2
    print(f"Player 2 Position is {p2}")
  if(p2>=100):
    print("Player 2 Won")
    break
