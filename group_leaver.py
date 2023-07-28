import os
import discord
from discord.ext import commands
from colorama import Fore, init
from time import sleep
from win10toast import ToastNotifier
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Discord group leaver")

client = commands.Bot(command_prefix='$', self_bot = True)

lblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
lmagenta = Fore.LIGHTMAGENTA_EX
magenta = Fore.MAGENTA

reset = Fore.RESET


def finished(title, text):
     toast = ToastNotifier()
     toast.show_toast(title = title, msg = text, duration= 5, icon_path= None)

def cls(): 
    os.system('cls')
    print(f"{cyan}Group leaver")
    print(f"{magenta}By MegaMikeFro\n")


cls()
token = str(input(f"{cyan}[!] {lblue}Enter you authorization token here: "))
os.system("cls")
print(f"{magenta}This may take a few minutes")
print(reset)

@client.event
async def on_ready():
    leaved=0
    for group in client.private_channels:
    	if not 'Direct Message' in str(group) and not str(group).lower()=='избранное': 
                await group.leave()
                leaved+=1
    cls()
    finished("Discord group leaver", f"Successfully leaved from {leaved} groups!")
    print(f"{cyan}[!] {lblue}Leaved from {lmagenta}{leaved} {lblue}groups{reset}")
    print()
    print("Close the window")

client.run(token)