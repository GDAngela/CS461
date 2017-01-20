import sys, io
from Crypto.Cipher import AES

if __name__ == '__main__':
	if len(sys.argv)<5:
		print "   missing input argument(s)!   "
		sys.exit()

	textFile = sys.argv[1]
	keyFile = sys.argv[2]
	ivFile = sys.argv[3]
	outputFile = sys.argv[4]

	with open(keyFile) as f1:
		key = f1.read().strip().decode('hex')
		with open(textFile) as f2:
			text = f2.read().strip().decode('hex')
			with open(ivFile) as f3:
				iv = f3.read().strip().decode('hex')
				print len(iv)
				aes = AES.new(key, AES.MODE_CBC, iv)	
				res = aes.decrypt(text)
				#print res
				with io.FileIO(outputFile, "w") as out:
					out.write(res)

