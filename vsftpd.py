import sys
import time
import random
import socket
from colorama import Fore, Back, Style

def usage():
    print("""



    Usage 
    _______________
    
    ./python3 vsftpd.py [IP Address] + [Protocol Port Number]
    
    ./python3 vsftpd.py 127.0.0.1 21""".strip())



def VulnChecker(target, port):
    check = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        check.connect((target, int(port)))
        print(Fore.BLUE + "[*] Connecting To Target [*]")
    except:
        print(Fore.BLUE + "[*] Connecting To Target Faild [*]")
        return False
    
    banner = check.recv(1024).strip()
    print(Fore.RED + "[!] Banner [!] ", banner)
    return False


