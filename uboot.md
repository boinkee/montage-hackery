# U-Boot docs
WIP 
* Typical U-Boot, with additional functionality
* You can access it from winstbupgrader > download section > select nor > select some xml file > press start
* or ?
<br>
Example log from WinStbUpgrader (read winstbupgrader.md):
~~~
Serial Port Opened
download start
Please reboot the STB manually.
Change baudrate to 115200.
Sync Succeed.
Sending boot init...
Send boot init completed.
boot init run successfully.
SendClient.
Sending Client is complete.
Client is up.
Client Functionality is good.


U-Boot 2012.04-hg1645-e088928bb4c6-dirty (Oct 31 2019 - 09:13:09)

*****************************************
**  Board: mips CPU: sym - MIPS 24KEc
**  SOC name  : 0x8080
**  PACKET type : SIP_68S_DDR2
*****************************************
D
RAM:  
DDR is 64MiBytes
20 MiB

== OTP_VERSION:[hg_NA] Build Time:[Oct 31 2019, 09:13:09]
Using default environment


cpu_secondary_init_r: image file for secondary core should already locate where it should be
current boot media:0...
phy_clk = 405, clk=50
R_SPIN_CH0_BAUD: 400000
09
SF: spi flash status register: 0x00, 0x02  ta=0x814283fc 
SPI: Detected W25Q32 with erase size 64 KiB, total 4 MiB

Net:   0xBF50001C = 0x0011ff03
0xBF510018 = 0xfffffff9
No ethernet found.
main_loop entered: bootdelay=0

Hit any key to stop autoboot:  0 
Please click start 


U-boot# 
uboot run successful


download successful!
m_download_thrd is stop!

U-boot# help
?       - alias for 'help'
av_launch- avcpu launch
bdinfo  - print Board Info structure
boot    - boot default, i.e., run 'bootcmd'
bootd   - boot default, i.e., run 'bootcmd'
bootm   - boot application image from memory
bootp   - boot image via network using BOOTP/TFTP protocol
check   - check flag from flash or usb upgrade or barcode
cmp     - memory compare
coninfo - print console devices and information
cp      - memory copy
cpu     - Multiprocessor CPU boot manipulation and release
crc32   - checksum calculation
echo    - echo args to console
editenv - edit environment variable
env     - environment handling commands
exit    - exit script
false   - do nothing, unsuccessfully
fatload - load binary file from a dos filesystem
fatwrite- write file into a dos filesystem
freeze_with_dioff- freeze_with_dioff
go      - start application at address 'addr'
goo     - start application at address 'addr'
help    - print command description/usage
iminfo  - print header information for application image
itest   - return true/false on integer compare
jpeg_logo- jpeg_logo
jpeg_logo_lite- jpeg_logo_lite
jpeg_sw - jpeg_sw
loadimg - load image from flash
macfilter- set mac filter
macinit - init ethernet before every test
macmode - set mac phy mode
macrx   - mac receive packets
mactx   - mac send single packet out
md      - memory display
mm      - memory modify (auto-incrementing address)
mpr     - read phy reg
mpw     - write phy reg
mtest   - simple RAM read/write test
mw      - memory write (fill)
nfs     - boot image via network using NFS protocol
nm      - memory modify (constant address)
ntt     - ntt for ethernet test cmd
printenv- print environment variables
reset   - Perform RESET of the CPU
run     - run commands in an environment variable
runapp  - print jump to exe montage app
secure  - secure sub-system
setenv  - set environment variables
sf      - SPI flash sub-system
sleep   - delay execution for some time
source  - run script from memory
test    - minimal test like /bin/sh
tftpboot- boot image via network using TFTP protocol
true    - do nothing, successfully
usb     - USB sub-system
usbboot - boot from USB device
usbup   - usbup   - update kernal & root file system & data automatically by script file

version - print monitor, compiler and linker version
U-boot# bdinfo
boot_params = 0x80FCEF88
memstart    = 0x80100000
memsize     = 0x01400000
flashstart  = 0x00000000
flashsize   = 0x00000000
flashoffset = 0x00000000
ethaddr     = 00:1B:11:17:00:77
ip_addr     = 192.168.1.55
baudrate    = 38400 bps
U-boot# sf probe 0
spi0 is already setup!!!
SF: spi flash status register: 0x00, 0x02  ta=0x814283fc
SPI: Detected W25Q32 with erase size 64 KiB, total 4 MiB
U-boot# printenv
addmisc=setenv bootargs ${bootargs} console=ttyS0,${baudrate} panic=1
baudrate=38400
bootcmd=if test $bootmedia -eq 1 || test $bootmedia -eq 4;then echo '####### Uboot Fixed Partitions #######';echo    bootinit       0x0~0x80000;echo    uboot         0x80000~0x180000;echo    boot.scr     0x180000~0x200000;echo '####################################';loadimg 0 0x180000 0x10000 0x80100000;source 0x80100000;elif test $bootmedia -eq 0;then echo '####### Uboot Fixed Partitions #######';echo    bootinit       0x0~0x10000;echo    uboot         0x10000~0x50000;echo    boot.scr     0x50000~0x60000;echo '####################################';loadimg 0 0x50000 0x10000 0x80100000;source 0x80100000;fi;
bootdelay=0
bootfile=/tftpboot/vmlinux
bootmedia=0
chipver=11
ddrsize=64
ethaddr=00:1B:11:17:00:77
ipaddr=192.168.1.55
lnxlinkaddr=0x80204430
lnxnfsbt=tftp 0x80200000 vmlinux;go ${lnxlinkaddr}
load=tftp 80500000 ${u-boot}
netmask=255.255.255.0
pinmux=1
serverip=192.168.1.1
stderr=serial
stdin=serial
stdout=serial

Environment size: 1052/4092 bytes
U-boot#

~~~
