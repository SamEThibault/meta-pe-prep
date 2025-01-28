# Explain in details, down to the machine language, what steps are executed after you type `ps` in the terminal
- Terminal captures input `ps` as a string and stores it in a buffer
- Shell (Bash probably) reads the input when Enter is pressed
- Shell tokenizes input string to understand what program you want to run and checks for args or options
- Shell looks for the program in its list of built-in commands, if not found, it looks for the program in the `$PATH` env variable. It locates `ps` binary in `/bin/ps` by checking the file system
- Shell uses `fork()` system call to create a new child process, which is a copy of the shell process, but it is marked for execution of a new program.
- Child process calls an `execve()` system call, passing the path of the `ps` binary (/bin/ps) and its arguments
- `execve()` replaces the child process's memory space with the code and data of the ps program
- The kernel loads the `ps` binary into memory
- The kernel maps the executable and shared libraries into the process's address space
- The kernel sets up the process's stack, heap, and registers
- The `ps` binrary's entry point is executed
- The `ps` program interacts with the `/proc` filesystem to get information about the running processes
- It uses system calls like `open()`, `read()`, and `close()` to read the information from `/proc`
- Each of these calls transition the process from user space to kernel space.
- Data requested by these system calls is retrieved from the kernel's internal process table, and formatted as a file-like structure under `/proc`. This is because `/proc` is a pseudo-filesystem: it doesn't store data on disk. Instead, files and dirs are generated on the fly by the kernel whenever they are accessed. It uses its internal process table to do this.
- Data requested by `ps` is copied from kernel space to user space
- Kernel returns control to the ps process after each system call
- `ps` program organizes the data into a table, calls `write()` system call to send data to `STDOUT`
- The terminal receives the data and converts it into a visible format using the terminal's display routines
- The `ps` program calls `exit()` system call to signal to kernel it has completed execution
- The kernel frees the process's resources, and sends a `SIGCHLD` signal to the shell process to indicate that their child process has terminated.
- The shell updates its state and displays a new prompt, ready for the next command


# You log in to your favorite OS from cold boot, you open a browser windows and type google.com and hit enter. Explain what happens NEXT in as much detail as possible

# What happens during the boot process from the moment you turn on the machine until you get a login prompt?