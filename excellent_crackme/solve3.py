import numpy as np
equations = open("numbers.txt",'r').read().split('\n')
matrix1 = []
matrix2 = []
for line in equations:
	eq = []
	for num in line.strip().split(' ')[:-1]:
		eq.append(int(num))
	matrix1.append(eq)
	matrix2.append(int(line.strip().split(' ')[-1]))

A = np.array(matrix1)
B = np.array(matrix2)
flag = np.linalg.inv(A).dot(B)
print(''.join(chr(int(round(f))) for f in flag))