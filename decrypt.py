import sys

cipher = "\x56\xf3\xee\x50\x34\xa9\xee\x6b\x55\x4b\x03\x3c\x9a\x01\x78\xb3\xfc\xb1\x3d\xd3\x9b\xd2\xcb\x9f\x06\xd1\xd1\x65\xe7\xbd\x2d\x9f\xb1\xee\x8d\xd8\xf3\xfb\xbb\xc3\xb8\xa1\x0b\xae\x3d\xc1\x2e\xae\xe2\x54\x07\xf0\x0a\x5a\xd0\x8a\x78\x04\x06\x32\x86\x2c\xac\xf1\xfa\x61\x17\xdc\x31\xc7\x7b\xaa\x56\x73\x8a\x87\x51\xb7\xf1\xfd\x90\x73\xe7\x6c\x6b\xc4\xf6\x13\x17\x35\xb5\x3d\xec\x75\xfa\xe5\xf3\x2a\x04\x01\x58\x4e\x13\x56\xe7\x2b\xc3\x1a\x82\x3d\x48\xfd\x6c\xf6\x12\x7d\xfe\x88\xde\x3d\x91\x99\xcf\x6d\x57\xae\x57\xe7\xe4\x4b\x28\xfb\x59\x3d\x58\x10\x6b\xc2\xf7\xb0\x2e\x66\x95\x54\x1e\xa0\x33\xdb\xa2\x08\xc5\xae\xd6\xe4\xfe\x7f\x82\xdd\xce\xab\xae\x26\x90\x30\xcb\xea\x58\xd6\x93\xfc\xd5\x8e\x22\xc2\x87\xdf\xd5\xde\x4d\x1b\x45\x62\xbe\xfd\x25\xeb\xa7\x02\x47\x05\xe4\x85\x52\x99\xd7\xc1\xe6\x3d\xaf\xee\x17\xc9\x1d\xd8\xda\x7d\x31\xdc\x98\x0b\x03\x94\x5e\x37\x4f\x96\x22\x32\x8f\x6e\x38\x6b\xf8\xa0\x98\x8d\x95\xe0\xb1\x10\x86\xa4\x83\xa6\x87\x66\x87\xac\xd7\x65\x44\x93\x54\x4b\xd5\xdd\x60\xc2\xf7\xd4\xdf\xfd\x39\x91\x90\x4b"

inputstr = sys.argv[1]
inputlen = len(inputstr)

password = ""

i = 0
while i < inputlen:
	if inputstr[i] == '&':
		symb = bytes.fromhex(inputstr[i + 1] + inputstr[i + 2])
		password += chr(ord(symb))
		i += 3
	else:
		password += inputstr[i]
	i += 1

res = ""

i = 0
for c in password:
	diff = ord(c) - ord(cipher[i])
	if diff < 0:
		diff = 255 + diff
	res += chr(diff)
	i += 1

print (res)

