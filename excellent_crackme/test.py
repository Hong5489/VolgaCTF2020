numbers = [i.strip().split(" ") for i in open("numbers.txt",'r').read().split("\n")]
inp = "VolgaCTF{" + 36*'b'
n = 45
for i in range(2):
	counter = 0
	for j in range(n):
		counter2 = int(numbers[i][j])
		counter = counter + (counter2 * ord(inp[j]))
	valid = numbers[i][n]
	print valid,counter