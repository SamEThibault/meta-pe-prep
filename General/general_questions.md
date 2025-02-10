# General Questions
These questions test one's understanding of the Linux process lifecycle, system calls, the boot process, and general internet networking protocols.

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
- Each of these calls transition the process from user space to kernel space (mode switch).
- Data requested by these system calls is retrieved from the kernel's internal process table, and formatted as a file-like structure under `/proc`. This is because `/proc` is a pseudo-filesystem: it doesn't store data on disk. Instead, files and dirs are generated on the fly by the kernel whenever they are accessed. It uses its internal process table to do this.
- Data requested by `ps` is copied from kernel space to user space
- Kernel returns control to the ps process after each system call
- `ps` program organizes the data into a table, calls `write()` system call to send data to `STDOUT`
- The terminal receives the data and converts it into a visible format using the terminal's display routines
- The `ps` program calls `exit()` system call to signal to kernel it has completed execution
- The kernel frees the process's resources, and sends a `SIGCHLD` signal to the shell process to indicate that their child process has terminated.
- The shell updates its state and displays a new prompt, ready for the next command


# You log in to your favorite OS from cold boot, you open a browser windows and type google.com and hit enter. Explain what happens NEXT in as much detail as possible
- Browser parses the URL and determines this is a URL and not a search query.
- It then checks if the resource for google.com is cached in the browser's cache. 
- Assuming no cache hit, the browser asks the OS for the IP address. 
- The OS checks its DNS cache
- Assuming no cache hit, the OS forwards the query to a DNS resolver (usually the one provided by the ISP)
- The DNS resolver begins querying the DNS hierarchy: root nameserver -> TLD nameserver -> authoritative nameserver -> returns IP for google.com
- The OS receives the IP address and forwards it to the browser
- The browser initiates a TCP connection to that IP addr through port 443 (HTTPS)
- The 3-way handshake is performed: SYN (client) -> SYN-ACK (server) -> ACK (client)
- This encrypts the communication using SSL/TLS, the client and server agree on a cipher suite, and exchange keys, and the client verifies the server's certificate during this handshake. 
- Now we have an encrypted channel between the client and server, so the client now sends an HTTP GET request to the server. 
- The request hits one of google's load balancers, which forwards the request to one of google's servers.
- The web server processes the request, retrieves the homepage, and returns the HTML content to the client in the form of a 200 OK response.
- The browser begins parsing the HTML document line by line.
- It will probably encounter links to additional resources (CSS, JS, images), and it will start fetching these resources.
- The browser's rendering engine converts the parsed HTML and CSS into a visual representation of the page.
- It might execute JS code.
- Once all resources are fetched and the page is rendered, the browser displays the page to the user.


# What happens during the boot process from the moment you turn on the machine until you get a login prompt?
- PSU supplies electrical power to the motherboard and other components
- POST: basic I/O system (BIOS) or UEFI firmware performs a POST to verify the basic functioanlity of hardware components like CPU, RAM, and storage devices.
- BIOS/UEFI firmware initializes hardware components and prepares the system for booting an OS
- It identifies the configured boot order and selects the first bootable device
- It reads the boot sector for the selected boot device, which contains the bootloader
- The bootloader is loaded into memory, it loads the OS kernel into memory and transfers control to it
- The kernel initializes hardware drivers, detects devices, and configures hardware
- It mounts the root filesystem to access system files and scripts (needed to run the init process)
- It executes the init process (systemd).
- The init process runs ititialization scripts and starts system services
- A virtual console TTY is displayed with a login prompt
