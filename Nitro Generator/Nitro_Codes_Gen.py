import random
import time
from colorama import Fore, init
import ctypes
import string
import sys

init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleW("Discord Nitro Codes Generator | By Maniac")

print(Fore.CYAN + """
        • ▌ ▄ ·.  ▄▄▄·  ▐ ▄ ▪   ▄▄▄·  ▄▄·      ▐ ▄ ▪  ▄▄▄▄▄▄▄▄        
        ·██ ▐███▪▐█ ▀█ •█▌▐███ ▐█ ▀█ ▐█ ▌▪    •█▌▐███ •██  ▀▄ █·▪     
        ▐█ ▌▐▌▐█·▄█▀▀█ ▐█▐▐▌▐█·▄█▀▀█ ██ ▄▄    ▐█▐▐▌▐█· ▐█.▪▐▀▀▄  ▄█▀▄ 
        ██ ██▌▐█▌▐█ ▪▐▌██▐█▌▐█▌▐█ ▪▐▌▐███▌    ██▐█▌▐█▌ ▐█▌·▐█•█▌▐█▌.▐▌
        ▀▀  █▪▀▀▀ ▀  ▀ ▀▀ █▪▀▀▀ ▀  ▀ ·▀▀▀     ▀▀ █▪▀▀▀ ▀▀▀ .▀  ▀ ▀█▄▀▪
""")
print(Fore.LIGHTMAGENTA_EX + "          @Sir.Maniac#5005 | GitHub - github.com/ManiacX0")

q=int(input("How many nitro codes ?\n> "))

for i in range(q):
    for g in range(1):
        w= ''.join(random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase) for _ in range(16))
        print(Fore.LIGHTCYAN_EX + w)
print(Fore.GREEN + "\nYou have successfully generated your nitro codes ! They have been saved to Nitro.txt !")
time.sleep(5)

sys.stdout = open("Nitro.txt", "w")
for i in range(q):
    for g in range(1):
        w= ''.join(random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase) for _ in range(16))
        print(w)
sys.stdout.close()