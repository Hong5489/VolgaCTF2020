from z3 import *
#inp_length = BitVec("inp_length",8)
n = 45
inp = [Int('inp%i' %i) for i in range(n)]
numbers = [i.strip().split(" ") for i in open("numbers.txt",'r').read().split("\n")]
solver = Solver()
solver.add(inp[0] == ord("V"))
solver.add(inp[1] == ord("o"))
solver.add(inp[2] == ord("l"))
solver.add(inp[3] == ord("g"))
solver.add(inp[4] == ord("a"))
solver.add(inp[5] == ord("C"))
solver.add(inp[6] == ord("T"))
solver.add(inp[7] == ord("F"))
solver.add(inp[8] == ord("{"))
for i in range(9,45):
	solver.add(inp[i] >= 32)
	solver.add(inp[i] <= 126) 
solver.add(inp[44] == ord("}"))
for i in range(44):
	counter = 0
	for j in range(n):
		counter2 = int(numbers[i][j])
		counter = counter + (counter2 * inp[j])
	valid = numbers[i][n]
	solver.add(valid == counter)
print(solver.check())
modl = solver.model()

print(repr(''.join([chr(modl[inp[i]].as_long()) for i in range(n)])))