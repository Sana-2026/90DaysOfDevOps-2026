Day 02 - Linux Architecture, Processes and systemd

Goal of todays task is to understand how Linux works under the hood


What is Linux?

	Linux is an open source operating system developed by Linus Torvalds in 1991.
	Its a Unix based, shell programming language with CLI interface.

	Linux = Kernel + Tools

	What is Kernel?

	The kernel is the core (heart) of Linux.
	It is the first program loaded when Linux starts and it controls everything in the system.

	Kernel = Bridge between hardware and software

	Applications never talk directly to hardware.
	They talk to the kernel, and the kernel talks to the hardware.


   
Why Linux for devops?

	*Open Source        free to use and modify and community support available.
	*Fast and stable    can run for longer periods without any reboot.
	*Secure             no virus attacks
	*Server OS          most servers run on Linux

	Its is a multi user, multi tasking programming language.

What is User Space in Linux?
	User Space = Where users & applications live
	Kernel Space = Where the kernel lives

         User Space             
              |
    Applications (nginx, docker)   
    Shell (bash, zsh)              
    Utilities (ls, cp, ps)         
    System Libraries       
              |
       System Calls
              |
 
         Kernel Space             
              |
     Process Management              
     Memory Management               
        File System                   
            |
          Hardware             
 


What is init in Linux ?


	init = first user-space process

	PID = 1

	Started by kernel

	Parent of all processes

	👉 If init dies → system dies

🔹 Boot flow
	BIOS → GRUB → Kernel → init (PID 1) → Services → Login

🔹 Job of init
	
	Start system services

	Stop services on shutdown

	Bring system to usable state


systemd 

	🔹 What is it?

		systemd = modern init system

		Runs as PID 1

		Started by the kernel

		Manages services, boot, processes

		systemd IS init today

	🔹 Why it exists

		Old init ❌ slow, sequential
		systemd ✅ parallel, fast, dependency-aware


	🔹 Core building block

		Unit = thing systemd manages

		  Unit		Purpose
		.service	Services (nginx, docker)
		.target		System state (boot levels)
		.timer		Cron replacement
		.mount		Mount points
		.socket		Socket-based activation



Process Creation & Management (Linux)

🔹 What is a process?

	A process = running program

	Has PID, memory, CPU state, open files

	Created & managed by the kernel

How a process is created (3 steps)

	1️ fork()  → copy of parent process
	2️ exec()  → load new program into memory
	3️ wait()  → parent waits for child

	👉 Everything starts from PID 1 (systemd)

🔹 Process states 

	State	Meaning
	R	Running
	S	Sleeping
	D	Uninterruptible sleep (I/O)
	T	Stopped
	Z	Zombie (dead, not cleaned)


Process management commands

	ps aux          # list processes
	top / htop      # live view
	kill PID        # send signal
	kill -9 PID     # force kill

