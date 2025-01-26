# The Basics (and common interview questions)
Checking which kernel version:	uname

Checking a system's current IP address:

	ip addr show, or specify device name (interface), and then IPv4 and v6 will be present

Checking for free disk space:

	df -ah (disk free, all file systems, human readable)

Checking size of dir:

	du -sh code/ (disk use)

Checking for open ports:

	netstat -tulpn

Check CPU usage of given process:

	ps aux | grep processName, or use top

Mounting a new drive:

	mount /dev/sda2 /mnt (device, and mount location)

How to get more info about a command:

	man

Check which disks are currently mounted:

	df or lsblk

## What happens in linux, on a kernel level, when you type in ls -l
    - Bash checks for alias for ls, assuming there isn't shell will search for the binary in the $PATH dirs.
    - ls is found in /bin/
    - Shell will fork to create a child process, then execve to run the executable, then will use waitpid to wait for the process to finish (parent shell process is in blocked state)
    - the child will run stat, lstat system calls to list details
    - Once child finished, waitpid will signal parent process to resume

## Troubleshooting application not starting
    - Check perms
    - Check logs
    - Check if application is compiled for the architecture: Use objdump or file utility and compare processor info using uname
    - If dynamically linked, check if interpreter is present on the system

## Linux Memory Allocation
    - Virtual memory is used to provide processes with the illusion of having more memory than is physically available

    - Each process gets its own virtual address space, which the kernel maps to physical memory as needed

    - Demand paging: Only parts of the program that actively accessed are loaded into RAM. If the program accesses parts of its memory that are not in physical RAM, the system will load those pages on demand

    - Swap space: If the system runs out of physical RAM, it moves less-used pages to swap space on the disk. That swap space can be a dedicated partition or a swap file

    - Although slower than RAM, swap allows the system to handle workloads that exceed physical memory

    - Page swaps use the Least Recently Used (LRU) algorithm. 

    - Thrashing: If the actively used memory is much larger than physical RAM, system might spend most of its time swapping pages in and out of RAM, severely degrading performance

    - If we get to a point where RAM and swap are not enough, OOM killer (out of memory) can terminate processes.

## Default signal that is generated when sending a kill command to a process
    - SIGTERM: signal termination, allows process to complete shutdown. It requests the process to terminate gracefully, then SIGKILL can be used to forcefully terminate a process, this can't be caught or ignored.

## Inodes:
    - data structure used to store metadata about a file or dir. Each file or dir has a unique inode

    - use ls -i to display inode number of a file, and stat to view detailed inode metadata

#### Random Fact:  $? in Bash: means "was the last command successful?" 

## Zombie Process: 
    Completed child process waiting for reaping by the parent process. They exist as an entry in the process table. Zombies are dead and mostly completed processes that do not take memory or CPU resources. They occur when the parent hasn't read its exit status using a system call like wait().
We can use: `ps aux | grep Z` to find zombie processes

## Kernel Modules
    - Can be loaded at boot time, or when needed

    - To view loaded module: lsmod | less

    - modinfo module_name gives more info about the module, including its dependencies

    - In /lib/modules, there's folders for each kernel architecture, cd into that, and in the kernel folder, there's folders for all the types of modules

    - Unloading modules: sudo rmmod module_name

    - Adding modules: sudo insmod <pathname.ko>

    - Alternatively, you can use modprobe module_name to add a module, which is better since you can use the module name instead of its absolute path

    - To remove one, you can do modprobe -r module_name

## What's a signal
    - Mechanism for processes to communicate with each other or to be notified by the OS about events. Signals are used to interrupt a process and notify to perform a specific action, like terminate or handle an event.

    - Example: SIGTERM (15), SIGKILL (9), SIGINT (2)

    - Example usage: kill -9 <process_id>, or kill -SIGTERM <process_id>

    - How it's handled by the kernel: kernel checks the signal number, see if it can be caught or ignored, if not, check if a handler is present, otherwise complete the default action

    - When a signal arrives, either:
        ○ Signal is ignored: discarded by the kernel and the process doesn't get notified anything
        ○ Process is terminated abnormally
        ○ A core dump file is generated and the process is terminated
        ○ The execution of the process is suspended or resumed

    - Interrupt vs signal: communication between CPU and kernel, vs communication between kernel and processes

## When a child process terminates
    - Signal SIGCHLD is sent to the parent

    - Default behavior is to ignore it, but parent can set up a handler that catches the signal, calls wait(), which picks up the status of the child and returns immediately (which ensures the child doesn’t remain a zombie process)

#### Fun Fact: IPv6, what is the A record equivalent: AAAA record

## System call
    - Way for computer program to ask the OS to perform an action which it wouldn't have permission to do in user mode (file accesses, I/O, Main memory management, networking etc…)

    - When a process makes a system call: 
        ○ OS switches from user mode to kernel mode (mode switch)
        ○ OS performs the operations requested
        ○ OS gives control back to the program  (mode switch)

