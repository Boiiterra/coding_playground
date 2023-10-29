section  .data
nline    db 10
nlinelen equ $-nline
msg      db  'This is quite interesting', 10; 10 -> '\n'; new-line
msglen   equ $-msg

section .text
global  _start

%imacro write_stdout 0
mov     eax, 4
mov     ebx, 1
%endmacro

func:
	write_stdout
	mov ecx, msg
	mov edx, msglen
	add edx, -5
	int 80h
	ret

_start:
	write_stdout
	mov ecx, msg
	mov edx, msglen
	int 80h

	call func

	write_stdout
	mov ecx, nline
	mov edx, nlinelen
	int 80h

	mov eax, 1
	mov ebx, 0
	int 80h
