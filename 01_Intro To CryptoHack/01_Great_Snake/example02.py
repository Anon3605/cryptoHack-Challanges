decimal=122
hexadecimal=0x33
binary=0b1111101001
octal=0o2133460

print(f"Bitwise OR operation with {decimal} and {hex(hexadecimal)} is {bin(decimal | hexadecimal)} or {decimal | hexadecimal}")
print(f"Bitwise AND operation with {oct(octal)} and {hex(hexadecimal)} is {bin(octal & hexadecimal)} or {octal | hexadecimal}")
print(f"Bitwise XOR operation with {bin(binary)} and {oct(octal)} is {bin(octal ^ binary)} or {binary | octal}")
