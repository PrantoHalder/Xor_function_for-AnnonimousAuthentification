import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()


#def check_password(hashed_password, user_password):
#    password, salt = hashed_password.split(':')
#    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


#new_pass = (input('Please enter a password: '))
hashed_password = (hash_password(new_pass))
word = hashed_password
byte_arr = bytearray(word,'utf8')
res = []
for byte in byte_arr:
  binary_rep = bin(byte)
  res.append(binary_rep[2:])
  a=''.join(res)
print(a)
#old_pass = input('Now please enter the password again to check: ')
#if check_password(hashed_password, old_pass):
#    print('You entered the right password')
#else:
#    print('I am sorry but the password does not match')