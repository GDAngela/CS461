#!/usr/bin/python
# -*- coding: utf-8 -*-
a = "I come in peace."
b = "Prepare to be destroyed!"
blob = """
                     ��k(���ww;���w���j�Y.AaB,��?�r���k����C����/��l �)��Ըk���.��!@i�������+�6)�ZG����F��O��(Iϰ�B�$	*����~����`��"""
c = blob.count('B')
d = blob.count('A')
if c%2==0 or d%2==0:	
	print a
else:
	print b
