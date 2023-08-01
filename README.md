# #Treasure hunt game.py

Language: PYTHON3

Hello, folks, welcome to another fun project! In this, you will learn how to make a
text-based Treasure Hunt adventure game in python3 using functions. 

A Treasure hunt game in which each person or team attempts to be first in finding something that has been hidden, using written directions or clues.
      
![image](https://miro.medium.com/v2/resize:fit:828/format:webp/1*wFVgskxviCjI0QIoJwY6Ig.jpeg)

Pre-Requisite:

    1. Python Installed
    2. Python Knowledge(if-else)


MAPING IMAGE

![image](https://i.imgur.com/llAJ1g4.png)

another! we start adventure game. Then tell the player a
story like "You are on a dirt road. it has come to an end, and you  can go left or right.which way would you like to go? (l or r)". takes 'l'
you come to a river.you can wolk around it or swim across.type swim to swim across and wolk around, If you take swim eaten by  alligator (or)
takes right,walk around you may go to stranger. He give a gold , you win!

SOURCE CODE:

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
                    print("not a valid option. you lose.")
               else:
                    print("not a valid option.you lose.")
       print("If lose game" ,'retry')
       
OUTPUT:

If you take right choise, In right way have been save & you win! Game.

     type your name:jon
     welcome jon to this adventure!
     you are on a dirt road. it has come to an end, and you  can go left or right.which way would you like to go?right
     you come to a bridge. It looks wobbly,do you want to cross it or head back (cross/back)?: cross
     you cross the  bridge and you meet a stranger,do you talk to them?(yes/no)?:yes
     you talked to the stranger and they give you gold. YOU WIN!

If does'nt take right decision,in right path you lose same like output.

    type your name:dileep
    welcome dileep to this adventure!
    you are on a dirt road. it has come to an end, and you  can go left or right.which way would you like to go?left
    you come to a river.you can wolk around it or swim across.type swim to swim across and wolk around:swim
    you swim across the river and get eaten by an alligator.





