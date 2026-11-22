# Import and global variables
import random

print()
print('welcome to Rock Paper Scissor game ^_^')
print('*'* 45)

CHOICES = ['rock', 'paper', 'scissor']

# Create function to get user input
def user():
    choice = input('pick your choice : ')
    while choice not in CHOICES:
        choice = input('pick your choice : ')
    return choice

# Create function to get computer input
def computer():
    print('---------- vs ----------')
    _computer = random.choice(CHOICES)
    print(f"computer's choice : {_computer}")
    return _computer

# Create function to game logic
def logic(user, computer):
    if user == computer:
        print()
        print('draw!')
    elif (user == 'rock' and computer == 'scissor') or \
        (user == 'sccisor' and computer == 'paper') or \
            (user == 'paper' and computer == 'rock'):
        print()
        print('user win!')
    else:
        print()
        print('computer win!')

# Runner
if __name__ == '__main__':
    answer = 'y'
    while answer == 'y':
        logic(user(), computer())
        print()
        answer = input('do you want to continue? (y/n) : ')
        print()