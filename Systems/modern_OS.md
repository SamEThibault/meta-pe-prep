# Modern Operating Systems
Notes from Andrew S. Tanenbaum's book "Modern Operating Systems", specifically, Chapter 10 case study of Linux.

## Interfaces to Linux
![alt text](image-1.png)

Programs make system calls by putting the arguments in registers, or sometimes on the stack, and issuing trap instructions to switch from user mode to kernel mode. Since there is no way to write a trap instruction in C, a library is provided, with one procedure per system call. These are written in assembly, but can be called from C.

There are technically 3 kinds of interfaces to Linux: the true system call interface, the library interface, and the interface formed by the set of standard utility programs.

## Bash Shell
Commands may take args, which are passed to the called program as character string. For example:
`cp src dest`
invokes the cp program with 2 args: src and dest. The way the program handles these args is up to the program.

Arguments that control the operation of a command or specify an optional value are called flags, and by convention are indicated with a dash. 

Wildcards: `*` matches any string of characters, `?` matches any single character, `[...]` matches any one of the characters inside the brackets.
For example: `ls [ape]*` lists all files that start with a, p, or e.

(page 727)