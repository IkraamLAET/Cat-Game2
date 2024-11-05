from cat import Cat

print("Welcome to the Cat Game!")

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
