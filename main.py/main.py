from cat import Cat
import pyfiglet as pyg

title=pyg.figlet_format("Welcome to the Cat Game!")  
print(title)
picture = """                                  .--.
                                               `.  \
                                                 \  \
                                                  .  \
                                                  :   .
                                                  |    .
                                                  |    :
                                                  |    |
  ..._  ___                                       |    |
 `."".`''''""--..___                              |    |
 ,-\  \             ""-...__         _____________/    |
 / ` " '                    `""""""""                  .
 \                                                      L
 (>                                                      \
/                                                         \
\_    ___..---.                                            L
  `--'         '.                                           \
                 .                                           \_
                _/`.                                           `.._
             .'     -.                                             `.
            /     __.-Y     /''''''-...___,...--------.._            |
           /   _."    |    /                ' .      \   '---..._    |
          /   /      /    /                _,. '    ,/           |   |
          \_,'     _.'   /              /''     _,-'            _|   |
                  '     /               `-----''               /     |
                  `...-'                                       `...-'
                  """
print(picture)
name=input("Enter cat name: ")
colour = input("Enter cat colour: ")

my_cat= Cat(name,colour)
while True:
    action = int(input("""
What would you like to do?
1. Train the cat
2. Feed the cat
3. Play with the cat
4. Put the cat to sleep
5. Print cat stats."""))
    
    if action == 1:
        my_cat.train()
    elif action == 2:
        my_cat.feed()
    elif action == 3:
        my_cat.play()
    elif action == 4:
        my_cat.sleep()
    elif action == 5:
        my_cat.stats()

    if my_cat.energy>=75 or my_cat.weight>=10:
        my_cat.too_high()
    if my_cat.age>=15:
        my_cat.too_old()