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
U-boot# fatload usb 0:1 0x83000000 uImage-montage-initramfs
reading uImage-montage-initramfs

2143932 bytes read
U-boot# bootm 0x83000000
## Booting kernel from Legacy Image at 83000000 ...
   Image Name:   montage-initramfs
   Created:      2026-10-06  18:43:55 UTC
   Image Type:   MIPS Linux Kernel Image (uncompressed)
   Data Size:    2143868 Bytes = 2 MiB
   Load Address: 806c0000
   Entry Point:  806c0000
   Verifying Checksum ... OK
   Loading Kernel Image ... OK
OK

Starting kernel ...

[    0.000000] Linux version 6.2.0-rc1-g6d1e71e45420-dirty (root@vm) (mips-linux-gnu-gcc (Ubuntu 12.4.0-2ubuntu1~24.04) 12.4.0, GNU ld (GNU Binutils for Ubuntu) 2.42) #1 Tue Oct  6 18:43:39 UTC 2026
[    0.000000] printk: bootconsole [early0] enabled
[    0.000000] CPU0 revision is: 00019655 (MIPS 24KEc)
[    0.000000] MIPS: machine is HS1168-8001-02B
[    0.000000] Initrd not found or empty - disabling initrd
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
[    0.000000] Writing ErrCtl register=0004abbd
[    0.000000] Readback ErrCtl register=0004abbd
[    0.000000] mem auto-init: stack:all(zero), heap alloc:off, heap free:off
[    0.000000] Memory: 55748K/65536K available (3305K kernel code, 555K rwdata, 768K rodata, 1248K init, 188K bss, 9788K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
[    0.000000] NR_IRQS: 256
[    0.000000] montage_intc_of_init: regs = bf100000
[    0.000000] plat_time_init: mips_hpt_frequency = 297000000
[    0.000000] clocksource: MIPS: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 6435220358 ns
[    0.000003] sched_clock: 32 bits at 297MHz, resolution 3ns, wraps every 7230584830ns
[    0.004952] Console: colour dummy device 80x25
[    0.007346] montage_console_setup: entry, idx=0, uart = 00000000
[    0.011055] Calibrating delay loop... 395.26 BogoMIPS (lpj=790528)
[    0.039503] pid_max: default: 32768 minimum: 301
[    0.042458] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
[    0.046761] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
[    0.054287] cblist_init_generic: Setting adjustable number of callback queues.
[    0.055782] cblist_init_generic: Setting shift to 0 and lim to 1.
[    0.060734] devtmpfs: initialized
[    0.064187] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.067311] futex hash table entries: 256 (order: -1, 3072 bytes, linear)
[    0.071501] pinctrl core: initialized pinctrl subsystem
[    0.085803] SCSI subsystem initialized
[    0.086123] usbcore: registered new interface driver usbfs
[    0.088169] usbcore: registered new interface driver hub
[    0.091320] usbcore: registered new device driver usb
[    0.094824] clocksource: Switched to clocksource MIPS
[    0.132569] workingset: timestamp_bits=30 max_order=14 bucket_order=0
[    0.133918] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.136720] fuse: init (API version 7.38)
[    0.140446] io scheduler mq-deadline registered
[    0.141769] io scheduler kyber registered
[    0.347453] montage_intc_map 26/26!
[    0.347534] montage_probe: montage_driver=80680cb0, port=809dfa18
[    0.349879] montage_config_port lol
[    0.352035] 1f540000.serial: ttyS0 at MMIO 0x1f540000 (irq = 26, base_baud = 0) is a montage-uart
[    0.357377] montage_set_mctrl lol
[    0.359369] montage_console_setup: entry, idx=0, uart = 809dfa18
[    0.362995] montage_console_setup: [0x08] = c000c000, [0x24] = 00000000
[    0.366995] montage_set_termios lol
[    0.369068] printk: console [ttyS0] enabled
[    0.369068] printk: console [ttyS0] enabled
[    0.374084] printk: bootconsole [early0] disabled
[    0.374084] printk: bootconsole [early0] disabled
[    0.395922] loop: module loaded
[    0.397805] spi-nor spi0.0: unrecognized JEDEC id bytes: 00 16 40 ef 00 00
[    0.399000] usbcore: registered new interface driver usb-storage
[    0.404096] usbcore: registered new interface driver usbhid
[    0.405584] usbhid: USB HID core driver
[    0.426553] montage_startup: [0x08] = c000c000, [0x24] = 00000000
[    0.426945] montage_intc_irq_unmask: hwirq=26
[    0.429537] montage_set_termios lol
[    0.431661] montage_set_mctrl lol
[    0.436270] Freeing unused kernel image (initmem) memory: 1248K
[    0.437172] This architecture does not have kernel memory protection.
[    0.441128] Run /init as init process

~~~
