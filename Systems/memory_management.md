# Linux Memory Management
[Source](https://www.youtube.com/watch?v=7aONIVSXiJ8)
## Single Address Space (Old Systems)
Simple systems have a single address space. All processes and OS share the same memory space. No memory protection.

## Virtual Memory (Current)
- System that uses address mapping
- Maps virtual addresses to physical RAM
- Also maps virtual addresses to hardware devices (PCI, GPU RAM, etc)
- Allows each process to have a different memory mapping (one process's RAM is inaccessible to other processes)
- Kernel RAM is invisible to user space processes
- Memory can be moved
- Memory can be swapped to disk
- We can map physical RAM to multiple processes (shared memory)
- Memory regions can have access permissions: read write execute

So now we have 2 address spaces: physical addresses (used by hardware), and virtual addresses (used by software).

Mapping is performed in hardware:
- No performance penalty for accessing already-mapped RAM regions
- Permissions are handled without penalty
- The same CPU instructions are used for accessing RAM and mapped hardware
- Software, during its normal operation, will only use virtual addresses

### Memory Management Unit (MMU)
Hardware responsible for mapping virtual addresses to physical addresses.
- Sits between CPU core and memory (usually integrated in CPU)
- Separate from the RAM controller
- Handles permissions
- Generates exceptions (page faults) or an invalid access (perms violation)

### Translation Lookaside Buffer (TLB)
Part of the MMU, list of mappings from virtual to physical address space in hardware. It's a physical buffer.
- Also holds permission bits
- There are a fixed number of entries in the TLB, varies by CPU.
- TLB is consulted by the MMU when the CPU accesses a virtual address:
    - If the virtual address is in the TLB, the MMU can look up the physical resource
    - If it's not, the MMU will generate a page fault exception and interrupt the CPU (does the same thing if the permissions are insufficient)

### Pages and Frames
Unit of memory sized and aligned at the page size. A page frame refers to a page-sized and page-aligned PHYSICAL memory block.

### Page Faults
CPU exception generated when software attempts to use an invalid virtual address:
- Not mapped
- Insufficient permissions
- Valid, but currently swapped out
A lot of page faults happen after a context switch.

## Kernel Virtual Memory
- Upper part of the virtual address space is reserved for the kernel, lower part is used for user space
- By default, kernel uses the top 1GB of virtual address space

## Linux Virtual Addresses
3 kinds:
- Kernel Logical Address: normal kernel address space, fixed offset
- Kernel Virtual Address: addresses in the region above the kernel logical address mapping. Used for kernel modules mem allocation, etc.
- User Virtual Address: all below the page offset, each process has its own mapping, threads share a mapping, user space processes make full use of the MMU, memory isn't contiguous, memory may be swapped out, and it can be moved.

Everytime you do a context switch, that memory map is changed (part of the overhead).

## Shared Memory
- Easily implemented with the MMU
- Simply map the same physical frame into 2 different processes
- The virtual addresses need not be the same

## Lazy Allocation
The kernel will not allocate pages requested by a process immediately. The kernel will wait until those pages are actually used. Used as a performance optimization tool.

Basically, there will be a page fault, since there won't be a mapping in the TLB, then the kernel will allocate the page and map it to the process. But the process is never aware that a page fault even happened, it's part of the normal operation of the system.

## Page Tables
- The entries in the TLB are a limited resource
- Far more mappings can be made than can exist in the TLB at one time
- The kernel must keep track of all of the mappings all of the time
- Some valid mappings may not be in the TLB, when these addresses are touched, the CPU will generate a page fault, because it has no knowledge of the mapping, only the kernel does
- When that fault happens, the page fault handler finds the appropriate mapping for the address in the kernel's page tables, then select and remove an existing TLB entry (LRU Cache is used here), then create a TLB entry for the page, then return to the user space process

## Swapping
- When memory util is high, the kernel may swap some frames to disk to free up RAM (using the MMU)
- The kernel can copy a frame to disk and remove its TLB entry
- When the process tries to access that frame, a page fault will occur, the kernel will then put the process to sleep, copy the frame from disk into an unused frame in RAM, fix the page table entry, wake the process
- We're now throttled by the block I/O bandwidth. 
- Note that when the page is restored to RAM, it's not necessarily restored to the same physical frame where it originally was located
- The MMU will use the same virtual address though, so the user space program will not know the difference.

