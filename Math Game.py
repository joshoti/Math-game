'''Math game'''
from random import choice, randint
def questionGenerator():
    """
    Variables
        leftHand(str)
        rightHand(str)
        operators(list): [add, subtract, multiply, floor division, modulo, power]
            
    Returns(str)
        space separated equation. Eg "4 ** 1"
    """    
    operators = ['+', '-', '*', '//', '%', '**']
    leftHand = str(randint(0,100))
    operator = choice(operators)
    rightHand = randint(0,100)    
    if operator == '*':
        rightHand = str(rightHand%10) # If * operator, Make the RHS between 0-10
    elif operator == '%':
        rightHand = str(choice([2,3,5,10])) # If % operator, Make RHS either 2,3,5,10
    elif operator == '**':
        rightHand = str(choice([0,1,2]))
        leftHand = str(randint(0, 20)) # If ** operator, Make LHS between 0-20 and RHS between 0-2
    return f"{leftHand} {operator} {str(rightHand)}"

def run():
    correctCount = 0
    for i in range(10):
        print(f"Question {i+1} / 10")
        question = questionGenerator() # Get question from question function
        try:
            userAnswer = int(input(f"\t\t{question}  ")) # Your answer
        except ValueError:
            print('Input not recognised')
            continue
        
        correctAnswer = eval(question) # Computes string to get correct answer
        if userAnswer == correctAnswer:
            print('Correct!\n')
            correctCount +=1
        elif userAnswer != correctAnswer:
            print(f"Incorrect\nCorrect answer is {correctAnswer}\n")
            
    print(correctCount,'Correct answer(s) out of 10')
    if 8 <= correctCount: print('Excellent Performance!\n')
    elif 6 <= correctCount < 8: print('Above Average Performance!\n')
    elif 4 <= correctCount < 6: print('Average Performance!\n')
    elif correctCount < 4: print('You can do better Kido!\n')
    return correctCount

def hint():
    print("\n=================  HINT  =================\n")
    print('// means floor division. Return the integer part of division. Eg:\n5 // 2 = 2\t(2 rem 1)\n8 // 3 = 2\t(2 rem 2)\n4 // 7 = 0\t(0 rem 4)\n')
    print('% means modulus. Return the remainder part of division. Eg:\n5 % 2 = 1\t(2 rem 1)\n9 % 3 = 0\t(3 rem 0)\n4 % 7 = 4\t(0 rem 4)\n')
    print('** means exponent/raised to the power of. Eg:\n5 ** 2 = 25\n2 ** 3 = 8\n4 ** 1 = 4')

hint()
progress = [] # To save the score of all your tries
tries = 0
retry = 'y'
while retry != 'n':
    tries += 1
    if tries > 1:
        print()
        for attemptNo, score in enumerate(progress, start=1):
            print(f"Try {attemptNo}: {score}") # Prints score of all your tries
    print('\n=================  Begin!  =================\n')
    progress.append(run()) # This lines saves the score in list
    while True:
        retry = input("Would you like to try again. ( y/n ) ")
        if (retry == 'y') | (retry == 'n'):
            break
    if retry == 'y':
        hints = input("Would you like to view the hint: ( y/n ) ")
    elif retry == 'n':
        continue
    if hints == 'y':
        hint()
    
