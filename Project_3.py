print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
choice1 = input("Yor're at a cross road. Where do you want to go? Type 'left' or 'right").lower()
if choice1 == "left":
 choice2 = input("You have come to a lake. There is a island in the middle of the lake. Type 'wait' to wait for a boat.Type 'swin' to swim across ").lower()
 if choice2 == "wait":
    choice3 = input("Which door? Red, Blue or Yellow.").lower()
    if choice3 == "yellow":
         print("You Win!")
    else:
         print("You chose the wrong gate.GAME OVER!")
 else: print("The CROC attacked you.GAME OVER")
else: print("You fell in the hole!GAME OVER")