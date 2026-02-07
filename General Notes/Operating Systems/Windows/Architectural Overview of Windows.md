The architecture of Windows, particularly the NT (New Technology) kernel line which underpins all modern versions (from Windows NT 3.1 to Windows 11), is a sophisticated hybrid kernel design.

## Kernel Mode vs. User Mode
A fundamental concept in Windows architecture is the distinction between Kernel Mode and User Mode:
	• Kernel Mode: This is a privileged mode of operation where the code has direct and unrestricted access to all hardware, system memory, and operating system resources. The Windows Executive (the NT kernel and its components) runs in kernel mode. Errors in kernel-mode code can lead to system crashes (e.g. BSOD).
	• User Mode: This is a less privileged mode where application programs, user-level services, and most parts of the Windows shell operate. User-mode processes have limited access to hardware and memory, which is mediated by the kernel. If a user-mode application crashes, it typically does not bring down the entire operating system.
	
## Key Components of the Windows Executive (NT Kernel)
The Windows Executive is a collection of core operating system components that run in kernel mode:
	• Hardware Abstraction Layer (HAL): This layer virtualizes hardware, abstracting away the differences between various hardware platforms. This allows the core OS components to be written in a more generic way, making Windows portable across different processor architectures and hardware configurations.
	• Kernel (NTOSKRNL.EXE): The core of the operating system, responsible for fundamental OS services such as thread scheduling, interrupt handling, multiprocessor synchronization, and trap dispatching.
	• Memory Manager: Manages virtual and physical memory, implementing paging, memory protection, and cache management.
	• Process Manager & Thread Manager: Responsible for creating, terminating, and managing processes and threads, including their scheduling and synchronization.
	• I/O Manager: Manages input/output operations for connected devices, providing a framework for device drivers and handling device-independent I/O.
	• Plug and Play Manager: Detects and configures hardware automatically, loading appropriate drivers without user intervention.
	• Power Manager: Manages power states of the system and individual devices to conserve energy.
	• Security Reference Monitor (SRM): Enforces security policies, performing access validations for objects and resources.
	• Configuration Manager (Registry): Manages the Windows Registry, a hierarchical database that stores configuration settings and options for the operating system and installed applications.

