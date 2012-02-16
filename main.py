#! usr/bin/env/ python
from __future__ import division

import cmath

#function DTL(examples, attributes, default) returns a decision tree
#	if examples is empty then return default
#	else if all examples have some classification then return that classification
#	else if attributes is empty then return MODE(examples)
#	else
#		best = CHOOSE-ATTRIBUTE(attributes, examples)
#		tree = a new decision tree w/ root test = best
#		for each value v[i] of best do:
#			examples[i] = {elements of examples with best = v[i] }
#			subtree = DTL(examples[i], attributes - best, MODE(examples))
#			add a branch to tree with label v[i] and subtree subtree
#		return tree

def dtl(examples, attributes, default):
    if examples == None:
        return default
    #helper function to check example classifications
    elif attributes == None:
        return MODE(examples)
    else:
        best = chooseAttribute(attributes, examples)
        tree = best
        #for each
        return tree

#function CHOOSE-ATTRIBUTE(attributes, examples) returns attribute
#	return attribute with highest gain
#def chooseAttribute(attributes, examples):
    

#function MODE(examples) returns a decision tree
#	return a new decision tree w/ answer = mode of results of examples

#function ENTROPY(examples) returns number
#	entropy = 0
#	for each classification value v:
#		prob = (examples classified as v)/(count of all examples)
#		entropy = entropy - (prob * log_2(prob))
#	return entropy

def entropy(examples, classification):
    entropy = 0
    prob = 0
    print examples
    print classification
    for v in classification:
        print "v : {}".format(v)
        prob = exampleValueChecker(examples, v)/len(examples)
        print "exampleValueChecker : {}".format(exampleValueChecker(examples, v))
        print "elements in examples : {}".format(len(examples))
        print "prob: {}".format(prob)
        if prob == 0:
            continue
        else:
            print "log_2(prob): {}".format(cmath.log(prob,2))
            entropy = entropy - (prob * cmath.log(prob,2))
        print "entropy: {}".format(entropy)
    return entropy

#function GAIN(attribute, examples) returns number
#	gain = ENTROPY(examples)
#	for each value of attribute v:
#		weight = (number of examples with attribute = v)/(total number of examples)
#		gain = gain - weight * ENTROPY(examples with attribute = v)
#	return gain

#def gain(attribute, examples):

#takes an array of examples and a value and returns the number of examples classified as that value    
def exampleValueChecker(examples, value):
    return examples.count(value)


classification = [1,2,3]
examples = [1,4,5]
value = entropy(examples, classification)
print value
