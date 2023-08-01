name = input("type your name:")
print("welcome",name,"to this adventure!")

answer=input(" you are on a dirt road. it has come to an end, and you  can go left or right.which way would you like to go?").lower()

if  answer == "left":
     answer = input("you come to a river.you can wolk around it or swim across.type swim to swim across and wolk around:").lower()
     
     if answer =="swim":
          print("you swim across the river and get eaten by an alligator.")
     elif answer =="wolk":
          print("you wolked for mony miles and you ran out water .you lose!")
     else:
          print("not a valid option you lose.")

elif answer == "right":
     answer = input("you come to a bridge. It looks wobbly,do you want to cross it or head back (cross/back)?: ")
    
     if answer == "back":
          print("you go back and lose.")
     elif answer == "cross":
        answer =input("you cross the  bridge and you meet a stranger,do you talk to them?(yes/no)?:")
     
        if answer =="yes":
            print("you talked to the stranger and they give you gold. YOU WIN!")
        elif answer == "no":
            print("not a valid option. yu lose.")


else:
    print("not a valid option.you lose.")


