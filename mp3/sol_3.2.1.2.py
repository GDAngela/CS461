import sys, io
from pymd5 import md5, padding
from urllib import quote

def attack(query, cmd):
	idx = query.find('&')
	tmp = query[:idx]
	token = tmp.split('=')[1]
	#print token
	cmds = query[idx+1:]
	
	pad = padding((8+len(cmds))*8)
	#print quote(pad)

	before = md5(state=token.decode('hex'), count=512)
	before.update(cmd)
	after = before.hexdigest()
	#print after
	
	return "token=" + after + "&" + cmds + quote(pad) + cmd

if __name__ == '__main__':
	if len(sys.argv)<4:
		print "   missing input argument(s)!   "
		sys.exit()

	query = sys.argv[1]
	cmd3 = sys.argv[2]
	outputFile = sys.argv[3]

	with open(query) as f1:
		q = f1.read().strip()
		with open(cmd3) as f2:
			cmd = f2.read().strip()
			res = attack(q, cmd)
			
			#print res
			with io.FileIO(outputFile, "w") as out:
				out.write(res)

