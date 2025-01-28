# Common Troubleshooting scenarios

## DB with Slow I/O, how can we improve it?
- Physical improvements: Upgrade I/O device that stores DB, Add RAM (better caching capabilities)
- Software improvements: Look for possible optimizations with queries, indexes, etc...
- Network improvements: Check network latency, packet loss, etc...
- Look into Batching queries
- Look into partitioning large tables
- Look into caching
- Look into table or column compression to reduce size of on-disk data
- Look into horizontal scaling: replication, sharding...
- Check DB config: adjust buffer sizes, etc...

## How would you troubleshoot a system in which you are not able to start an application on the server?
- Check logs: app logs: `journalctl`, sys logs: `dmesg`
- Check resource availability: `top` or `free` or `df -h` to check CPU, memory, and disk/swap usage, `ulimit -n` to check # available file descriptors
- Check for any missing environment variables, or dependencies/external services that the app relies on: systemctl status <service> to check their states
- Check perms on app files and dirs: `ls -l`, ensure user attempting to run the app has sufficient perms
- If application requires external network resources, check network connectivity: `ping`, `curl`, DNS resolution: `nslookup`, or firewall rules that might block communication `ufw status`
- Try starting the app (through systemctl or directly through bin) and check journalctl for any errors (journalctl -u <service>)
- Ensure the application is not trying to bind a port already in use: `netstat -tulnp`
