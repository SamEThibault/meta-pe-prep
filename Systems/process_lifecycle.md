# UNIX Process Lifecycle
A process can be running or idle.

- It can be in the "new" state, where the OS allocates and initiates a process control block (PCB) for it.
- It can be in the "ready" state, meaning it has not been dispatched to the CPU.
- It can be in the "running" state, meaning it is currently executing.
- It can be in the "waiting" state, meaning it is waiting for an event to occur.
- It can be in the "terminated" state, meaning it has finished executing.