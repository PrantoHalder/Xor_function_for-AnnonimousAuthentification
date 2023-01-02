word =
byte_arr = bytearray(word,'utf8')
res = []
for byte in byte_arr:
  binary_rep = bin(byte)
  res.append(binary_rep[2:])
b= ''.join(res)



for hr in range(numberOfItems):
    if hr == positions:
        word = str(p_bar[hr])
        byte_arr = bytearray(word, 'utf8')
        res = []
        for byte in byte_arr:
            binary_rep = bin(byte)
            res.append(binary_rep[2:])
        b = ''.join(res)
        rPrime = int(b) ^ int(binary_passward[hr])
print("this is the value of r prime", rPrime)
PBarPrime = (hash_password(str(rPrime)))
print("this PBarPrime ", PBarPrime)

if (rBar) == (PBarPrime):
    print("the clint is ready to send r prime")

print(rPrime)
print(r)
