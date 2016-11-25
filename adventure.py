# An adventure game

Bosshealth = 50
health = 100

from random import randint

def room1():
    global health
    
    print("Hello player!What is your name?")
    name = input("Name: ")
    print("Well,Welcome", name)
    print("Would you like to venture out into the land?")
    answer = input("Yes? or No?: ")
    if answer.lower() == "yes":
        print("You are now carrying your weapons and shield.")
        room2()
    else:
        print("You choose to walk to the castle for quest")
        print("""*                |>>>                    +
+          *                      |                   *       +
                    |>>>      _  _|_  _   *     |>>>
           *        |        |;| |;| |;|        |                 *
     +          _  _|_  _    \\.    .  /    _  _|_  _       +
 *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|
               \\..      /    ||:+++. |    \\.    .  /           *
      +         \\.  ,  /     ||:+++  |     \\:  .  /
                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *
          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +
                 ||+++ ||.    .     .      . ||+++.|   *
+   *            ||: . ||:.     . .   .  ,   ||:   |               *
         *       ||:   ||:  ,     +       .  ||: , |      +
  *              ||:   ||:.     +++++      . ||:   |         *
     +           ||:   ||.     +++++++  .    ||: . |    +
           +     ||: . ||: ,   +++++++ .  .  ||:   |             +
                 ||: . ||: ,   +++++++ .  .  ||:   |        *
                 ||: . ||: ,   +++++++ .  .  ||:   |                   """)
        answer = input("""The King ask'do you want to marry my daughter or do you want to go kill dragon?
                       1? or 2?: """)
        if answer.lower() == "2":
            room2()
        else:
            print("You live happyily ever after and have baby with your beautiful wife!The End!")
            print("""````´´¶¶¶¶¶¶¶¶´´´´´´Sweet
                    ´´´´´¶¶¶¢¢¢¢¶¶¶´´´´´
                    ´´´´1¶¶¢¢¢¢¢¢¶¶´´´´´
                    ´´´´¶¶¢¢¢¢¢¢¢¶1´´´´´Caring
                    ´´´´¶¢¢¢¢¢¢¢¢¶¶´´´´´
                    ´´´¶¶¢¢¢¢¢¢¢¢¢¶´´´´´
                    ´´1¶¢¢¢¢¢¢¢¢¢1´´´´´´Naughty
                    ´´7¶¢¢¢¢¢¢¢¢¢¶¶¶´´´´
                    ´´´¶¢¢¢¢¢¢¢¢¢¢¢¶¶´´´
                    ´´¶¶¶¶¶¶¢¢¢¢¢¢¢¶¶´´´$3X!
                    ´1¶¶¶´´¶¶¢¢¢¢¢¶¶´´´´
                    ´¶¶¶´´´´¶¶¢¢¢¢¶7´´´´
                    7¶¢¢1´´´´¶¢¢¢¢¶´´´´´Inteligent
                    ´¶¶¶¶¶¶¶¢¢¢¢1¶¢´´´´´
                    ´´´´´´1¢¢¢¢¢¢¶7´´´´´
                    ´´´´´¢¢¢1111¢¶´´´´´´Loving
                    ´´´´¶¶¢¢1111¶¶´´´´´´
                    ´´´1¶¢111111¶´´´´´´´
                    ´´´´¶¢111111¶´´´´´´´Loyal
                    ´´´´¶¢111111¶´´´´´´´
                    ´´´´1¶111111¶´´´´´´´
                    ´´´´´¶¢1111¢¶´´´´´´´Reliable
                    ´´´´´´¶1111¶¢´´´´´´´
                    ´´´´´´¶1111¶´´´´´´´´
                    ´´´´´´¶¢111¶7´´´´´´´Freaky
                    ´´´´´´¶1111¶¢´´´´´´´
                    ´´´´´1¶¢111¢¶´´´´´´´
                    ´´´´´¶¢1111¢¶´´´´´´´Humuorus
                    ´´´´¢¶¢¢¢¢¢¢¢´´´´´´´
                    ´´´´¶¢¢¢¢¢¢¢¶´´´´´´´
                    ´´´´¶¢¢¢¢¢¢¢¶´´´´´´´Dependable
                    ´´´´¢¶¢¶1¶¶¢¶¶´´´´´´
                    ´´´´´¶¢¶´´¶¶¢¶´´´´´´
                    ´´´´´¶¢¶´´´¶¢¶¢´´´´´Trendy
                    ´´´´´¶¢¶7´´1¶¶¶´´´´´
                    ´´´´´¶¢¶1´´´1¶¶¶´´´´
                    ´´´7¶¶¢¶¶´´´´¶¢¶¶´´´Beautiful
                    ´´´´¶¶¢¢¶´´´¶¶¢¢¶¶´´
                    ´´´´¶¶¢¶¶¶7´´¶¶¢¢¶´´""")

