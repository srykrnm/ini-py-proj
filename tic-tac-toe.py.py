from colorama import Fore
import sys
import time
import os
import random

### FUNCTIONS ###

def sp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.05)
  else:
      print()  

### MAIN ###

os.system('clear')
while True:
    a=['_','_','_']
    b=['_','_','_']
    c=['_','_','_']
    boarddict={'a':a,'b':b,'c':c}
    oppls=[a,b,c]
    print()
    start=input(f'{Fore.CYAN}HOME PAGE{Fore.RESET}\n________\n\nEnter !start = to start\n\nEnter !about = to go to the about page . \n\n: ')
    if start.lower()=='!start':
        os.system('clear')
        l=1
        while l>0:
            print()
            print(f'{Fore.CYAN}TIC TAC TOE{Fore.RESET}')
            print('___________')
            print()
            ch=input('enter your choice (x/o) : ')
            if ch.lower() in 'xo':
                if ch.lower()=='x':
                    cch='o'
                else:
                    cch='x'
                print()
                print(f'you chose \'{ch}\'\n\nTherefore the computer is \'{cch}\'')
                time.sleep(2)
                print()
                os.system('clear')
                hg=0
                i=1
                while i > 0:
                    print()
                    print(f'{Fore.CYAN}TIC TAC TOE{Fore.RESET}')
                    print('___________')
                    print()
                    print(f'''     1    2    3
    
a   | {a[0]} | {a[1]} | {a[2]} |
        +   +
b   | {b[0]} | {b[1]} | {b[2]} |
        +   +
c   | {c[0]} | {c[1]} | {c[2]} |

''')
                    inp=input(f'\'{ch}\'s turn\n\nselect where you want to mark \'{ch}\' . eg -: b1 etc .. : ')
                    time.sleep(1)
                    if len(inp)==2 and inp[0].isalpha() and inp[1].isdigit() and inp[0].lower() in 'abc' and inp[1] in '123':
                        g=boarddict[inp[0]] #a
                        r=int(inp[1])-1 #0
                        hg+=1
                        if g[r]=='_':
                            g[r]=ch
                            if a[0]==a[1]==a[2]==ch or b[0]==b[1]==b[2]==ch or c[0]==c[1]==c[2]==ch:
                                winner=f'{Fore.GREEN}you won!{Fore.RESET}'
                                i-=1
                            elif a[0]==b[1]==c[2]==ch or a[2]==b[1]==c[0]==ch:
                                winner=f'{Fore.GREEN}you won!{Fore.RESET}'
                                i-=1
                            elif a[0]==b[0]==c[0]==ch or a[1]==b[1]==c[1]==ch or a[2]==b[2]==c[2]==ch:
                                winner=f'{Fore.GREEN}you won!{Fore.RESET}'
                                i-=1
                            else:
                                if hg==5:
                                    winner=f'{Fore.LIGHTRED_EX}its a draw!{Fore.RESET}'
                                    i-=1
                            sf=1
                            while sf>0:
                                cchr=random.choice(oppls)
                                s=random.randint(0,2)
                                if cchr[s]=='_':
                                    cchr[s]=cch
                                    sf-=1
                                else:
                                    if hg==5:
                                        sf-=1
                                    else:
                                        pass
                            else:
                                if a[0]==a[1]==a[2]==cch or b[0]==b[1]==b[2]==cch or c[0]==c[1]==c[2]==cch:
                                    winner=f'{Fore.RED}computer won !{Fore.RESET}'
                                    i-=1
                                elif a[0]==b[1]==c[2]==cch or a[2]==b[1]==c[0]==cch:
                                    winner=f'{Fore.RED}computer won !{Fore.RESET}'
                                    i-=1
                                elif a[0]==b[0]==c[0]==cch or a[1]==b[1]==c[1]==cch or a[2]==b[2]==c[2]==cch:
                                    winner=f'{Fore.RED}computer won !{Fore.RESET}'
                                    i-=1
                                else:
                                    pass

                        else:
                            print()
                            print(f'{Fore.RED}The place \'{Fore.LIGHTBLUE_EX}{inp}{Fore.RESET}\'{Fore.RED} is already filled ! .{Fore.RESET}')
                            time.sleep(0.7)
                            os.system('clear')    
                    else:
                        print()
                        print(f'{Fore.RED}error : invalid input .{Fore.RESET}')
                        time.sleep(0.7)
                        os.system('clear')
                    os.system('clear')               
                else:
                    os.system('clear')
                    print()
                    print(f'{Fore.CYAN}TIC TAC TOE{Fore.RESET}')
                    print('___________')
                    print()
                    print(f'''     1    2    3
    
a   | {a[0]} | {a[1]} | {a[2]} |
        +   +
b   | {b[0]} | {b[1]} | {b[2]} |
        +   +
c   | {c[0]} | {c[1]} | {c[2]} |

''')
                    print()
                    print(winner)
                    print()
                    restch0=input('do you want to go back to the home page ? (y/n) : ')
                    if restch0.lower()=='y':
                        os.system('clear')
                        break
                    elif restch0.lower()=='n':
                        l-=1
                    else:
                        print()
                        print(f'{Fore.RED}error : invalid input{Fore.RESET}')
                        l-=1

            else:
                print()
                print(f'{Fore.RED}error : invalid input{Fore.RESET}')
                time.sleep(0.7)
                os.system('clear')
        else:
            break    
    
    elif start.lower()=='!about':
        os.system('clear')
        print()
        print(f'{Fore.CYAN}ABOUT{Fore.RESET}')
        print('_____')
        print()
        sp(''' 
How to play : -> use the !start command to start the game.
              -> enter your choice (x/o)
              -> enter where you want to place your choice 
                 eg -: a1,b3,c2 etc ..  
              -> after this the computer will mark its choice
              -> this loop will continue until win/draw .''')
        print()
        restch=input('do you want to go back to the start page ? (y/n) : ')
        if restch.lower()=='y':
            os.system('clear')
            pass
        elif restch.lower()=='n':
            break
        else:
            print()
            print(f'{Fore.RED}error : invalid input{Fore.RESET}')
            break
    else:
        print()
        print(f'{Fore.RED}error : invalid input{Fore.RESET}')
        time.sleep(0.7)
        os.system('clear')
print()
print(f'{Fore.BLUE}program over .{Fore.RESET}')
print()