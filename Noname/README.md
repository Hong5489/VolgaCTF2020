# Noname
I have Noname; I am but two days old.

[encrypted](encrypted) [encryptor.py](encryptor.py)

It got two files:
- encrypted (Flag that is encrypted)
- encryptor.py (Script that used to encrypt the flag)

encryptor.py:
```python
# Take current timestamp and convert to md5 hash
key = md5(str(int(time.time()))).digest() 
# Add padding to the flag string because it uses AES encryption
padding = 16 - len(flag) % 16
aes = AES.new(key, AES.MODE_ECB)
# Encrypt the flag
outData = aes.encrypt(flag + padding * hex(padding)[2:].decode('hex'))
# Convert to Base64
print outData.encode('base64')
```

This challenge is to brute force the timestamp, its easy to brute force because the **timestamp not a large number and it converted to an integer**

Also the range of number brute force is less because the challenge description say so: **I am but two days old**

I wrote a [python script](decrypt.py) to brute force:
```python
flag = open("encrypted",'r').read().decode("base64")
i = 1
t = int(time.time())
while(1):
	# Minus the current timestamp with counter
	key = md5(str(t-i)).digest()
	aes = AES.new(key, AES.MODE_ECB)
	outData = aes.decrypt(flag)
	# If the decrypted data starts with the flag format
	if outData.startswith("VolgaCTF"):
		print outData
		break
	i += 1
```
## Flag
```
VolgaCTF{5om3tim3s_8rutf0rc3_i5_th3_345iest_w4y}
```