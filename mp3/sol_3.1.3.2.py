import sys, io, string, random

def WHA(inStr):
	mask = 0x3fffffff
	outHash = 0
	br = bytearray(inStr)
	
	for b in br:
		in_val = ((b^0xcc)<<24) | ((b^0x33)<<16) | ((b^0xaa)<<8) | (b^0x55)
		outHash = (outHash & mask) + (in_val & mask)
	return outHash
	

if __name__ == '__main__':
	if len(sys.argv)<3:
		print "   missing input argument(s)!   "
		sys.exit()

	# 0xe87ebc3

	inPut = sys.argv[1]
	outputFile = sys.argv[2]

	with open(inPut) as f1:
		inStr = f1.read().strip()
		res = WHA(inStr)
		res = hex(res)
		#print res
		with io.FileIO(outputFile, "w") as out:
			out.write(res)
		
