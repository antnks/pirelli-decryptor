# pirelli-decryptor

Decrypts passwords stored in Pirelli router config

Usage:

`python decrypt.py "&b7;UP"`

Outputs:

aaa

# Priviledge escallation

Configuration is hidden from a non priviledged user, but you can access it directly with this link:

http://192.168.1.254/rg_conf.cgi?is_inline=1

Search for `(admin` to find list of users. User with ID 0 is root, decrypt the password and enjoy the power of full control

Tested on Pirelli DRG A125G ver TEO_4.2.5.0017	

# Analysis of ADB EA4201N

https://github.com/digiampietro/adbtools2
