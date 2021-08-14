import os
import sys
import subprocess
import asyncio
from sty import fg, bg, ef, rs
import json
import time

# Open the config file
with open("config.json", 'r') as f:
	settings = json.load(f)

env = {}
v = "4.2.2a"
env['TERM'] = "linux"
cwd = os.getcwd()
clearFixed = False # <- This is wether or not I've replaced the clear function with a function that doesn't use os.system() because shell's can't do that.
customCommands = False
textColor = str(settings['textColor'])
dirColor = str(settings['dirColor'])
colors1Work = False
colors2Work = False
color1 = fg.white
color2 = fg.white

def clear():
	os.system('clear') # <- Temporary

def reset():
	os.system('python3 main.py') # <- Temporary

def help():
	print(f"""Bearbones-Shell v{v}
Copyright (c) 2021: Michael S.
------------------------------
Bearbones Help Screen
	help: 		Shows this
	exit: 		Closes Shell
	reset-bear: Restarts Shell
	todo:       Shows upcoming updates
	clear:      Clears screen.
	info:       Shows some extra info that may be useful
	Every command you've used in bash, works with this shell!	
""")

def new():
	print(f"""Bearbones-Shell v{v}
Copyright (c) 2021: Michael S.
------------------------------
New Stuff I Want to Work On/To-Do List
	[X] Write Documentation
	[ ] Make commands like vim work
	[ ] Bug test
	[ ] Theme
	[X] Config Files
	[X] Configuration Documentation
""")

def colors():
	global colors1Work
	global colors2Work
	global color1
	global color2
	if textColor != 'dark_black' and textColor != 'dark_red' and textColor != 'dark_green' and textColor != 'dark_blue' and textColor != 'dark_magenta' and textColor != 'dark_cyan' and textColor != 'dark_white' and textColor != 'black' and textColor != 'red' and textColor != 'green' and textColor != 'yellow' and textColor != 'blue' and textColor != 'magenta' and textColor != 'cyan' and textColor != 'white' and textColor != 'light_black' and textColor != 'light_red' and textColor != 'light_green' and textColor != 'light_yellow' and textColor != 'light_blue' and textColor != 'light_magenta' and textColor != 'light_cyan' and textColor != 'light_white':
		print('E: TextColor is invalid!')
		print('O: Defaulting to white...')
		time.sleep(5)
		color1 = fg.white
	elif dirColor != 'dark_black' and dirColor != 'dark_red' and dirColor != 'dark_green' and dirColor != 'dark_blue' and dirColor != 'dark_magenta' and dirColor != 'dark_cyan' and dirColor != 'dark_white' and dirColor != 'black' and dirColor != 'red' and dirColor != 'green' and dirColor != 'yellow' and dirColor != 'blue' and dirColor != 'magenta' and dirColor != 'cyan' and dirColor != 'white' and dirColor != 'light_black' and dirColor != 'light_red' and dirColor != 'light_green' and dirColor != 'light_yellow' and dirColor != 'light_blue' and dirColor != 'light_magenta' and dirColor != 'light_cyan' and dirColor != 'light_white':
		print('E: DirColor is invalid!')
		print('O: Defaulting to white...')
		time.sleep(5)
		color2 = fg.white
	else:
		colors2Work = True
		colors1Work = True

	# YandereDev Moment
	if colors1Work and colors2Work:
		if textColor == 'dark_black':
			color1 = fg.da_black
		elif textColor == 'dark_red':
			color1 = fg.da_red
		elif textColor == 'dark_green':
			color1 = fg.da_green
		elif textColor == 'dark_blue':
			color1 = fg.da_blue
		elif textColor == 'dark_magenta':
			color1 = fg.da_magenta
		elif textColor == 'dark_cyan':
			color1 = fg.da_cyan
		elif textColor == 'dark_yellow':
			color1 = fg.da_yellow
		elif textColor == 'black':
			color1 = fg.black
		elif textColor == 'red':
			color1 = fg.red
		elif textColor == 'green':
			color1 = fg.green
		elif textColor == 'blue':
			color1 = fg.blue
		elif textColor == 'magenta':
			color1 = fg.magenta
		elif textColor == 'cyan':
			color1 = fg.cyan
		elif textColor == 'white':
			color1 = fg.white
		elif textColor == 'yellow':
			color1 = fg.yellow
		elif textColor == 'light_black':
			color1 = fg.li_black
		elif textColor == 'light_red':
			color1 = fg.li_red
		elif textColor == 'light_green':
			color1 = fg.li_green
		elif textColor == 'light_blue':
			color1 = fg.li_blue
		elif textColor == 'light_magenta':
			color1 = fg.li_magenta
		elif textColor == 'light_cyan':
			color1 = fg.li_cyan
		elif textColor == 'light_yellow':
			color1 = fg.li_yellow
		if dirColor == 'dark_black':
			color2 = fg.da_black
		elif dirColor == 'dark_red':
			color2 = fg.da_red
		elif dirColor == 'dark_green':
			color2 = fg.da_green
		elif dirColor == 'dark_blue':
			color2 = fg.da_blue
		elif dirColor == 'dark_magenta':
			color2 = fg.da_magenta
		elif dirColor == 'dark_cyan':
			color2 = fg.da_cyan
		elif dirColor == 'dark_yellow':
			color2 = fg.da_yellow
		elif dirColor == 'black':
			color2 = fg.black
		elif dirColor == 'red':
			color2 = fg.red
		elif dirColor == 'green':
			color2 = fg.green
		elif dirColor == 'blue':
			color2 = fg.blue
		elif dirColor == 'magenta':
			color2 = fg.magenta
		elif dirColor == 'cyan':
			color2 = fg.cyan
		elif dirColor == 'white':
			color2 = fg.white
		elif dirColor == 'yellow':
			color2 = fg.yellow
		elif dirColor == 'light_black':
			color2 = fg.li_black
		elif dirColor == 'light_red':
			color2 = fg.li_red
		elif dirColor == 'light_green':
			color2 = fg.li_green
		elif dirColor == 'light_blue':
			color2 = fg.li_blue
		elif dirColor == 'light_magenta':
			color2 = fg.li_magenta
		elif dirColor == 'light_cyan':
			color2 = fg.li_cyan
		elif dirColor == 'light_yellow':
			color2 = fg.li_yellow

