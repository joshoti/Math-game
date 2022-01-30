'''Math game'''
def que():
    from random import choice as rc
    ops = ['+','-','*','//','%','**']
    num = [i for i in range(101)]
    snum = [i for i in range(21)]
    q = f"{str(rc(num))} {rc(ops)} {str(rc(num))}"
    check = q.split()
    if check[1] == '*': check[2] = str(int(check[2])%10); return ' '.join(check) # If * operator, Make the RHS between 0-10
    elif check[1] == '%': check[2] = str(rc([2,3,5,10])); return ' '.join(check) # If % operator, Make RHS either 2,3,5,10
    elif check[1] == '**': check[2] = str(rc([0,1,2])); check[0] = str(rc(snum)); return ' '.join(check) # If ** operator, Make LHS between 0-20 and RHS between 0-2
    return q

def run():
    count = 0
    for _ in range(10):
        print(f"Q. {_+1} / 10")
        q = que() # Get question from question function
        x = int(input(f"\t\t{q} ")) # Your answer
        part = q.split()
        if part[1]=='+': y = int(part[0]) + int(part[2]) # IF Block computes correct answer
        elif part[1]=='-': y = int(part[0]) - int(part[2])
        elif part[1]=='*': y = int(part[0]) * int(part[2])
        elif part[1]=='//': y = int(part[0]) // int(part[2])
        elif part[1]=='%': y = int(part[0]) % int(part[2])
        elif part[1]=='**': y = int(part[0]) ** int(part[2])
        print(y) # Outputs correct answer
        if x==y: print('Correct!\n'); count +=1
        elif x!=y: print('Incorrect\n')
    print(count,'Correct answer(s) out of 10')
    if 8<=count: print('Excellent Performance!')
    elif 6<=count<8: print('Above Average Performance!')
    elif 4<=count<6: print('Average Performance!')
    elif count<4: print('You can do better Kido!')
    return count

def hint():
    print("HINT:")
    print('// means floor division. Return the integer part of division. Eg:\n5 // 2 = 2\t(2 rem 1)\n8 // 3 = 2\t(2 rem 2)\n4 // 7 = 0\t(0 rem 7)\n')
    print('% means modulus. Return the remainder after dividing. Eg:\n5 % 2 = 1\t(2 rem 1)\n9 % 3 = 0\t(3 rem 0)\n4 % 7 = 4\t(0 rem 7)\n')
    print('** means exponent/raised to the power of. Eg:\n5 ** 2 = 25\n2 ** 3 = 8\n4 ** 1 = 4')

hint()
progress = {} # To save the score of all your attempts
tries = 0
retry = 'y'
while retry!='n':
    tries+=1
    if tries>1:
        print('')
        for k,v in progress.items(): print(f"Try {k}: {v}") # Prints score of all your tries
    print('\nBegin!\n')
    progress[tries] = run() # This lines saves the score in dictionary
    while True: # Loop to make sure only recognised input is given
        retry = input("Would you like to try again. ( y/n ) ")
        if (retry == 'y') | (retry == 'n'): break
    if retry == 'y': hints = input("Would you like to view the hint: ( y/n )")
    if hints == 'y': hint()
    
