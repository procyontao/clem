#!/usr/bin/python
'''
Created on Dec.24, 2013

@author: Yuntao
'''



def writest2(xylist,filename,z=0,defocus=-100.0,spot=7,mode=3,intensity=60.0,index=1):
	import numpy as np
	from struct import *
	xylist=np.asarray(xylist,'double')
	xylist=xylist.reshape(len(xylist)/2,2)
	s=long(len(xylist))
	f=open(filename,'w')
	f.write('\x0cFeiTem Stage\x00\x00\x00\x00\x00\x00\x08@)\x00\x00\x00*\x00\x00\x002\x00\x00\x00=\x00\x00\x00A\x00\x00\x00\x00\x00c\x1f\x01\xca\x9fS\xe4@c\x1f\x01\xca\x9fS\xe4@TAOCHANGLU\x00')

	f.write(pack('l',s))#long Number of stage positions
	i=1
	p=78
	for xy in xylist:
		f.write(pack('i',p+i*100))#pointer integer

		f.write(pack('d',xy[0]*10**-6))#double x

		f.write(pack('d',xy[1]*10**-6))#double y

		f.write(pack('d',z*10**-6))#double z

		f.write(pack('d',0.0))#double alpha

		f.write(pack('d',0.0))#double beta

		f.write(pack('i',mode))#integer mode: 3 means Par uP SA; 1 means Par LM

		f.write(pack('i',index))#integer index

		f.write(pack('i',spot))#integer spot

		f.write('\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')#unkwown 20 bytes:	TEM/STEM	Series	Lorentz

		f.write(pack('d',defocus*10**-6))#double focus

		f.write(pack('d',intensity*10**-2))#double intensity

		f.write("%02i"%i+'.\tp'+"%02i"%i+'\x00')#string Comment

		i=i+1

