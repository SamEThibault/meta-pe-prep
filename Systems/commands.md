# List of Important Linux Commands

# NETWORKING
### `hostname`
Used to view / temporarily set the hostname of the machine

### `host`
Used to find a DNS name attached with an IP (host 8.8.8.8) or vice versa (host google.com).

### `ping`
Used to check if the remote server is reachable or not. Can set num of packets to send: `ping -c 4 google.com`

### `curl`
Used to stransfer data from or to a server, can also be used for network troubleshooting. Supports protocols such as HTTPS, FILE, FTP, SCP...
Check for headers: `curl -I google.com`
Check content: `curl -v google.com`

### `wget`
Used to fetch web pages.

### `ip` or `ifconfig`
ip command is newer, used to display and manipulate routes and network interfaces.
`ip addr`: Get IP addresses of network devices
`ip a show eth0`: Get details of specific device
`ip route`: List routing tables

### `arp`
Address Resolution Protocol: shows the cache table of local network's IP and MAC addresses that the system interacted with.

### `ss` or `netstat`
ss command is newer, used to list TCP, UDP, and Unix socket connections. Usually, I use flags `-tulpn` (only listening, show process, show UDP).

### `traceroute`
Network troubleshooting utility used to track packet hops.

### `mtr`
Combines ping and traceroute, sends packets regularly and measures average response times, and its routes

### `dig`
Queries DNS name servers: `dig google.com` returns DNS records and TTL info.
It also does reverse DNS lookup: `dig -x 8.8.8.8`

### `nslookup`
Similar to dig, `nslookup google.com`, and it does reverse lookups as well.

### `nc`
Netcat allows you to check connectivity of a service running on a specific port.
Check is ssh port is open: `nc -v -n 8.8.8.8 22`

### `telnet`
Used to troubleshoot TCP connections on a port: `telnet 8.8.8.8 22`

### `tcpdump`
Used to analyze network traffic.
Can capture packets on specific interface and port: `sudo tcpdump -i eth0 port 80`

### `lsof`
Lists all open files.
To find PID associated with a port: `lsof -i :PORT_NUMBER`

### `sar`
Shows network stats and load: `sar -n DEV 1`.
Can also show TCP connection metrics: `sar -n TCP,ETCP 1`.

### `ufw`
(Uncomplicated Firewall), used to check and configure firewall rules.
Check basics: `sudo ufw status verbose`

### `iptables`
Used to view current firewall rules: `iptables -L`

# PROCESSES
### `ps`
Used to monitor running processes. 
To show the most relevant info: `ps aux`
For a specific process: `ps aux | grep <processName>
To find zombie processes: `ps aux | grep Z`

### `strace`
Used to trace system calls and signals made by a process.
Attach to a process: `strace -p <PID>`.

### `gdb`
GNU debugger.
Set breakpoints for signal handling: `gdb -p <PID>`, then `catch signal <SIGNAL>`

### `kill` or `pkill`
Used to kill processes by PID or name: `kill -9 <PID>` or `pkill -f <processName>`

# DISK
### `lsblk`
Lists information about storage devices

### `mount`
Mounts devices: `mount /dev/sda2 /mnt`

### `df`
Used to analyze file system and check storage: `df -ah` For all info in human readable format.

### `du`
used to check directory size: `du -sh`

### `iostat`
Used to get more I/O information: `iostat -xz 1` shows read/write loads, await times, avg number of requests, and device util

### `stat`
Used to show file i-node data: `stat file.sh`

# CPU
### `uptime`
Used to show load / demand averages (# processes wanting to run) in 1, 5, and 15min load averages.

### `mpstat`
Used to show CPU time breakdowns on a core granularity.
`mpstat -P ALL 1` for info on all cores

### `top` or `htop`
Used to show top processes by CPU usage.

### `pidstat`
Similar to top, but prints rolling summary instead of clearing the screen: `pidstat 1`

### `perf`
Used for a bunch of stuff: profiling, configuration
To record CPU cycles for entire system for 10sec: `perf record -a sleep 10`

# MEMORY
### `free`
Used to show memory stats to analyze buffers and page cache: `free -m`

# GENERAL
### `systemctl`
Used to view/control services. (status, enable, disable, start, stop, restart, ...)
To reload all system config files: `sudo systemctl daemon-reload`
To power off: `sudo systemctl poweroff`
To reboot: `sudo systemctl reboot`
To view processes: `sudo systemctl list-unit-files`

### `ulimit`
Used to find shell resource limits: `ulimit -a`

### `dmesg`
Shows system messages from the kernel ring buffer: `dmesg | tail`

### `vmstat`
Used to show virtual memory start, prints summary of key server statistics:
- r: num processes waiting for CPU
- free: free memory in KB
- si, so: swap-ins and outs
- Breakdowns of CPU time across all CPUs
`vmstat 1`

### `lsmod`
Used to list currently loaded modules

### `modprobe`
Used to load a module dynamically: `sudo modprobe wifi`, for example. use -r to remove.


# LOGS
There's a few key areas where useful files can point to some important information:
- `/var/log/` has logs for loads of services if they have been configured
- `/proc/<PID>/status` file contains the info that the task_struct of the process holds.
- `grep -i oom /var/log/messages` checks to see if any OOM faults occured.

### `journalctl`
Used to view logs of various processes: `journalctl -u service.service`
If you know the PID: `journalctl _PID=<PID>`
View errors: `journalctl -p err`