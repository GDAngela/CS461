import sys, io
from Crypto.PublicKey import RSA

if __name__ == '__main__':
	if len(sys.argv)<5:
		print "   missing input argument(s)!   "
		sys.exit()

	textFile = sys.argv[1]
	keyFile = sys.argv[2]
	modulo = sys.argv[3]
	outputFile = sys.argv[4]

	with open(keyFile) as f1:
		key = f1.read().strip()
		key = int(key, 16)
		with open(textFile) as f2:
			text = f2.read().strip()
			text = int(text, 16)
			with open(modulo) as f3:
				modu = f3.read().strip()
				modu = int(modu, 16)
				res = pow(text, key, modu)
				hexx = hex(res)[2:]
				hexx = hexx.replace("L", "")
				with io.FileIO(outputFile, "w") as out:
					out.write(hexx)
				

