import sys, io, hashlib

# s1 = "ae4d7552696361a34794fd7b3124b15ce773033b2f8f36b449213675b1f5e93a"
# s2 = "18de46bebf532de885cd3acb9af5eec726619d51fed134c4e3a87090b0d5015a"

if __name__ == '__main__':
	if len(sys.argv)<4:
		print "   missing input argument(s)!   "
		sys.exit()

	File1 = sys.argv[1]
	File2 = sys.argv[2]
	outputFile = sys.argv[3]

	with open(File1) as f1:
		content1 = f1.read().strip()
		s1 = hashlib.sha256(content1).hexdigest()
		s1 = bin(int(s1, 16))[2:]
		with open(File2) as f2:
			content2 = f2.read().strip()
			s2 = hashlib.sha256(content2).hexdigest()
			s2 = bin(int(s2, 16))[2:]
			
			diff = 0
		        l = len(s2)
			for i in range(0, l):
				if s1[i] != s2[i]:
					diff += 1
			#print diff
			with io.FileIO(outputFile, "w") as out:
					out.write(str(hex(diff)[2:]))