## Strace
    - Debugging tool to trace system calls and signals made by a process

    - Strace <process you want to trace>

    - To attach it to a running process: strace -p <PID>

    - Works by using the ptrace system call which causes the kernel to halt the program being traced each time it  does a mode switch. Strace can then inspect the state of the program 

## Ways to catch a signal for a program without its source code
    - Strace

    - Gdb (GNU debugger), set breakpoints for signal handling: gdb -p <PID>, then "catch signal <SIGNAL>"

    - Cat /proc/<PID>/status , then check for SigCgt (signals caught) and SigIgn (signals ignored)

    - Perf can monitor signal-related events

## Containerization
    - Packaging of software with just the OS libraries and dependencies required to run the code to create a single lightweight executable (container) that runs consistently on any infrastructure

    - Abstracts host OS away

    - They're lightweight: they share the machine's OS kernel and don't require the overhead of associating an OS within each application. (this is somewhat true, for example, if you're on a Unix host, then yea you can containerize a different distro and it will use the host kernel directly. But if you're trying to containerize a linux distro on a windows machine, then they employ VM-like techniques and this doesn't really apply anymore)

## Virtualization
    - Uses a hypervisor: a software layer placed on a physical computer or server that allows the physical computer to separate its OS and applications from its hardware

    - Each application and its related file system, libraries and other deps are packaged together as a VM.

## Daemonize a Linux process:
    - Call os.setsid()

    - The process becomes the leader of  new session, breaking away from the existing session and its controlling terminal.

## Making a process a service
    - Create a service file: /etc/systemd/system/myfile.service

    - Reload systemd: sudo systemctl daemon-reload

    - Start the service: sudo systemctl start myfile

## System call vs context switch
    - Sys call: request made by a user-space program to the kernel to perform privileged operations (requires mode switch), low overhead

    - Context switch: the process of saving the state of one process or thread and switching to another, involves saving/restoring registers, stack pointers, program counters, etc…, so higher overhead

## Filesystem
    - methods and data structures that an OS uses to keep track of files on a disk or partition (the way the files are organized on the disk).

    - Central Concepts:
        ○ Superblock: info about the filesystem as whole, such as size
        ○ Inode: all info about a file, except its name (the name is stored in dir, together with the inode #). It contains several Data block #s
        ○ Data block: used to store the data from a file
        ○ Directory block: entries with filenames and their associated inode number
        ○ Indirection block: there is only room for a few data block numbers in an inode, but you can point to more dynamically. So an indirection block contains pointers to additional data blocks.

# How does the system call go from user to kernel space
    - User program makes a system call using a library of predefined functions

    - The function prepares the call: sets up args and the system call number

    - A CPU software interrupt is executed (trap), which causes the CPU to switch from user mode to kernel mode

    - The CPU jumps to a predefined entry point in the kernel, typically an interrupt vector or a system call handler, which is determined by the system call number

    - The kernel function performs the requested operation

    - The kernel returns control to the user process with the result of the system call, and the CPU switches back to user mode
    
## Soft vs Hard link
    - Both are ways to reference files in a filesystem

    - Soft Link: Symbolic Link, a special type of file that contains a path to another file or dir
        ○ Acts as a shortcut to the og file
        ○ Breaks if the og file is deleted or moved, since it points to the path, not the data
        ○ ln -s /path/to/og /path/to/link

    - Hard Link: direct reference to the same inode as the og file:
        ○ Points to the same data blocks
        ○ Remains valid even if og file is delete, as it references the same inode
        ○ ln /path/to/og /path/to/link

## Files
    - Permissions: perms are defined for 3 categories of users and control 3 types of operations:
    - Users Categories:
        ○ Owner (User)
        ○ Group: group of users who share access
        ○ Others: everyone else
    - Permission Types:
        ○ r
        ○ w
        ○ x

    - Execute is 1

    - Changing perms: chmod 755 file.txt

    - Changing ownership chown user:group file.text

## Systemd
    - system and service manager.

    - Responsible for bootstrapping the user space and managing system services. It replaces olde r init systems

## Systemctl
    - command line tool used to interact with systemd, allows you to manage and control services, units, and the system's overall state

    - view logs: journalctl -u service.service

    - Reboot: sudo systemctl reboot

    - Shutdown: sudo systemctl poweroff

## Init system
    - first process started by kernel after the system boots.

    - Responsible for initializing user space and starting essential processes (operates as PID 1) and remains running as the parent process for all other processes

## Killing a zombie process
    - You can't kill it directly: it's already dead. But you can clean it up by terminating the parent, which will make PID 1 inherit the zombie process and wait on it and clear its entry in the process table

## How Linux manages virtual memory
    - Each process has its own virtual address space, which includes text segment, data segment, heap and stack

    - MMU (memory management unit) in the CPU translates virtual addresses to physical ones using page tables and page sizes

    - Memory is divided into fixed-size pages (virtual) and frames (physical)

    - Linux uses demand paging

    - Kernel space: shared and mapped identically for all processes, handles OS functions
    
    - User space: private for each process
