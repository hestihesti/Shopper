import os
import sys
from termcolor import colored

def shop():
	clr = 'clear'
	os.system(clr)
	q1 = input('[m]ake A Grocery List OR [u]se List In Store:\n> ')
	if q1 == 'm':
		groc = ''
		while groc != "q":
			print(colored('Press "q" To Quit', 'red'))
			groc = input('What Do You Need:\n> ')
			format = groc + '\n'
			if groc != 'q':
				with open('list.txt', 'a') as f:
					f.write(format)
			elif groc == "q":
				os.system(clr)
				break
			else:
				print('Something Went Wrong!')
	elif q1 == 'u':
		item = ''
		os.system(clr)
		while item != "q":
			cat = 'cat list.txt'
			os.system(cat)
			print(colored('Press "q" To Quit', 'red'))
			item = input('What Item Can You Remove From List:\n> ')
			if item != "q":
				try:
					with open('list.txt', 'r') as rd:
						lines = rd.readlines()
						with open('list.txt', 'w') as fw:
							for line in lines:
								if line.strip('\n') != item:
									fw.write(line)
									print(colored('Item Deleted From List', 'green'))
				except:
					print('Something Went Wrong!')
			elif item == "q":
				os.system(clr)
				break
			else:
				print('Something Went Wrong')

	else:
		print('Some Type Of Error Happened')


shop()
