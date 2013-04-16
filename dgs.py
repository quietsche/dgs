#!/usr/bin/python
"""
* DGS - DotLAN-GalerieSauger
*
* Copyright 2013, Daniel 'grindhold' Brendle
* Released under LGPL License.
*
* Dieses Skript saugt Bildergalerien von einer Dotlan-Galerie
* in den Ordner, von dem aus dieses Skript gestartet wird.
* Es setzt ein installiertes wget auf dem ausfuehrenden System vorraus.
* Die drei konstanten HOST, GALERY_ID und COUNT muessen vor dem ausfuehren 
* gesetzt werden.
"""
HOST = "" # Der Host auf dem die Galerie liegt (bspw: 1024lan.de)
GALERY_ID = "" # Die Galerie, zu finden in der URL eines einzelnen bildes (bspw: 20130908-C3D952)
COUNT = 0 # Die Anzahl der in der Galerie vorhandenen Bilder (bspw: 50)

import os
import urllib2

i = 0
a = ""

for i in range(1,COUNT+1,1):
	if i < 10:
		a = "00"+str(i)
	elif i < 100:
		a = "0"+str(i)
	else:
		a = str(i)

	source = "http://%s/gallery/archive/%s/0%s.jpg"%(HOST, GALERY_ID, a)
	print source
	
	f = urllib2.urlopen(source)
	data = f.read()
	f.close()
	target = open("0%s.jpg"%a,"wb")
	target.write(data)
	target.close()
