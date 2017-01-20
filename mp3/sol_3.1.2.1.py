import sys, io

def convert(k):	
	res = dict()	
	l = len(k)
	for i in range(l):
		res[k[i]] = chr(ord("A")+i)
	res[' '] = ' '
	return res		


if __name__ == '__main__':
	if len(sys.argv)<4:
		print "   missing input argument(s)!   "
		sys.exit()

	textFile = sys.argv[1]
	keyFile = sys.argv[2]
	outputFile = sys.argv[3]

	with open(keyFile) as f1:
		key = f1.read().strip()
		with open(textFile) as f2:
			t = f2.read().strip()
			m = convert(key)
			
			tmp = [m[c] for c in t]
			output = "".join(tmp)
			#print output
			with io.FileIO(outputFile, "w") as out:
				out.write(output)

