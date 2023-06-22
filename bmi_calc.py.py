from colorama import Fore,Style
import sys
import os
import time

def sp(str): # Thanks JBlove27 xD
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.05)

os.system("clear")
print(f"{Fore.BLUE}\nBMI CALCULATOR\n--------------{Style.RESET_ALL}\n")
sp('This is a BMI calculator . you have to enter your weight in kg and height in centimeters and it will return your BMI status\n')
print()
w=input('enter your weight in kg : ')
h=input('enter your height in centimeters : ')
if w.isdigit() and h.isdigit():
	try:
		bmi=int(w)/float((int(h)/100)**2)
	except:
		print(f'{Fore.RED}ERROR: the data you have given is wrong !{Style.RESET_ALL}')
		exit(1)
	if bmi<18.5:
		status=f'{Fore.RED}underweight{Style.RESET_ALL}'
	elif bmi >=18.5 and bmi <=24.9:
		status=f'{Fore.GREEN}normal{Style.RESET_ALL}'
	elif bmi>=25 and bmi<=29.9:
		status=f'{Fore.RED}overweight{Style.RESET_ALL}'
	elif bmi >=30 and bmi<=34.9:
		status=f'{Fore.RED}obese (class 1){Style.RESET_ALL}'
	elif bmi >=35 and bmi <=39.9:
		status=f'{Fore.RED}obese (class 2){Style.RESET_ALL}'
	elif bmi>=40:
		status=f'{Fore.RED}obese (class 3){Style.RESET_ALL}'
	else:
		print(f'{Fore.RED}error the data ou have given is wrong !{Style.RESET_ALL}')
	print()
	sp(f'your BMI is {round(bmi,2)} . this tells that your BMI status is {status}\n')
else:
	print(f'{Fore.RED}ERROR: the data you have given is wrong !{Style.RESET_ALL}')
print()
print(f'{Fore.BLUE}pgm over{Style.RESET_ALL}')
print()