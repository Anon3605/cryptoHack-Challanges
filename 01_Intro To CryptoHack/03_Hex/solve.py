X="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
for i in range(0,len(X),2):
    print(chr(int(X[i:i+2],16)),end="")
print()
#Or just This
print("Returning in bytes")
print(bytes.fromhex(X))