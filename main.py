import os
import sys
import subprocess
import asyncio

env = {}
v = "2.1.1"
env['TERM'] = "linux"
cwd = os.getcwd()
c = input(f"[{cwd}]- #: ")

def write():
	print(f"Bearbones-Shell v{v}")
	print("Copyright (c) 2021: Michael S.")	

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
	while True:
		c = input(f"[{cwd}]- #: ")
		comDir = "/usr/bin"
		command = c.lower()
		commandSplit = command.split()
		firstPart = commandSplit[0]
		comCheck = os.path.isfile(f"{comDir}/{firstPart}")
		if len(commandSplit) > 1:
			args = commandSplit[1]
			firstPart = commandSplit[0]
			asyncio.run(run(f'{firstPart} {args}'))
			print('\n')
		elif len(commandSplit) == 1:
			args = ""
			firstPart = commandSplit[0]
			if firstPart != 'help' and 'exit':
				subprocess.run([firstPart], capture_output=True,text=True, shell=True)
				print('\n')
			elif firstPart == 'exit':
				sys.exit(-1)
				exit(-1)
			else:
				print("Not a command!")
commands()