import colorama   # importing colorama library for colorful text
from colorama import Fore
colorama.init(autoreset=True)
import os
from datetime import datetime

# taking input the path of the directory where file is present
reqpath = input("Enter the directory path(without filename): ")
file = input("Enter the file name: ")  # taking input file name
today = datetime.now()   # finding current date

filepath = os.path.join(reqpath,file)
if os.path.isfile(filepath):
	# finding date of creation of file
	filecrdate = datetime.fromtimestamp(os.path.getctime(filepath))

	# calculating the days of age
	difds = (today - filecrdate).days
	print(f"\nDate of creation: {filecrdate}")
	print(f"{Fore.GREEN}\nThis file is",str(difds),f"{Fore.GREEN}day(s) old\n")
else:
	print(f"{Fore.RED}\nNo such file in this directory!\n")
