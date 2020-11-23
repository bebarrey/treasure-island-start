print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

path = input("You have entered the great dragon chrythem's lair.There are two paths in front of you.Choose left or right to continue.Left or Right?\n")
path_l = path.lower()
if path_l == "left":
  swim = input("Wise Decision. Continue on the path. Wait there seems to a river of some sort. Do you want to swim across and redeem your luck? Or, wait to think of your options? Swim or Wait?\n")
  swim_l = swim.lower()
  if swim_l == "wait":
    door = input("What luck! You spotted a log that connects both river banks.You have easily crossed the river. There are three doors around the corner.Which one will you open?Red, Yellow, or Blue?\n")
    door_l = door.lower()
    if door_l == "yellow":
      print("You made it. You found Solomon's Chest. Good fortune begins now. Enjoy.")
    elif door_l == "red":
      print("The dragon found your scent and followed you. You are toast.")
    else:
      print("This is the end. You are lost in the blackhole and can't escape.Good bye.")    
  else:
    print("You are swimming well. But, the river is unforgiving. You hit the river bottom and can't escape.")

else:
  print("Oh no! You have encountered the great dragon and turned to ashes.")  
