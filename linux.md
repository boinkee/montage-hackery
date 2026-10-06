# Linux 
* linux kernel boots. 
* To load the kernel, 
~~~
usb start # we usin usb
fatload usb 0:1 0x83000000 uImage
bootm 0x83000000
~~~
Example booting (without the rootfs)
~~~
U-boot# usb start
(Re)start USB...
auto_detect_usb_port --- usb default sel port 1
port_sts0:0x0c000000 port_sts1:0x00000803 next scan port:0
auto_detect_usb_port --- usb sel port 1
USB:   ehci_hcd_init...
Register 10011 NbrPorts 1
USB EHCI 1.00
scanning bus for devices... 2 USB Device(s) found
       scanning bus for storage devices... 1 Storage Device(s) found
U-boot# fatload usb 0:1 0x83000000 uImage-montage-test
reading uImage-montage-test

1413724 bytes read
U-boot# bootm 0x83000000
## Booting kernel from Legacy Image at 83000000 ...
   Image Name:   montage-test
   Created:      2026-10-06   5:12:32 UTC
   Image Type:   MIPS Linux Kernel Image (uncompressed)
   Data Size:    1413660 Bytes = 1.3 MiB
   Load Address: 80550000
   Entry Point:  80550000
   Verifying Checksum ... OK
   Loading Kernel Image ... OK
OK

Starting kernel ...