def unknownCustomCommandDirectory():
	global customCommands
	customDirectory = settings['customCommandDirectory']
	customCommandsUse = settings['useCustomCommands']
	if customCommandsUse:
		if os.path.isdir(customDirectory) and os.path.exists(customDirectory):
			customCommands = True
			print("Custom commands folder found!")
			if not os.listdir(customDirectory):
				print('W: Directory is Empty')
				time.sleep(4)
			else:
				print('O: Files found in directory')
				time.sleep(3)
		else:
			print("A critical error has been encountered.")
			print(f"The directory: {str(settings['customCommandDirectory'])} was not found!")
			print("Please fix this in your config.json file.")
			print("This prompt will close in 8 seconds.")
			time.sleep(8)

def info():
	print(f"""Bearbones-Shell v{v}
Copyright (c) 2021: Michael S.
------------------------------
Bearbones Info Screen
	Different output prefixes:
		O: Everything went OK
		E: Error encountered
		W: Just a warning
""")

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\nO: {stdout.decode()}')
    if stderr:
        print(f'[stderr]\nE: {stderr.decode()}')

def commands():
	clear()
	unknownCustomCommandDirectory()
	colors()
	clear()
	print(f"Bearbones-Shell v{v}")
	print("Copyright (c) 2021: Michael S.")
	print("------------------------------")
	print("Important! Some commands may not work as excpected.")
	print("Bearbones is in alpha so excpect bugs! It would be")
	print("Appreciated if you could write an issue if you encounter one.")
	print("-------------------------------------------------------------")
	while True:
		d = color1 + "[" + color2 + f"{cwd}" + color1 + "]- #: " + fg.rs
		c = input(d)
		comDir = "/usr/bin"
		command = c.lower()
		commandSplit = command.split()
		firstPart = commandSplit[0]
		comCheck = os.path.isfile(f"{comDir}/{firstPart}")
		if len(commandSplit) == 2:
			if firstPart == 'vim':
				# Temporary fix.
				# Before adding this, when the vim command would be ran nothing would show up.
				# I'll fix it soon.
				#      -- Michael [8/12/2021@7:57PM PST]
				arg = commandSplit[1]
				os.system(f'/usr/bin/vim {arg}')
			elif customCommands == True:
				customComCheck = os.path.isfile(f"{str(settings['customCommandDirectory'])}/{firstPart}")
				if customComCheck:
					args = commandSplit[1]
					firstPart = commandSplit[0]
					asyncio.run(run(f"{str(settings['customCommandDirectory'])}/{firstPart} {args}"))
				elif customComCheck == False:
					print('That command was not found in your custom commands directory!')
					print('Running from /usr/bin instead...')
					args = commandSplit[1]
					firstPart = commandSplit[0]
					asyncio.run(run(f"{comDir}/{firstPart} {args}"))
			elif customCommands == False:
				args = commandSplit[1]
				firstPart = commandSplit[0]
				asyncio.run(run(f'{firstPart} {args}'))
		elif len(commandSplit) == 1:
			args = ""
			firstPart = commandSplit[0]
			if firstPart != 'exit' and firstPart != 'help' and firstPart != 'todo' and firstPart != 'reset-bear' and firstPart != 'info' and firstPart != 'ls' and customCommands == False:
				asyncio.run(run(f'{firstPart}'))
			elif firstPart == 'exit':
				clear()
				break
			elif firstPart == 'help':
				help()
			elif firstPart == 'todo':
				new()
			elif firstPart == 'reset-bear':
				reset()
				break
			elif firstPart == 'cls' and clearFixed == False:
				clear()
			elif firstPart == 'info':
				info()
			elif firstPart == 'ls':
				asyncio.run(run(f'ls {cwd}'))
			elif customCommands == True:
				customComCheck = os.path.isfile(f"{str(settings['customCommandDirectory'])}/{firstPart}")
				if customComCheck:
					firstPart = commandSplit[0]
					asyncio.run(run(f"{str(settings['customCommandDirectory'])}/{firstPart}"))
				elif customComCheck == False:
					print('That command was not found in your custom commands directory!')
					print('Running from /usr/bin instead...')
					firstPart = commandSplit[0]
					asyncio.run(run(f"{comDir}/{firstPart}"))
			elif customCommands == False:
				firstPart = commandSplit[0]
				asyncio.run(run(f'{comDir}/{firstPart}'))
		
		elif len(commandSplit) == 3:
			arg = commandSplit[1]
			arg1 = commandSplit[2]
			if customCommands == True:
				customComCheck = os.path.isfile(f"{str(settings['customCommandDirectory'])}/{firstPart}")
				if customComCheck:
					firstPart = commandSplit[0]
					asyncio.run(run(f"{str(settings['customCommandDirectory'])}/{firstPart}"))
				elif customComCheck == False:
					print('That command was not found in your custom commands directory!')
					print('Running from /usr/bin instead...')
					firstPart = commandSplit[0]
					asyncio.run(run(f"{comDir}/{firstPart}"))
			elif customCommands == False:
				firstPart = commandSplit[0]
				asyncio.run(run(f'{comDir}/{firstPart} {arg} {arg1}'))
		
		elif len(commandSplit) == 4:
			firstPart = commandSplit[0]
			arg = commandSplit[1]
			arg1 = commandSplit[2]
			arg2 = commandSplit[3]
			if customCommands == True:
				customComCheck = os.path.isfile(f"{str(settings['customCommandDirectory'])}/{firstPart}")
				if customComCheck:
					firstPart = commandSplit[0]
					asyncio.run(run(f"{str(settings['customCommandDirectory'])}/{firstPart}"))
				elif customComCheck == False:
					print('That command was not found in your custom commands directory!')
					print('Running from /usr/bin instead...')
					firstPart = commandSplit[0]
					asyncio.run(run(f"{comDir}/{firstPart}"))
			elif customCommands == False:
				firstPart = commandSplit[0]
				asyncio.run(run(f'{comDir}/{firstPart} {arg} {arg1} {arg2}'))
commands()