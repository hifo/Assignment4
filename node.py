#! /usr/bin/env python

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

    def print(self):
        print self.toStr(0)

	#indent: number - number of spaces to indent this node by
	def toStr(self, indent):
		str = ""
		nextIndent = indent + 2
        if(self.classification != None):
            return indent*" "+"{}".format(self.classification)
        elif(self.attribute != None):
            str = indent*" "+"{}? : {\n".format(self.attribute)
        for val, child in self.children:
			#print value : node
			str = str + nextIndent*" " + val + " :\n" + child.toStr(nextIndent) + ",\n"
		str = str + indent*" "+"}"