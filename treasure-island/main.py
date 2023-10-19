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

horizontal_direction = input('You are on a cross road. Where do you want to go? Type "left" or "right"')
if(horizontal_direction.lower() == "right"):
  print("Fall into a hole. Game Over")
elif(horizontal_direction.lower() == "left"):
  swimOrWait = input('You come to lake. There is an island in the middle of the lake. Type "wait" to wait a boat. Type to "swim" a lake')
  if(swimOrWait.lower() == "swim"):
    print("Attacked by trout.Game Over.")
  elif(swimOrWait.lower() == "wait"):
    door = input('You arriwed on an island unharmed. Choose a door to get into. Red, yellow, or green?')
    if(door.lower() == "red"):
      print("Burned by fire.Game Over.")
    elif(door.lower() == "yellow"):
      print("Eaten by beasts.Game Over.")
    elif(door.lower() == "green"):
      print("You won!")
    else:
      exit()
  else:
    exit()
else:
  exit()


