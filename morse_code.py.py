from colorama import Fore,Style
from os import system

morsedict={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',' ':'/','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----','/':'-..-.','@':'.--.-.','!':'-.-.--','&':'.-...','(':'-.--.',')':'-.--.-','=':'-...-',',':'--..--','\'':'.----.','"':'.-..-.',':':'---...'}
while True:
	print(f"\n{Fore.BLUE}MORSE CODE ENCODER / DECODER\n----------------------------{Style.RESET_ALL}\n")
	choice=input('Enter your choice\n\na.)convert english to morse code\nb.)convert morse code to english\n\n(a/b) : ')
	if choice.lower()=='a':
		converted=''
		print()
		inpt=input('enter what you want to convert ? : ')
		for i in inpt:
			if i.lower() in morsedict:
				converted+=morsedict[i.lower()]+' '
			else:
				print()
				print(f'{Fore.RED}error : there is no morse code for \'{i}\'{Style.RESET_ALL}')
				break
		else:
			print()
			print(f'morse code for your input is : {Fore.BLUE}{converted}{Style.RESET_ALL}')
	elif choice.lower()=='b':
		converted=''
		print()
		inpt=input('enter the morse code that you want to convert : ')
		for i in (inpt.split(' ')):
			key_list = list(morsedict.keys())
			val_list = list(morsedict.values())
			if i in val_list:
				converted+=key_list[val_list.index(i)]
			else:
				print()
				print(f'{Fore.RED}error : there is no english alphabet for \'{i}\'{Style.RESET_ALL}')
				break
		else:
			print()
			print(f'english for your input is : {Fore.BLUE}{converted}{Style.RESET_ALL}')
			print()
	else:
		print()
		print(f'{Fore.RED}error : your choice is not in options .{Style.RESET_ALL}')
	rech=input('\ndo you want to start over ? : (y/n) ')
	if rech.lower()=='y':
		system('clear')
	elif rech.lower()=='n':
		break
	else:
		print(f'{Fore.RED}error : your choice is not in options .{Style.RESET_ALL}')
		break
print(f'\n{Fore.BLUE}program over.{Style.RESET_ALL}\n')