#! /usr/bin/env python

class Node():
    def __init__(self, parent, children, classification, attribute):
        self.parent = parent
        self.children = children
        self.classification = classification
        self.attribute = attribute

    def print(self):
        if(self.classification != None):
            print self.classification
        elif(self.attribute != None):
            print "{}?".format(self.attribute)
        for child in self.children:
            child.print()
