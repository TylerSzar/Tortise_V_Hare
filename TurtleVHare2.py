
# Turtle v Hare
'''
This program uses 3 different functions which are combined into a
main function to simulate the famous race between the tortoise and the hare
It is 50 'seconds' long and uses probability to determine the animal’s next move
the time it takes to complete a race and the winner is then displayed
'''
import random
# moveset for hare using min and max to set range
def hare(pos):
    rand_hare = random.randint(1,10)
    if rand_hare in range(1,3):
        return pos
    elif rand_hare in range(3,5):
        return min(pos+7,50)
    elif rand_hare == 5:
        return max(1,pos-10)
    elif rand_hare in range(5,9):
        return min(pos+1,50)
    elif rand_hare in range(9,11):
        return max(pos-2,1)
# moveset for tortioise using min and max to set a range
def tort(pos):
    rand_tort = random.randint(1,10)
    if rand_tort in range(9,11):
        return max(0,pos-5)
    elif rand_tort in range(1,6):
        return min(pos+3,50)
    elif rand_tort in range(6,9):
        return min(pos+1,50)

# displays race in progress
def race_prog(curr_hare,curr_tort):
    for i in range(1,51):
        if i == curr_hare and i == curr_tort:
            print('OW!',end = '')
            continue
        if i == curr_hare:
            print("H",end = "")
        if i == curr_tort:
            print("T",end = "")
        else:
            print(" ",end = "")

    print()

def main():
    print('On your mark!... \n GET READY \n GO! GO! GO!')
    time = 0
    curr_hare = 1
    curr_tort = 1

    while curr_hare < 50 and curr_tort < 50:
        curr_hare = hare(curr_hare)
        curr_tort = tort(curr_tort)
        time += 1
        race_prog(curr_hare,curr_tort)
        

    if curr_hare == 50:
        print("Congrats to the fast hare")
    elif curr_tort == 50:
        print("We can't believe it! \n THE TURTLE WINS!!!")
    elif time >= 50:
        print('Valiant effort! \n It was a tie which means the Tortoise wins!')
    print(f"Time of race : {time} seconds")

main()
