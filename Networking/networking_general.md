# General Questions and Concepts Surrounding Computer Networking
Router: Device that forwards data packets between computer networks. They perform the traffic directing functions on the internet. 

How does a computer know where to send packets:
- Destination IP addr: obtained via DNS resolution of a domain name
- Subnet Mask and Gateway: the OS checks if the destination IP is in the same subnet as the source IP. If not, it sends the packet to the default gateway (router). If it is, the packet is sent directly usng ARP (address resolution protocol) to resolve the MAC address of the destination IP.
- Routing Table: The source computer maintains a routing table that maps IP ranges to network interfaces or gateways. The OS uses this table to determine where to send packets.

How to packets move across a network:
- The app layer generates data
- The transport layer segments the data and adds a port number (TCP/UDP)
- The network layer (IP) adds the destination and source IP addresses
- The link layer (Ethernet/WIFI) adds MAC addresses and prepares the frame for transmission
- If destination is within the same network, packet is sent directly to the destination's MAC address.
- If not, the packet is sent to the router.
- The router examines the packet's destination IP addr, and uses its routing table to determine the next hop (another router or the final destination)
- Packets traverse multiple routers (hops) across the internet backbone
- Once the packet reaches the destination's subnet, the final router sends it to the target device by resolving its MAC address

Masks and Subnets:
- subnet: logical subdivision of an IP network. Allows for organizing and segmenting a network to improve efficiency, enhance security, and simplify routing by limiting broadcast domains.
- subnet mask: 32-bit number (IPv4) that defines which part of an IP address identifies the network and which part identifies the host. For example, /24 means the first 24 bits are the network address, and the remaining 8 bits are the host address.

Stopping people on a wireless network that you're also on from hogging bandwidth by streaming videos:
- Packet Flooding (Denial of Service): aireplay-ng to send deauth packets to the target device, forcing it to disconnect and reconnect to the network. This can be automated with a script.
- ARP Spoofing (Man-in-the-middle-attack): Tools like Ettercap or Bettercap can be used to perform ARP spoofing, rerouting the traffic of speicifc devices through your machine. Once you're the middleman, you can throttle the bandwidth of the target devices, or block requests to streaming services.
- DNS Manipulation: You cna block streaming services by redirecting their domains to invalid addresses. 

`tcpdump`:
- Command-line packet analyzer. It allows the user to display TCP/IP and other packets being transmitted or received over a network to which the computer is attached.
- Used for network troubleshooting, security analysis, protocol debugging, traffic monitoring

TCP Congestion control:
- Congestion WIndow: a sender-maintained varaible that dictates the maximum amount of data that can be sent without waiting for ACK
- Slow Start Threshold: Determines the boundary between the slow start and congestion avoidance phases. 
- Round-Trip Time (RTT): Time it takes for a packet to travel from the sender to the receiver and back. It influences retransmission timeouts and adaptive adjustments.

