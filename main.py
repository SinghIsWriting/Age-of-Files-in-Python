#!/data/data/com.termux/files/usr/bin/python3
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import os
from datetime import datetime

reqpath = input("Enter the directory path(without filename): ")
file = input("Enter the file name: ")
today = datetime.now()

filepath = os.path.join(reqpath,file)
if os.path.isfile(filepath):
	filecrdate = datetime.fromtimestamp(os.path.getctime(filepath))
	difds = (today - filecrdate).days
	print(f"{Fore.GREEN}\nThis file is",str(difds),f"{Fore.GREEN}day(s) old\n")
else:
	print(f"{Fore.RED}\nNo such file in this directory!\n")
