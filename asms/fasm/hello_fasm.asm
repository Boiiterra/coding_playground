; Made with some help from Tsoding <3
format ELF64 executable

SYS_write = 1
SYS_exit = 60
STDOUT = 1

macro write fd, buf, count
{
	mov   rax, SYS_write
	mov   rdi, STDOUT
	mov   rsi, msg
	mov   rdx, msg_len
	syscall
}

macro exit code
{
	mov   eax, SYS_exit
	mov   rdi, code
	syscall
}

segment readable executable
entry   main

main:
	repeat 5
		write  1, msg, msg_len
	end    repeat
	exit   0

segment readable writeable
	msg     db "Hello there", 10
	msg_len = $ - msg
