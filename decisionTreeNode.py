#! /usr/bin/env python

import data

class Node():
	#parent: Node
	#children: dict((attribute value) -> Node)
	#classification: attribute value (of the classification attribute)
	#attribute: tuple(string, set(attribute value))
	def __init__(self, parent, children, classification, attribute):
		self.parent = parent
		self.children = children
		self.classification = classification
		self.attribute = attribute
	
	def printTree(self):
		print self
	
	def __str__(self):
		return self.toStr(0)

	def __repr__(self):
		return self.toStr(0)
		
	#indent: number - number of spaces to indent this node by
	def toStr(self, indent):
		str = ""
		nextIndent = indent + 2
		if(self.classification != None):
			return indent*" "+"Classification = {}".format(self.classification)
		elif(self.attribute != None):
			str = indent*" "+"{}? : {{\n".format(self.attribute[0])
			for val, child in self.children.iteritems():
				#print value : node
				str = str + nextIndent*" " + "{}:\n".format(val)
				str = str + "{},\n".format(child.toStr(nextIndent))
			str = str + indent*" "+"}"
			return str

	def search(self, datum):
		if(self.classification != None):
			return self.classification
		elif(self.attribute != None):
			return self.children[datum[data.indexOfAttribute(self.attribute)]].search(datum)