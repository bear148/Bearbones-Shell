import os
import sys
import subprocess

env = {}
v = "1.1.1"
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

def commands():
	while True:
		c = input(f"[{cwd}]- #: ")
		comDir = "/usr/bin"
		command = c.lower()
		commandSplit = command.split()
		firstPart = commandSplit[0]
		comCheck = os.path.isfile(f"{comDir}/{firstPart}")
		p = os.fork()
		if len(commandSplit) > 1:
			args = commandSplit[1]
			firstPart = commandSplit[0]
			ran = subprocess.run([firstPart, "-l", args], capture_output=True,text=True, shell=True)
			print(ran.stdout)
		elif len(commandSplit) == 1:
			args = ""
			firstPart = commandSplit[0]
			if firstPart != 'help':
				ran = subprocess.run([firstPart], capture_output=True,text=True, shell=True)
				print(ran.stdout)
			if firstPart == 'exit':
				sys.exit(-1)
				exit(-1)
commands()