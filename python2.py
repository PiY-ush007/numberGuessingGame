import random
num = random.randint(1, 9)
userInput = int(input())
chances = 5

if (userInput != num):
    print('sorry that is not the number, it was', num)
    print('you have', chances, 'chances')
    chances -= 1

elif (userInput == num):
    print('congrats!! right answer, it is', num)
