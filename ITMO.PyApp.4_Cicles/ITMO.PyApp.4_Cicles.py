print("Practice 4. Cicles")

from random import randint
import time


#Names input
igrok1 = input('First Player name: ')
igrok2 = input('Second player name: ')


#Scores count
wins_counter1 = 0
wins_counter2 = 0
sum_of_points1 = 0
sum_of_points2 = 0

for i in range(5):

    #Player 1 rolls a dice
    print('')
    print('Round', i+1)
    print(igrok1 ,'rolls a dise')
    time.sleep(1)
    n1 = randint (1, 6)
    print('Roll result', n1)
    sum_of_points1 += n1           # Score sum
    print('Total score', igrok1, 'Try number', i+1, 'is', sum_of_points1)

    # Player 2 rolls a dice
    print(igrok2 ,'rolls a dise')
    time.sleep(1)
    n2 = randint (1, 6)
    print('Roll result', n2)
    sum_of_points2 += n2           # Score sum
    print('Total score', igrok2, 'Try number', i+1, 'is', sum_of_points2)

    if n1 > n2:
        wins_counter1 +=1
        print('This round is after player', igrok1)
    elif n1 < n2:
        wins_counter2 +=1
        print('This round is after player', igrok2)
    else:
        print('Draw')
    

# Defining a winner
if wins_counter1 > wins_counter2:
    print('')
    print('The winner is', igrok1)
    print('Total wins', wins_counter1)
    print('Total score', sum_of_points1)
elif wins_counter2 > wins_counter1:
    print('')
    print('The winner is', igrok2)
    print('Total wins', wins_counter2)
    print('Total score', sum_of_points2)
else:
    print('')
    print('Draw')