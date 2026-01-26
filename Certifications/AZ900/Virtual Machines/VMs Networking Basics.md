	• Azure Virtual Networks (vNETs) - fundamental for private network in Azure (like a DC in Azure Cloud)
	• vNETs enabme VMs to communicate with each other over the internet and with an on-prem DC
	• vNETs are the equivalent of a traditional IP network for a DC, but running a network in Azure

<img width="1265" height="704" alt="image" src="https://github.com/user-attachments/assets/e62f0b16-3e33-4729-b177-3c6e40f72844" />

## Availability Sets:
	• Logical grouping of two or more VMs within a DC, allowing Azure to understand how the app is built to provide redundancy/availability
	• Azure will split the fleet of VMs on different racks of servers (fault domains) preventing the app outage in case of unplanned maintenance events
	• Update domains can prevent the application outage in case of VM reboot or planned maintenance


## Virtual Machine Scale Sets (VMSS):
	• Azure VMSS let you create and manage a group of identical load balanced VMs
	• Number of VM instances can automatically increase or decrease in response to traffic demand or a defined schedule
	• For high availability, a minimum of 2 VMs should be placed in a VMSS (99.95% Azure SLA met)


## Azure Batch:
	• Enables large-scale job scheduling and compute management with the ability to scale to tens, hundreds or thousands of VMs 

