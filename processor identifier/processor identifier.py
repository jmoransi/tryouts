import platform
import string
import sys

modeldata={hex(0x3A):'IvyBridge',
hex(0x2A):'SandyBridge',
hex(0x2D):'SandyBridge',
hex(0x25):'Westmere',
hex(0x2C):'Westmere',
hex(0x2F):'Westmere',
hex(0x1E):'Nehalem', 
hex(0x1A):'Nehalem'
}

info=platform.processor().split(' ')
family=hex(int(info[info.index('Family')+1])) 
model=hex(int(info[info.index('Model')+1]))
if family==hex(0x06):
	print 'You have a '+ modeldata[model]+' processor'
else
	print 'This script is only compatible with the Core iX Processors'


	


