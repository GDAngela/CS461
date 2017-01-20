import sys, fractions, math, decimal, io
from fractions import Fraction
from decimal import Decimal
from sympy import Symbol
from sympy.solvers import solve

if __name__ == '__main__':

	if len(sys.argv)<5:
		print "   missing input argument(s)!   "
		sys.exit()

	cipherText = sys.argv[1]
	keyFile = sys.argv[2]
	modFile = sys.argv[3]
	outputFile = sys.argv[4]
	with open(cipherText) as f1:
		text = int(f1.read().strip(),16)
	with open(keyFile) as f2:
		e = int(f2.read().strip(),16)
	with open(modFile) as f3:
		N = int(f3.read().strip(),16)
	
# find continued fraction 
	continued_fraction = []

	top = e
	bottom = N

	while 1 : 
		if top == 1 :
			break 
		else:
			t = top/bottom 
			top = top - (t*bottom)
			continued_fraction.append(t)
			t = top
			top = bottom
			bottom = t

# find convergence		
	convergence = []
	for index, i in enumerate(continued_fraction): 
		t = Fraction(0)
		if len(continued_fraction[:index+1][::-1]) != 0:
			for i in continued_fraction[:index+1][::-1]:
				if i == 0:
					pass
				else:
					t = Fraction(1/Fraction(i+t))
			
		convergence.append(t)

	for i in convergence:
		k = i.numerator		
		d = i.denominator
		if k == 0 :
			pass
		else:	
			t = (e * d - 1) / k 			
			x = Symbol('x')
			roots = solve(x * x + (N + 1 - t) * x + N, x)
			if roots[0]*roots[1] == N:
				break
    
	res = hex(pow(text, d, N))[2:-1]
	#print res

	with io.FileIO(outputFile, "w") as out:
		out.write(res)

	
