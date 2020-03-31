from Crypto.Cipher import AES
#from secret import flag
import time
from hashlib import md5
flag = open("encrypted",'r').read().decode("base64")
i = 1
t = int(time.time())
while(1):
	key = md5(str(t-i)).digest()
	aes = AES.new(key, AES.MODE_ECB)
	outData = aes.decrypt(flag)
	if outData.startswith("VolgaCTF"):
		print outData
		break
	i += 1