zimage at:     80553140 806A8730
Uncompressing Linux at load address 80200000
Copy device tree to address  80540280
Now, booting the kernel...
[    0.000000] Linux version 6.2.0-rc1-g6d1e71e45420-dirty (root@vm) (mips-linux-gnu-gcc (Ubuntu 12.4.0-2ubuntu1~24.04) 12.4.0, GNU ld (GNU Binutils for Ubuntu) 2.42) #3 Tue Oct  6 05:12:14 UTC 2026
[    0.000000] printk: bootconsole [early0] enabled
[    0.000000] CPU0 revision is: 00019655 (MIPS 24KEc)
[    0.000000] MIPS: machine is HS1168-8001-02B
[    0.000000] OF: of_alias_scan: stdout path is serial0
[    0.000000] Primary instruction cache 16kB, VIPT, 4-way, linesize 32 bytes.
[    0.000000] Primary data cache 16kB, 4-way, VIPT, no aliases, linesize 32 bytes
[    0.000000] Zone ranges:
[    0.000000]   Normal   [mem 0x0000000000000000-0x0000000003ffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000000000-0x0000000003ffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x0000000003ffffff]
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 16256
[    0.000000] Kernel command line: console=ttyS0,115200 earlyprintk
[    0.000000] Unknown kernel command line parameters "earlyprintk", will be passed to user space.
[    0.000000] Dentry cache hash table entries: 8192 (order: 3, 32768 bytes, linear)
[    0.000000] Inode-cache hash table entries: 4096 (order: 2, 16384 bytes, linear)
[    0.000000] Writing ErrCtl register=0004abb8
[    0.000000] Readback ErrCtl register=0004abb8
[    0.000000] mem auto-init: stack:all(zero), heap alloc:off, heap free:off
[    0.000000] Memory: 57232K/65536K available (2210K kernel code, 535K rwdata, 448K rodata, 1216K init, 179K bss, 8304K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
[    0.000000] NR_IRQS: 256
[    0.000000] montage_intc_of_init: regs = bf100000
[    0.000000] plat_time_init: mips_hpt_frequency = 297000000
[    0.000000] clocksource: MIPS: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 6435220358 ns
[    0.000003] sched_clock: 32 bits at 297MHz, resolution 3ns, wraps every 7230584830ns
[    0.004939] Console: colour dummy device 80x25
[    0.007354] montage_console_setup: entry, idx=0, uart = 00000000
[    0.011051] Calibrating delay loop... 395.26 BogoMIPS (lpj=790528)
[    0.039480] pid_max: default: 32768 minimum: 301
[    0.042477] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
[    0.046738] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
[    0.055198] devtmpfs: initialized
[    0.057825] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.060430] futex hash table entries: 256 (order: -1, 3072 bytes, linear)
[    0.064565] pinctrl core: initialized pinctrl subsystem
[    0.077225] clocksource: Switched to clocksource MIPS
[    0.109457] workingset: timestamp_bits=30 max_order=14 bucket_order=0
[    0.111131] io scheduler mq-deadline registered
[    0.112715] io scheduler kyber registered
[    0.314779] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
[    0.318502] montage_intc_map 26/26!
[    0.318579] montage_probe: montage_driver=8051d5c8, port=809c1a18
[    0.321041] montage_config_port lol
[    0.323194] 1f540000.serial: ttyS0 at MMIO 0x1f540000 (irq = 26, base_baud = 0) is a montage-uart
[    0.328536] montage_set_mctrl lol
[    0.330529] montage_console_setup: entry, idx=0, uart = 809c1a18
[    0.334155] montage_console_setup: [0x08] = c000c000, [0x24] = 00000000
[    0.338154] montage_set_termios lol
[    0.340230] printk: console [ttyS0] enabled
[    0.340230] printk: console [ttyS0] enabled
[    0.345289] printk: bootconsole [early0] disabled
[    0.345289] printk: bootconsole [early0] disabled
[    0.351171] sysfs: cannot create duplicate filename '/class/tty/ttyS0'
[    0.354919] CPU: 0 PID: 1 Comm: swapper Not tainted 6.2.0-rc1-g6d1e71e45420-dirty #3
[    0.359533] Stack : 00000000 9cfe4242 ffffffff 00000000 00000000 00000000 00000000 00000000
[    0.364572]         00000000 00000000 00000000 00000000 00000000 00000001 80831a28 9cfe4242
[    0.369614]         80831ac0 00000000 00000000 00000000 00000038 804223c4 00000000 00000000
[    0.374657]         00000000 00000000 80c39e7c 37653164 00000000 00000000 8046f7e0 804a0000
[    0.379699]         00000001 804a0000 80852610 80982f20 00000000 00000000 00000000 80650000
[    0.384742]         ...
[    0.386213] Call Trace:
[    0.387683] [<802085a0>] show_stack+0xb0/0x158
[    0.390369] [<8040a1d8>] dump_stack_lvl+0x38/0x60
[    0.393204] [<803213c4>] sysfs_warn_dup+0x68/0x84
[    0.396041] [<803216b4>] sysfs_do_create_link_sd+0xc8/0xd0
[    0.399349] [<803cc30c>] device_add+0x240/0x7f4
[    0.402081] [<80399e30>] tty_register_device_attr+0x170/0x24c
[    0.405548] [<803b94fc>] uart_add_one_port+0x40c/0x500
[    0.408647] [<803d0ba8>] platform_probe+0x6c/0xd0
[    0.411483] [<803cf190>] really_probe+0x17c/0x2f0
[    0.414319] [<803cf3f8>] __driver_probe_device+0xf4/0xfc
[    0.417523] [<803cf444>] driver_probe_device+0x44/0xd4
[    0.420622] [<803cf6d0>] __driver_attach+0x114/0x128
[    0.423616] [<803cd818>] bus_for_each_dev+0x84/0xc8
[    0.426558] [<803cdf70>] bus_add_driver+0xd8/0x1e8
[    0.429447] [<803d0308>] driver_register+0xd0/0x118
[    0.432388] [<80532df4>] montage_init+0x34/0x5c
[    0.435119] [<80520f08>] do_one_initcall+0xa4/0x280
[    0.438061] [<80521378>] kernel_init_freeable+0x224/0x258
[    0.441317] [<80423878>] kernel_init+0x24/0x110
[    0.444049] [<80202198>] ret_from_kernel_thread+0x14/0x1c
[    0.447305] 
[    0.448309] montage 1f540000.serial: Cannot register tty device on line 0
[    0.467132] loop: module loaded
[    0.480220] montage_startup: [0x08] = c000c000, [0x24] = 00000000
[    0.480552] montage_intc_irq_unmask: hwirq=26
[    0.483256] montage_set_termios lol
[    0.485318] montage_set_mctrl lol
[    0.487489] List of all partitions:
[    0.489436] No filesystem could mount root, tried: 
[    0.489455] 
[    0.493201] Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0)
[    0.498194] ---[ end Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0) ]---
~~~