def dragon_fight():
    global health, Bosshealth

    

    while health >= 0 and Bosshealth >= 0:
        attack = randint(1, 50)
        dodge = randint(1, 2)

        if dodge == 1:
            print("You dodge the dragon's fire breath") 
        else:
            print("The dragon burns you with his dingleroot")
            health = health - randint(25, 50)
            print("Health: ", health)



    if health <= 0:
        print("The dragon killed you,you should go again!")
        quit()
    else:
        print("You win and the king reward you with his draughter.")
        print("""````´´¶¶¶¶¶¶¶¶´´´´´´Sweet
                    ´´´´´¶¶¶¢¢¢¢¶¶¶´´´´´
                    ´´´´1¶¶¢¢¢¢¢¢¶¶´´´´´
                    ´´´´¶¶¢¢¢¢¢¢¢¶1´´´´´Caring
                    ´´´´¶¢¢¢¢¢¢¢¢¶¶´´´´´
                    ´´´¶¶¢¢¢¢¢¢¢¢¢¶´´´´´
                    ´´1¶¢¢¢¢¢¢¢¢¢1´´´´´´Naughty
                    ´´7¶¢¢¢¢¢¢¢¢¢¶¶¶´´´´
                    ´´´¶¢¢¢¢¢¢¢¢¢¢¢¶¶´´´
                    ´´¶¶¶¶¶¶¢¢¢¢¢¢¢¶¶´´´$3X!
                    ´1¶¶¶´´¶¶¢¢¢¢¢¶¶´´´´
                    ´¶¶¶´´´´¶¶¢¢¢¢¶7´´´´
                    7¶¢¢1´´´´¶¢¢¢¢¶´´´´´Inteligent
                    ´¶¶¶¶¶¶¶¢¢¢¢1¶¢´´´´´
                    ´´´´´´1¢¢¢¢¢¢¶7´´´´´
                    ´´´´´¢¢¢1111¢¶´´´´´´Loving
                    ´´´´¶¶¢¢1111¶¶´´´´´´
                    ´´´1¶¢111111¶´´´´´´´
                    ´´´´¶¢111111¶´´´´´´´Loyal
                    ´´´´¶¢111111¶´´´´´´´
                    ´´´´1¶111111¶´´´´´´´
                    ´´´´´¶¢1111¢¶´´´´´´´Reliable
                    ´´´´´´¶1111¶¢´´´´´´´
                    ´´´´´´¶1111¶´´´´´´´´
                    ´´´´´´¶¢111¶7´´´´´´´Freaky
                    ´´´´´´¶1111¶¢´´´´´´´
                    ´´´´´1¶¢111¢¶´´´´´´´
                    ´´´´´¶¢1111¢¶´´´´´´´Humuorus
                    ´´´´¢¶¢¢¢¢¢¢¢´´´´´´´
                    ´´´´¶¢¢¢¢¢¢¢¶´´´´´´´
                    ´´´´¶¢¢¢¢¢¢¢¶´´´´´´´Dependable
                    ´´´´¢¶¢¶1¶¶¢¶¶´´´´´´
                    ´´´´´¶¢¶´´¶¶¢¶´´´´´´
                    ´´´´´¶¢¶´´´¶¢¶¢´´´´´Trendy
                    ´´´´´¶¢¶7´´1¶¶¶´´´´´
                    ´´´´´¶¢¶1´´´1¶¶¶´´´´
                    ´´´7¶¶¢¶¶´´´´¶¢¶¶´´´Beautiful
                    ´´´´¶¶¢¢¶´´´¶¶¢¢¶¶´´
                    ´´´´¶¶¢¶¶¶7´´¶¶¢¢¶´´""")

        
            

def room2():
    global health
    
    print("""You are now in a land full of dragons.
          In front of you,you see two caves.
          In one cave,the dragon is friendly and will share his treasure with you.
          The other dragon is hungry and will eat you""")
    response = input("""You don't know which cave is good so which cave will you go into?
                left or right?: """)
    if response.lower() == "left":
        print("You saw all the gold and now you are forever rich and stop with the venture.")
    else:
        print("You are going to fight a big dragon!")
        dragon_fight()
        print("You have", health, "health left.")
    

# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()

