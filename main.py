import os
import sys
import subprocess
import asyncio

env = {}
v = "3.1.1"
env['TERM'] = "linux"
cwd = os.getcwd()
c = input(f"[{cwd}]- #: ")

def help():
	print("\n")
	print(f"""
Bearbones-Shell v{v}")
Copyright (c) 2021: Michael S.
------------------------------
Bearbones Help Screen
	help: Shows this
	exit: Closes Shell
	Every command you used in bash, works with this shell!""")

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
	print(f"Bearbones-Shell v{v}")
	print("Copyright (c) 2021: Michael S.")	
	while True:
		c = input(f"[{cwd}]- #: ")
		comDir = "/usr/bin"
		command = c.lower()
		commandSplit = command.split()
		firstPart = commandSplit[0]
		comCheck = os.path.isfile(f"{comDir}/{firstPart}")
		if len(commandSplit) == 2:
			if firstPart == 'vim':
				arg = commandSplit[1]
				asyncio.run(run(f'/usr/bin/vim {arg}'))
				print("\n")
			else:
				args = commandSplit[1]
				firstPart = commandSplit[0]
				asyncio.run(run(f'{firstPart} {args}'))
				print('\n')
		elif len(commandSplit) == 1:
			args = ""
			firstPart = commandSplit[0]
			if firstPart != 'help' and 'exit' and 'ls' and 'cwd':
				subprocess.run([firstPart], capture_output=True,text=True, shell=True)
				print('\n')
			elif firstPart == 'exit':
				break
				sys.exit(-1)
				exit(-1)
			elif firstPart == 'ls':
				print(cwd)
			elif firstPart == 'cwd':
				print(cwd)
			else:
				print("Not a command!")
		
		elif len(commandSplit) == 3:
			arg1 = commandSplit[1]
			arg2 = commandSplit[2]
			asyncio.run(run(f'{firstPart} {arg1} {arg2}'))
		
		elif len(commandSplit) == 4:
			arg = commandSplit[1]
			arg1 = commandSplit[2]
			arg2 = commandSplit[3]
			asyncio.run(run(f'{firstPart} {arg} {arg1} {arg2}'))
			print("\n")
commands()