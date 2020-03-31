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
	condition = ""
	for j in range(n):
		condition += "("+ numbers[i][j] + "* inp[%i])+" % j
	solver.add(eval(condition[:-1] + "==" + numbers[i][n]))
print(solver.check())
modl = solver.model()
print(''.join([chr(modl[inp[i]].as_long()) for i in range(n)]))