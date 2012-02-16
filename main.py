#!usr/bin/env/python

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

#function CHOOSE-ATTRIBUTE(attributes, examples) returns attribute
#	return attribute with highest gain

#function MODE(examples) returns a decision tree
#	return a new decision tree w/ answer = mode of results of examples

#function ENTROPY(examples) returns number
#	entropy = 0
#	for each classification value v:
#		prob = (examples classified as v)/(count of all examples)
#		entropy = entropy - (prob * log_2(prob))
#	return entropy

#function GAIN(attribute, examples) returns number
#	gain = ENTROPY(examples)
#	for each value of attribute v:
#		weight = (number of examples with attribute = v)/(total number of examples)
#		gain = gain - weight * ENTROPY(examples with attribute = v)
#	return gain