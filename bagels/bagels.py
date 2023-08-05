import random

NUM_DIGITS = 3
MAX_GUESS = 10

def guessSecretNum(numbers=list(range(10)), secretNum= ''):

    random.shuffle(numbers)

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):

    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
        if len(clues) == 0:
            return 'Bagels'
        clues.sort()
        return ' '.join(clues)
    
def isOnlyDigit(num):
    
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

print(f'I am thinking of a {NUM_DIGITS}digit number. Try to guess what it is')
print('The clues I give are...')
print('When I say: That means:')
print('Bagels -  None of the digits is correct.')
print('Pico -   One digit is correct but in the wrong position.')
print('Fermi -  One digit is correct and in the right position')

while True:
    secretNum = guessSecretNum()
    print(f'I have thought up a number. You have {MAX_GUESS} guesses to get it')
    guessTaken = 1

    while guessTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigit(guess):
            print(f'Guess # {guessTaken}')
            guess = input()
        print(getClues(guess, secretNum))
        guessTaken += 1

        if guess == secretNum:
            break
        elif guessTaken > MAX_GUESS:
            print(f'You ran out of guesses. The answer was {secretNum}.')
            
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break




