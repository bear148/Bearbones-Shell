import os
import sys
import posix

env = {}
v = "1.0.1"
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
		if len(commandSplit) > 1:
			print("2")
			if comCheck:
				args = commandSplit[1]
				print("Executeda")
				p = os.fork()
				if p == 0:
					os.execve(f"/usr/bin/{firstPart}", [f"{firstPart}", f"{args}"], env)
				print('\n')
		elif len(commandSplit) == 1:
			print("Executedb")
			print("1")
			if comCheck:
				args = ""
				p = os.fork()
				if p == 0:
					os.execve(f"/usr/bin/{firstPart}", [firstPart, args], env)
			elif command == 'exit':
				sys.exit(-1)
				exit(-1)
			elif command == 'help':
				help()
commands()