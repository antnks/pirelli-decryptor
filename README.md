# pirelli-decryptor

Decrypts passwords stored in Pirelli router config

Usage:

`python decrypt.py "&b7;UP"`

Outputs:

aaa

**Update.** Another research with deobfuscation script: https://www.nccgroup.trust/globalassets/our-research/us/whitepapers/2016/october/optimum-routers--researching-managed-routers-.pdf

# Priviledge escallation of DRG A125G

Configuration is hidden from a non priviledged user, but you can access it directly with this link:

http://192.168.1.254/rg_conf.cgi?is_inline=1

Search for `(admin` to find list of users. User with ID 0 is root, decrypt the password and enjoy the power of full control

Tested on Pirelli DRG A125G ver TEO_4.2.5.0017	

# Analysis of ADB EA4201N

https://github.com/digiampietro/adbtools2

https://unlocka1.wordpress.com/2014/04/28/adb-full-root-access/

https://www.exploit-db.com/exploits/44983

```
root@localhost:~# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 00004000 00004000 "CFE"
mtd1: 00200000 00004000 "bootfs_1"
mtd2: 01cd0000 00004000 "rootfs_1"
mtd3: 00200000 00004000 "bootfs_2"
mtd4: 01cd0000 00004000 "rootfs_2"
mtd5: 01ed0000 00004000 "upgrade"
mtd6: 00010000 00004000 "conf_old_main"
mtd7: 00020000 00004000 "conf_fs"
mtd8: 00010000 00004000 "conf_factory"
mtd9: 00100000 00004000 "bbt"
mtd10: 04000000 00004000 "flash"
```
