## Overview:
	- Managed Cloud-based network security service that protects Azure vNET resources
	- Can use to grant access to resources in a vNET based on IP Address
	- Only the specified IP is allowed into the internal resource
	- Access is permitted/denied through firewall rules
		○ Can specify IP ranges

  <img width="1766" height="787" alt="image" src="https://github.com/user-attachments/assets/9aa272a0-9ada-4c66-b496-bb936a063f99" />

## DoS and DDoS:
	- Denial of Service is a type of attack that aims to overwhelm a network resource by sending lots of requests, so the resource becomes slow/unresponsive
	- Distributed Denial of Service -  multiple systems flood bandwidth or resources of a system, usually 1 or more web servers
	- Azure DDoS protection provides defense against DDoS attacks

## Azure DDoS Service Tiers:
	- Basic
		○ Enabled by default
		○ Always-on traffiv monitoring and real-time mitigation of common network-level attacks
		○ Free
	- Standard
		○ Advanced mitigation capabilities
		○ Can mitigate volumetric attacks, protocol attacks and application layer attacks
		○ Price is based on usage, on a monthly basis

## DDoS Attacks:
	- Volumetric Attacks
		○ Victim is flooded (at network layer - IP) with a high amount of traffic that seems to be legit
	- Protocol Attacks
		○ Attacks target at layer 3 and 4 protocol stack
		○ Common example: SYN flood attacks (TCP, Layer 4)
	- Application Layer Attacks
		○ Target Web Applications
		○ Common examples: SQL injection, cross-site scripting

