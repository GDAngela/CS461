.global _main
.section .text

_main:

push	%ebp
mov	%esp,%ebp

mov $0xb, %eax
mov $0xbffffda0, %ebx
lea 8(%ebx), %ecx
xorl %edx, %edx
movl $0x6e69622f, (%ebx)
movl $0x68732f, 4(%ebx)
mov %ebx, (%ecx)
mov %edx, 4(%ecx)
int $0x80

leave
ret

