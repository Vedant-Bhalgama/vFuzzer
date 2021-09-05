import argparse
import socket
import time
import sys
import pyfiglet
from colorama import Fore, init

init(convert=True)

def banner():
    result = pyfiglet.figlet_format("vFuzz")
    print(Fore.RED + result)
    print("Vanila Buffer Overflow Fuzzing Tool!\n")

def create_socket_with_prefix():
    buffer = "A"*args.buffer
    prefix = args.setprefix
    if args.recvfirst == 1:
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((args.target, args.port))
                s.recv(1024)
                s.send(prefix.encode())
                s.recv(1024)
                s.send(buffer.encode())
                s.recv(1024)
                s.close()
                print(Fore.WHITE + "[!] Fuzzing with : " + str(len(buffer)) + " bytes")
                buffer = buffer + "A"*args.buffer
                time.sleep(args.delay)
            except:
                print(Fore.RED + "\n[!] Program crashed at : " + str(len(buffer)))
                sys.exit()
    if args.recvfirst == 0:
        while True:
            try:                        
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((args.target, args.port))
                s.send(prefix.encode())
                s.recv(1024)
                s.send(buffer.encode())
                s.recv(1024)
                s.close()
                print(Fore.WHITE + "[!] Fuzzing with : " + str(len(buffer)) + " bytes")
                buffer = buffer + "A"*args.buffer
                time.sleep(args.delay)  
            except:
                print(Fore.RED + "\n[!] Program crashed at : " + str(len(buffer)))
                sys.exit()                 


def create_socket_without_prefix():
    buffer = "A"*args.buffer
    if args.recvfirst == 1:
        while True:        
            try:            
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((args.target, args.port))
                s.recv(1024)
                s.send(buffer.encode())
                s.recv(1024)
                s.close()
                print(Fore.WHITE + "[!] Fuzzing with : " + str(len(buffer)) + " bytes")
                buffer = buffer + "A"*args.buffer
                time.sleep(args.delay)
            except:
                print(Fore.RED + "\n[!] Program crashed at : " + str(len(buffer)))
                sys.exit()
    if args.recvfirst == 0:
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((args.target, args.port))
                s.send(buffer.encode())
                s.recv(1024)
                s.close()
                print(Fore.WHITE + "[!] Fuzzing with : " + str(len(buffer)) + " bytes")
                buffer = buffer + "A"*args.buffer
                time.sleep(args.delay)  
            except:
                print(Fore.RED + "\n[!] Program crashed at : " + str(len(buffer)))
                sys.exit()

banner()
print(Fore.WHITE + "[!] Example (With Prefix) : python ./vfuzzer.py -b 1000 -d 2 -s 'administrator' -t 192.168.1.32, -p 9091 -rf\n")
parser = argparse.ArgumentParser(description=Fore.WHITE + "Vanilla Buffer Overflow Fuzzing Tool!")
parser.add_argument('-np', '--noprefix', action='store_true', help="Specify this flag if you don't want to keep a prefix")
parser.add_argument('-b', '--buffer', help="Set the bytes to send", type=int)
parser.add_argument('-d', '--delay', help="Set a time delay", type=int)
parser.add_argument('-s', '--setprefix', help="Set a prefix")
parser.add_argument('-t', '--target', help="Specify a target host")
parser.add_argument('-p', '--port', help="Specify the target port to fuzz", type=int)
parser.add_argument('-rf', '--recvfirst', help="Recieve bytes first, If you want to use it, Set it to 1 else 0", type=int)

args = parser.parse_args()


if args.noprefix:
    create_socket_without_prefix()

if args.setprefix:
    create_socket_with_prefix()
