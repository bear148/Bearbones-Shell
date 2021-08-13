import os
import sys
import subprocess
import asyncio
from sty import fg, bg, ef, rs

###########################
#		DISCLAIMER		  #
# Anything here that uses #
# os.system() is temporary!#
###########################

env = {}
v = "3.2.2a"
env['TERM'] = "linux"
cwd = os.getcwd()
clearFixed = False # <- This is wether or not I've replaced the clear function with a function that doesn't use os.system() because shell's can't do that.

def clear():
	os.system('clear')

def reset():
	# Temp
	os.system('python3 main.py')

def help():
	print(f"""
Bearbones-Shell v{v}
Copyright (c) 2021: Michael S.
------------------------------
Bearbones Help Screen
	help: Shows this
	exit: Closes Shell
	Every command you used in bash, works with this shell!""")

def new():
	print(f"""
Bearbones-Shell v{v}
Copyright (c) 2021: Michael S.
------------------------------
New Stuff I Want to Work On/To-Do List
	[ ] Write Documentation
	[ ] Make commands like vim work
	[ ] Bug test
	[ ] Theme
	[ ] Config Files
""")

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

def commands():
	clear()
	print(f"Bearbones-Shell v{v}")
	print("Copyright (c) 2021: Michael S.")
	print("------------------------------")
	print("Important! Some commands may not work as excpected.")
	print("Bearbones is in alpha so excpect bugs! It would be")
	print("Appreciated if you could write an issue if you encounter one.")
	print("-------------------------------------------------------------")
	while True:
		d = fg.da_green + "[" + fg.li_green + f"{cwd}" + fg.da_green + "]- #: " + fg.rs
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
			else:
				args = commandSplit[1]
				firstPart = commandSplit[0]
				asyncio.run(run(f'{firstPart} {args}'))
		elif len(commandSplit) == 1:
			args = ""
			firstPart = commandSplit[0]
			if firstPart != 'exit' and firstPart != 'help' and firstPart != 'todo' and firstPart != 'reset-bear':
				asyncio.run(run(f'{firstPart}'))
			elif firstPart == 'exit':
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
		
		elif len(commandSplit) == 3:
			arg1 = commandSplit[1]
			arg2 = commandSplit[2]
			asyncio.run(run(f'{firstPart} {arg1} {arg2}'))
		
		elif len(commandSplit) == 4:
			arg = commandSplit[1]
			arg1 = commandSplit[2]
			arg2 = commandSplit[3]
			asyncio.run(run(f'{firstPart} {arg} {arg1} {arg2}'))
commands()