#!/usr/bin/python

import dpkt, sys, socket

recev_dic = {}
send_dic = {}

if len(sys.argv) < 2:
	print "need an argument"
	sys.exit()

f = open(sys.argv[1])
pcap = dpkt.pcap.Reader(f)

for ts,buf in pcap:	
	
	#check if ethernet objetc 
	if len(buf) <= 0 :
		print 'debug'
		continue

	try:
		eth = dpkt.ethernet.Ethernet(buf)	
	except dpkt.dpkt.UnpackError:
		continue
	
	if not isinstance(eth, dpkt.ethernet.Ethernet):
		continue
	
	#check if ip objetc 	
	ip = eth.data	
	if not isinstance(ip , dpkt.ip.IP):
		continue

	#check if tcp objetc 	
	tcp = ip.data	
	if not isinstance(tcp, dpkt.tcp.TCP):
		continue

	# 0x12 SYN-ACK
	if tcp.flags == 18 :
		if ip.dst not in recev_dic:
			recev_dic[ip.dst] = 0
		else: 			
			recev_dic[ip.dst] += 1 
	# 0x02 SYN
	elif tcp.flags == 2:		
		if ip.src not in send_dic:
			send_dic[ip.src] = 0
		else:
			send_dic[ip.src] += 1


for ip in send_dic:
		if ip not in recev_dic:
			print socket.inet_ntoa(ip)		
		elif send_dic[ip] > (3*recev_dic[ip]):
			print socket.inet_ntoa(ip)

f.close()
