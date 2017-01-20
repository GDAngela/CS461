.global your_asm_fn
.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp

push    0x00c105ed 
mov     %esp,%eax 

push    0x11111111
push    0x11111111
push    0x00 

push    %eax 
push    0xacce55ed

call    practice  


leave
ret
