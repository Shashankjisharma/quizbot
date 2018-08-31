questions = [
    ['Linux', 'Who wrote the Linux Kernel? 1 - Linus , 2 - Bill , 3 - Nikhil , 4 - Nobody', '1'],
    ['Linux', 'What file mounts a FS persistently? 1 - fstab , 2 - lvm.conf , 3 - multipath.conf , 4 - trin.conf', '1'],
    ['Indian culture', 'How many states in India?', '29'],
    ['Linux', 'Name of the penguin (Linux mascot)?', 'Tux'],
    ['Red Hat', 'Who is nkshirsa?', 'nikhil kshirsagar'],
    ['Red Hat', 'Where is Red Hat headquartered?', 'Raleigh'],
    ['General Knowledge', 'What must you do during thinpool configuration? 1 - Pray 2 - Turn autoextend on 3 - Nothing 4 - Delete and use thick lvs', '2'],
    ['Linux', 'what command lists open files?', 'lsof'],
    ['Linux', 'what state of a process in ps output implies uninterruptible sleep?', 'D'],
    ['Red Hat Cee', 'Who developed foobar?', 'Madhavprasad Pai'],
    ['General Knowledge', 'Only constant according to einstein?', 'Speed of Light'],
    ['General Knowledge', 'Who wrote The Hitchhikers Guide to the Galaxy?', 'Douglas Adams'],
    ['Linux', 'Which filesystem cannot be shrunk once created?', 'xfs'],
    ['Linux', 'LVM metadata restoration command?', 'vgcfgrestore'],
    ['Linux', 'Linux threads implemented using what library?', 'pthreads'],
    ['Linux', 'What is used to analyze application dump files (core files)?', 'gdb'],
    ['Linux', 'What is LVM using for everything it does ?', 'Device mapper'],
    ['Red Hat trivia', 'What does SOL stand for in Red Hat?', 'Support Operations Lead'],
    ['General knowledge', 'Who said talk is cheap, show me the code', 'linus torvalds'],
    ['Red Hat', 'When was Red Hat established? (month year)', 'March 1993'],
    ['General knowledge', 'When did Red Hat go Public (year)', '1999'],
    ['Linux', 'Who designed the first PCP architecture?', 'Mark Goodwin'],
    ['General Knowledge', 'Who wrote A Brief History of Time?', 'Stephen hawking'],
    ['General Knowledge', 'Default IO scheduler on RHEL 7?', 'deadline'],
    ['General Knowledge', 'Default IO scheduler on RHEL 6?', 'cfq'],
    ['General Knowledge', 'Default filesystem on RHEL 6?', 'ext4'],
    ['General Knowledge', 'Default filesystem on RHEL 7?', 'xfs'],
    ['Linux', 'Where did the name GLUSTER come from?', 'GNU and Cluster'],
    ['Unix', 'Who wrote UNIX?', 'Dennis Ritchie'],
    ['Unix', 'Who created GPL license?', 'Richard Stallman'],
    ['Gaming', 'First ever video game made popular', 'pong'],
    ['Gaming', 'First ever graphical game written for PC in pascal by broderbund software', 'prince of persia'],
    ['Gaming', 'First popular strategy fantasy game', 'dungeons and dragons'],
    ['internet', 'popular text browser in the ninties', 'lynx'],
    ['linux', 'If one of the thread in multithreaded process is blocked on an I/O, which of the following is true? 1 - the entire process will block if their is no kernel supported threads 2 - Other threads of the process will continue to execute even if there is no kernel supported threads 3 - It depends on specific implementatation 4 - All of the mentioned', '1'],
    ['internet', 'popular search engine in the ninties', 'lycos'],
    ['internet', 'popular social media site before facebook ', 'orkut'],
    ['internet', 'First online bookstore', 'amazon'],
    ['gaming', 'First first person shooter game', 'wolfenstein'],
    ['internet', 'Popular search engine in the ninties before yahoo and google', 'altavista'],
    ['linux', 'This OS was what linus torvalds used to study before developing linux?', 'minix'],
    ['linux', 'Which niceness value among the following indicate most favorable scheduling? 1 - 0 , 2 - 19 , 3 - -20 , 4 - 100', '3'],
    ['linux', 'Each process has unique ? 1 - fd table , 2 -  file table, 3 -  inode table, 4 - data block table', '1'],
    ['linux', 'The file system information is stored in? 1 - Boot block, 2 - Super Block, 3 -  inode table, 4 - data block ', '2'],
    ['linux', 'What is the use of fcntl function?? 1 -  locking a file, 2 - reading the file descriptor flag, 3 -   changing the file status flag, 4 - all of the mentioned', '4'],
    ['linux', 'The maximum time slice that can be given to a process in Linux in ms? 1 - 10 , 2 - 50 , 3 - 200 , 4 - 600', '4'],
    ['linux', 'printf() uses which system call? 1 - open, 2 - read, 3 - write, 4 - none of these', '3'],
    ['linux', 'read() system call on success returns? 1 - 0, 2 - 1, 3 -  number of characters, 4 - none of these', '3'],
    ['linux', 'Default action of SIGSEGV is? 1 - Terminate, 2 - Core dump + Terminate, 3 -  Stop, 4 - none of these', '2'],
    ['linux', 'The persistancy of a FIFO is? 1 - process, 2 - kernel 3 -  file system , 4 - none of these', '3'],
    ['linux', 'Which one of the following is not system V IPC ?? 1 - Shared Memory, 2 - Semaphores 3 -  FIFO, 4 - Message Queues', '3'],
    ['linux', 'Command used to check shared memory is?? 1 - ipcs, 2 - ipcs -m 3 -  ipcs -s, 4 - ipcs -q', '2'],
    ['linux', 'Which is Fastest IPC??? 1 - Message Queue, 2 - shared memory 3 - Socket, 4 - FIFO', '2'],
    ['linux', 'A system has 512MB of physical memory. Which among the following is not a suitable virtual memory size for this system architecture?? 1 - 512MB, 2 - 256MB, 3 -4GB, 4 - none of these', '4'],
    ['linux', 'what is thin provisioning? 1 - redundant storage 2 - journalling filesystem 3 - multiple copies of storage like raid 4 - overallocation of storage', '4'],
    ['Linux', 'What helps monitor network traffic and activity?', 'tcpdump'],
    ['Linux', 'The structure which keeps the information about shared memory in the kernel?', 'shmid_ds'],
    ['Linux', 'Which call to use to set the resource count of semaphore??', 'sem_set_count'],
    ['Linux', ' Race condition can be avoided by using?? 1 - semaphore 2 - mutex 3 - both 4 - none', '3'],
    ['Linux', 'Linux kernel is?? 1 - Monolithic 2 - Microkernel 3 - Exo 4 - none', '1'],
    ['Linux', 'Section 2 of manpage describes?? 1 - Commands 2 - System calls 3 - Function calls 4 - Drivers', '2'],
    ['Linux', 'What helps find memory leaks in a program?', 'valgrind'],
    ['Linux', 'What tool from rational helps find root causes of crashes due to memory errors?', 'purify'],
    ['Linux', 'What tool from rational is a well known versioning system?', 'clearcase'],
    ['Linux', 'Who designed and developed git?', 'linus torvalds'],
    ['Linux', 'Name of Indian supercomputer running on linux?', 'param'],
    ['Linux', 'command to search for strings in text?', 'grep'],
    ['Linux', 'virtual devices created from existing disks which can be used for testing?', 'loopback devices'],
    ['Linux', 'What happens when debugger is attached to a running process ? 1 - process terminates 2 - process is paused 3 - all threads except main threads of process are suspended 4 - process continues running normally', '2'],
    ['Linux', 'What helps sync data from one disk or file to another across a network?', 'rsync'],
    ['Linux', 'What system call does malloc call?', 'brk'],
    ['Linux', 'How many passes does C compiler make? 1 - 1 , 2 - 2 , 3 - 3 , 4 - 10' , '2'],
    ['Linux', 'Can main be called from within main in c? 1 - always , 2 - never , 3 - sometimes , 4 - only with special gcc flag' , '1'],
    ['Linux', 'What C function helps make a copy of a process?', 'fork'],
    ['Linux', 'What library is automatically linked into your compiled C program?', 'standard library'],
    ['Linux', 'COFF is a ? 1 - network protocol 2 - file format 3 - debugger 4 - newly discovered asteroid', '2'],
    ['Linux', 'What did Steve Bourne write?', 'bash'],
    ['Linux', 'What is used to monitor system calls that a process makes?', 'strace'],
    ['Linux', 'What is the term for a function calling itself?', 'recursion'],
    ['C++', 'Hidden pointer stored for virtual functions in a class in C++?', 'vptr'],
    ['C++', 'vptr points to what for implementing virtual functions in a class in C++?', 'vtable'],
    ['C++', 'Who wrote c++?','Bjarne Stroustrup'],
    ['C programming', 'typedef in C is used for? 1 - defining macros 2 - writing new code 3 - making new types 4 - none of these','3'],
    ['C programming', 'break keyword in C is used for? 1 - calling interrupts 2 - dead code 3 - exitting the program 4 - none of these','4'],
    ['C programming', 'scanf in C is used for? 1 - calling interrupts 2 - input from user 3 - exitting the program 4 - none of these','2'],
    ['C programming', 'putc in C is used for? 1 - user input 2 - output to terminal 3 - exitting the program 4 - none of these','2'],
    ['C programming', '#pragma in C is used for? 1 - user input 2 - special switch for compiler 3 - exitting the program 4 - none of these','2'],
    ['C programming', 'system function in C is used for? 1 - calling interrupts 2 - invoking binaries 3 - exitting the program 4 - none of these','2'],
    ['C programming', 'Data structure that stores similar kinds of items in C?', 'array'],
    ['C programming', 'Data structure that stores dis-similar kinds of items in C?', 'struct'],
    ['linux', 'What is a context switch? 1 - Kernel switches from executing one process to another 2 - Process switches from kernel mode to user mode 3 - Process switches from user mode to kernel mode 4 - None of the mentioned', '1'],
    ['Linux', 'What state does a process go in when debugger attached to it? 1 - sleep 2 - tracing 3 - zombie 4 - no state change', '2'],
    ['Linux', 'What command is used to count the total number of lines, words, and characters contained in a file?', 'wc'],
    ['Linux', 'What hardware architecture is not supported by Red Hat?', 'Macintosh'],
    ['Linux', 'How do you find which remote hosts are connecting to your host on a particular port?', 'netstat'],
    ['Linux', 'What command helps find how many days your Server is up??', 'uptime'],
    ['Linux', 'What command helps find hostname from ip address?', 'nslookup'],
    ['Linux', 'Which well known text editor contains an inbuilt doctor or psychiatrist?', 'emacs'],
    ['Linux', 'Parent process id of a deamon process is? 1 - 2 ,  2 - 0 ,  3 - none of these  , 4 - 1', '4'],
    ['Linux', 'ctrl-c sends which signal?', 'sigint'],
    ['Linux', 'Which function returns two values at the same time?', 'fork'],
    ['Linux', 'ctrl-z sends which signal?', 'sigtstp'],
    ['Linux', 'NTP is used to synchronize what?', 'clock'],
    ['Linux', 'What is the default maximum number of processes that can exist in Linux? 1 - 32768 2 - 1024 3 - 4096 4 - no limit', '1'],
    ['Linux', 'What command will verify the syntax of a hosts.allow and hosts.deny file combination?', 'tcpdchk'],
    ['Linux', 'Worlds largest non-commercial Linux distribution?', 'Debian'],
    ['Linux', 'How do you define a macro in C? Using what keyword?', '#define'],
    ['Linux', 'How many bytes required to store an integer on x86_64?', '4'],
    ['Linux', 'How many bytes required to store a pointer on x86_64?', '8'],
    ['Linux', 'What are the arguments passed to a C main() function called by default?', 'argc and argv'],
    ['Linux', 'What program is used to analyze a vmcore?', 'crash'],
    ['Linux', 'What is the name of our internal cee vmcore analysis server?', 'optimus'],
    ['Linux', 'What is the name of the command to build an rpm package?', 'rpmbuild'],
    ['Linux', 'What is the tool to autodownload case attachments?', 'foobar'],
    ['Linux', 'What is the tool to auto analyze sosreports for problems?', 'insights'],
    ['Linux', 'What is the tool to analyze problems related to storage performance?', 'iostat'],
    ['Linux', 'What command loads a driver at runtime?', 'modprobe'],
    ['Linux', 'This company makes device drivers for video cards, and a lot more?', 'nvidia'],
    ['Linux', 'This company tried to make their own version of linux and failed miserably?', 'oracle'],
    ['Linux', 'What is a good network protocol for audio and video?', 'UDP'],
    ['Linux', 'Microsoft cloud solution?', 'azure'],
    ['Linux', 'Red Hat cluster solution for rhel 7 ?', 'pacemaker'],
    ['Linux', 'Which of the following protocols/tools is MOST likely to be used in integrating a Linux system into a Windows network, and for accessing Windows files?', 'Samba'],
    ['General Knowledge', 'Great computer scientist, famous for his computer science concepts called machines?', 'Alan Turing'],
    ['General Knowledge', 'Great computer scientist, wrote a great book on operating systems?', 'Andrew Tannenbaum'],
    ['General Knowledge', 'What bot do I fear the most?', 'redskull'],
    ['General Knowledge', 'What do bots do when they cannot sleep?', 'count electric sheep'],
    ['General Knowledge', 'The best AI chat bot in the world?', 'quizbot'],
    ['General Knowledge', 'CEO of google, an Indian...', 'Sundar Pichai'],
    ['General Knowledge', 'What is my favorite hobby?', 'shayari'],
    ['Linux', 'First alpha release of linux in which month and year', 'January 1996'],
    ['Linux', 'Full form of l10n', 'localization'],
    ['Linux', 'Full form of i18n', 'internationalization'],
    ['Linux', 'Largest contributor to Linux Kernel?', 'Intel'],
    ['General Knowledge', 'Best selling Indian author won the Man Booker Prize for Fiction?', 'Arundhati Roy'],
    ['General Knowledge', 'Who wrote A song of Fire and Ice on which is based Game of Thrones?', 'George R. R. Martin'],
    ['General Knowledge', 'How wicked am I?', 'So wicked that this answer is something nobody can guess and so just give up already!'],
    ['Linux', 'Which command displays the list of groups to which a user belongs?', 'lsgroup'],
    ['Linux', 'EMC multipathing solution?', 'powerpath'],
    ['Linux', 'Storage protocol that completely bypasses scsi ?', 'nvme'],
    ['Linux', 'What is infiniband?', 'networking protocol'],
    ['Linux', 'used in programming to synchronize threads of a process in order to protect global data access?', 'mutex'],
    ['Linux', 'What service is used to configure and capture a vmcore?', 'kdump'],
    ['Linux', 'What does kdump internally use?', 'kexec'],
    ['Linux', 'daemon that lvm currently uses, deprecated in RHEL 8?', 'lvmetad'],
    ['Linux', 'Which filesystem supports filesystem level snapshots?', 'btrfs'],
    ['Linux', 'Name of virtual filesystem that stores process information in memory? (starts with /)', '/proc'],
    ['Linux', 'Name of encryption module used by Red Hat?', 'luks'],
    ['Linux', 'Command to manually reclaim space from SSD storage after data deleted from filesystem?', 'fstrim'],
    ['Red Hat', 'Our biggest competitor?', 'Suse'],
    ['Red Hat', 'Red Hats acquisition for kubernetes development?', 'CoreOS'],
    ['Linux', 'What must you install for getting symbols in application core files? 1 - debuginfo packages, 2 - strace , 3 - kdump , 4 - sym drivers', '1'],
    ['Linux', 'What is the command to display a backtrace in a vmcore? 1 - show, 2 - log, 3 - bt, 4 - goto', '3'],
    ['Linux', 'What is the smallest size of IO in a RHEL system? 1 - blocksize, 2 - chunksize, 3 - minimum_io_size, 4 - kblockd', '3'],
    ['me', 'On a scale of 1 to 10, how enthusiastic are folks about me? 1 - 1, 2 - 2, 3 - 5, 4 - 10', '1'],
    ['me', 'What language am I written in?', 'python'],
    ['Linux', 'Which key combination can yank a line in vi? 1 - yw, 2 - dd, 3 - yy, 4 - dy', '3'],
    ['Linux', 'Choose the correct from below to search for lines beginning with the pattern using grep 1 - ^pattern, 2 - pattern^, 3 -  $pattern, 4 - none of these', '1'],
    ['Linux', 'Which command can be used to make variables of shell to be made available to sub shell? 1 - import, 2 - export, 3 -  echo, 4 - none of these', '2'],
    ['Linux', 'The command mknod myfifo b 4 16 will create what? 1 - a block device if user is root, 2 - a block device for all users, 3 -  a FIFO if user is not root, 4 - none of these', '1'],
    ['Linux', 'Which command is used to record a user login session in a file? 1 - macro, 2 - read, 3 - history, 4 - script', '4'],
    ['General Knowledge', 'WiFi full form?', 'Wireless Fidelity'],
    ['Linux', 'What does LUKS do?', 'encryption'],
    ['Linux', 'What has the sole purpose of helping mount the root filesystem', 'initramfs'],
    ['Linux', 'Which daemon tracks events on your system?', 'syslogd'],
    ['Linux', 'Filesystem data structure which has the description of all the files and pointers to the data blocks of files stored in it?', 'inode'],
    ['Linux', 'Which command is used to check the number of files and disk space used and the each users defined quota?', 'repquota'],
    ['Linux', 'Which utility is used automate rotation of logs?', 'logrotate'],
    ['Linux', 'Which daemon is used for scheduling of the commands?', 'crond'],
    ['Linux', 'Linux kernel feature that allows to aggregate multiple network interfaces into a single virtual link?', 'Network Bonding'],
    ['Linux', 'A process is said to be in this state when it has finished execution but is waiting for its parent to retrieve its exit status?', 'zombie'],
    ['Linux', 'What will help list the services that are enabled at a particular run level in linux server ??', 'chkconfig'],
    ['Linux', 'What script is used to rescan scsi devices?', 'rescan-scsi-bus.sh'],
    ['Linux', 'In Puppet what are the files in which the client configuration is specified called?', 'manifests'],
    ['Linux', 'the average sum of the number of process waiting in the run queue?', 'load average'],
    ['Linux', 'Which files stores the user min UID, max UID, password expiration settings, password encryption method being used etc?', 'login.defs'],
    ['Linux', 'What is /etc/skel used for? 1 - copy file to new user account automatically 2 - define network topology 3 - kill particular processes 4 - none of these', '1'],
    ['Linux', 'What does echo $? do? 1 - current shell ID 2 - prints the arguments passed 3 - shows the exit status of the most previous process command  4 - none of these', '3'],
    ['Linux', 'What does echo $$ do? 1 - report PID of previous background process 2 - shows current shell ID 3 - shows the exit status of the most previous process command  4 - none of these', '2'],
    ['Linux', 'What does echo $@ do? 1 - report PID of previous background process 2 - shows current shell ID 3 - shows the exit status of the most previous process command  4 - none of these', '4'],
    ['Linux', 'What does echo $# do? 1 - report PID of previous background process 2 - shows total number of arguments passed ID 3 - shows the exit status of the most previous process command  4 - none of these', '2'],
    ['Linux', 'What does echo $! do? 1 - report PID of previous background process 2 - shows total number of arguments passed ID 3 - shows the exit status of the most previous process command  4 - none of these', '1'],
    ['Linux', 'What does echo $* do? 1 - report PID of previous background process 2 - shows total number of arguments passed ID 3 - prints arguments passed 4 - none of these', '3'],
    ['Linux', 'Command and flag used to convert ext2 file system into ext3?', 'tune2fs -j'],
    ['Linux', 'Last field of fstab is for? 1 - device 2 - filesystem type 3 - filesystem check 4 - none of these', '3'],
    ['Linux', 'In filesystems Maximum mount count is for? 1 - How many times can it be mounted 2 - after how many mounts to run fsck 3 - How many concurrent mounts 4 - none of these', '2'],
    ['Linux', ' To increase the response time and throughput, the kernel minimizes the frequency of disk access by keeping a pool of internal data buffer called? 1 - Pooling 2 - Spooling 3 - Buffer cache 4 - Swapping ', '3'],
    ['Linux', 'At start of process execution, STDOUT & STDERR 1- Point to current terminal device 2 - Are closed 3 -  Point to special files on the system 4 - None of the mentioned ', '1'],
    ['Linux', 'wtmp and utmp files contain 1 - Temporary system data 2 - User login-logout log 3 - The users command execution log 4 - The users su and sudo attempts', '2'],
    ['Linux', 'Applications communicate with kernel by using:', 'System calls'],
    ['Linux', 'Which of the following is NOT a UNIX variant ? 1 - solaris 2 - aix 3 - irix 4 - as400', '4'],
    ['Linux', 'The system calls in Linux are written using which language 1 - C 2 - C++ 3 - python 4 - perl', '1'],
    ['Linux', 'Which command is used to set limits on file size', 'ulimit'],
    ['Linux', 'How many links are created when we creat a directory file?', '2'],
    ['Linux', 'If two files on same partition point to the same inode structure they are called', 'hard links'],
    ['Linux', 'Where can I find the printer in the file structure? 1 - /etc 2 - /dev 3 - /lib 4 - printer', '2'],
    ['Linux', 'Which of the following statement is true? 1 - The cp command will preserve the meta data of the file 2 - The sort command by default sorts in the numeric order 3 - The mv command will preserve the meta data of the file 4 - The command ps will display the filesystem usage', '3'],
    ['Linux', 'What UNIX command is used to update the modification time of a file? 1 - time 2 - modify 3 - touch 4 - none of these', '3'],
    ['Linux', 'Which of the following is not a valid run-level 1 - S 2 - 0 3 - 8 4 - 1', '3'],
    ['Linux', 'The shell used for Single user mode shell is 1 - bash 2 - csh 3 - ksh 4 - sh', '4'],
    ['Linux', 'Which is the only partition mounted in Single user mode 1 - boot 2- usr 3 - root  4 - tmp', '3'],
    ['Linux', 'At the end of kernel bootstrap, which process is started?', 'init'],
    ['Linux', 'Which file is read by init to get the default runlevel', 'inittab'],
    ['Linux', 'Which of the following statement is FALSE ? 1 - Unix supports multiple users 2 - Linux is an open source operating system and the source code is shared 3 - Shell takes care of inter process communication 4 - Shell provides the feature of I/O Redirection', '3'],
    ['Linux', ' If a program executing in background attempts to read from STDIN 1 - It is terminated 2 - Its execution is suspended 3 - STDIN is made available to it 4 - None of the mentioned', '2'],
    ['Linux', 'When a child process exits before the parent process exits, which of the following is true: 1 -  the child process becomes defunct 2 -  the parent process becomes defunct 3 -  if the parent process does not handle SIGCHLD, the child process becomes a zombie 4 - none of the mentioned', '3'],
    ['Linux', 'srwxr-xrw- is a 1 - internet socket file 2 -  unix domain socket file 3 - symbolic link 4 - shared file', '3'],
    ['Linux', 'Which of the following is not a valid file type on Linux 1 - Socket 2 - Softlink 3 - Inode 4 - FIFO', '3'],
    ['Linux', 'Which are the two types of device files? 1 - Character & Block 2 - Character & Socket 3 - Block & FIFO 4 - Input & output', '1'],
    ['Linux', 'The encrypted password of a user is stored in 1 - /etc/shadow 2 - /etc/enpasswwd 3 - /etc/.passwd 4 - /etc/passwd', '1'],
    ['Linux', 'User id 0 is 1 - An invalid user id 2 - The id of the root user 3 - The id of a user when the users account is deleted 4 - None of the mentioned ', '2'],
    ['Linux', 'By default, a Linux user falls under which group? 1 - staff 2 - others 3 - same as userid 4 - system', '3'],
    ['Linux', 'What will be output of following command: $ echo "The process id is" $$$$ 1 - The process id is $$ 2 - The process id is $<pid>$<pid> 3 - The process id is <pid><pid> 4 - The process id is $$$$', '3'],
    ['Linux', 'The file permission 764 means: 1 - Every one can read, group can execute only and the owner can read and write 2 - Every one can read and write, but owner alone can execute 3 - Every one can read, group including owner can write, owner alone can execute 4 - Every one can read and write and execute', '3'],
    ['Linux', 'Sticky bit can be set using following permission 1 - 0777 2 - 2666 3 - 4744 4 - 1711', '4'],
    ['Linux', 'A user does a chmod operation on a file. Which of the following is true? 1 - The last accessed time of the file is updated 2 - The last modification time of the file is updated 3 - The last change time of the file is updated 4 - None of the mentioned', '3'],
    ['Linux', 'If the umask value is 0002. what will be the permissions of new directory 1 - 777 2 - 775 3 - 774 4 - 664', '2'],
    ['Linux', 'What does chmod +t do? 1 - wrong syntax 2 - set effective userid for filename 3 - set effective groupid for filename 4 - set the sticky bit', '4'],
    ['Linux', 'Which of the following umask settings doesnt allow execute permission to be set by default on directory files 1 - 222 2 - 111 3 - 000 4 - 444', '3'],
    ['Linux', ' While executing a command, the shell 1 - Executes it in the same process (as shell) 2 - Creates a child shell to execute it 3 - Loads a special program to take care of the execution 4 - None of the mentioned', '2'],
    ['Linux', 'Which command is used to debug a shell script program 1 - set 2 - set -x 3 - debug 4 - db', '2'],
    ['Linux', 'For every successful login, which script will be executed? 1 - /etc/inittab 2 - /etc/profile 3 - /etc/login 4 - /etc/init', '2'],
    ['Linux', ' Which of the following is true? 1 - Shell is a process and can be started by superuser only 2 - Shell is a built-in Kernel functionality 3 - Shell is a wrapper for all the commands and utilities 4 - None of the mentioned', '3'],
    ['Linux', 'BASH shell stands for? 1 - Bourne-again Shell 2 - Basic Access Shell 3 - Basic to Advanced Shell 4 - Big & Advanced Shell ', '1'],
    ['Linux', 'The redirection 2> abc implies 1 - Write file 2 to file abc 2 - Write standard output to abc 3 -  Write standard error to abc 4 -  None of the mentioned ', '3'],
    ['Linux', 'cmd 2>&1 > abc will 1 - Write file2 to file1 2 - Write standard output and standard error to abc 3 - Write standard error to abc 4 - Write standard output to abc & standard error to monitor', '4'],
]
