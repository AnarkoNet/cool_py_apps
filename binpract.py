from random import randint as rng
import os
os.system("clear")
start="Binary Practice (press q to quit)\n 128 64 32 16  8  4  2  1\n   0..0..0..0..0..0..0..0\n   192 96 48 24 12  6  3"
start="Binary Practice (press q to quit)\n  0...0...0...0...0...0...0...0\n128  64  32  16   8   4   2   1\n  192  96  48  24  12   6   3\n    224 112  56  28  14   7\n      240 120  60  30  15"
print(start)
num=rng(0,255)
bnm=bin(num)[2:]
bnm=("0"*(8-len(bnm)))+bnm
xnm=("0"+hex(num)[2:])[-2:].upper()
inp=input("What is \x1b[96m"+str(num)+"\x1b[0m? -> ")
while inp.lower()!="q":
    os.system("clear")
    print(start)
    print("What is \x1b[96m"+str(num)+"\x1b[0m? -> "+inp)
    if inp.replace("0"," ").lstrip()==bnm.replace("0"," ").lstrip():
        print("  0b\x1b[92m\x1b[92m"+bnm+" \x1b[0m0x\x1b[92m"+xnm)
    else:
        print("  0b\x1b[91m"+bnm+" \x1b[0m0x\x1b[91m"+xnm)
    num=rng(0,255)
    bnm=bin(num)[2:]
    bnm=("0"*(8-len(bnm)))+bnm
    xnm=("0"+hex(num)[2:])[-2:].upper()
    inp=input("\x1b[0mWhat is \x1b[96m"+str(num)+"\x1b[0m? -> ").lower()