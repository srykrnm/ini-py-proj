from random import randint
from colorama import Fore,Style
from os import system as sys 
from time import sleep

### MAIN ###

ch=['rock','paper','scissors']
sys('clear')
print()
print(f'{Fore.LIGHTBLUE_EX}ROCK PAPER SCOSSORS{Style.RESET_ALL}')
print('__________________')
print()
ppoints=input('For how many points do you want to play ? : ')
if ppoints.isdigit() and int(ppoints)>0:
  sys('clear')
  ipoints=int(ppoints)
  ymark=0
  cmark=0
  dmark=0
  chno=1
  while ipoints > 0:
    print()
    print(f'{Fore.LIGHTBLUE_EX}ROCK PAPER SCOSSORS{Style.RESET_ALL}')
    print('__________________')
    print()
    print(f'your score = {ymark}\ncomputer\'s score = {cmark}\nnumber of ties = {dmark}')
    print()
    ch01=input(f'{chno}.) Enter your choice \n\n0.)rock\n1.)paper\n2.)scissors\n\n(0/1/2) : ')
    print()
    if ch01 in '012':
      compch0=randint(0,2)
      print()
      print(f'{Fore.GREEN}you chose :{Fore.RESET} {ch[int(ch01)]}')
      print()
      print(f'{Fore.CYAN}computer chose :{Fore.RESET} {ch[compch0]}')
      print()
      if int(ch01)==compch0:
        dmark+=1
        pass
      elif int(ch01)==0 and compch0==1:
        cmark+=1
      elif int(ch01)==0 and compch0==2:
        ymark+=1
      elif int(ch01)==1 and compch0==0:
        ymark+=1
      elif int(ch01)==1 and compch0==2:
        cmark+=1
      elif int(ch01)==2 and compch0==0:
        cmark+=1
      elif int(ch01)==2 and compch0==1:
        ymark+=1
      ipoints-=1
      chno+=1
      sleep(2)
      sys('clear')
    else:
      print(f'{Fore.RED}invalid input !{Style.RESET_ALL}')
      sleep(1)
      sys('clear')
  else:
    if cmark==ymark:
      re='it\'s a tie'
    elif cmark>ymark:
      re=f'{Fore.RED}computer won !{Style.RESET_ALL}'
    else:
      re=f'{Fore.GREEN}you won !{Style.RESET_ALL}'
    print(f'\nyour score = {ymark}\ncomputer\'s score = {cmark}\nnumber of ties = {dmark}\n\n{re}')
    sleep(0.7)
else:
  print()
  print(f'{Fore.RED}invalid input !{Style.RESET_ALL}')
  sleep(0.7)
print()
print(f'{Fore.BLUE}program over .{Style.RESET_ALL}\n')

### END ###