#! usr/bin/env/ python
from __future__ import division

import math
import decisionTreeNode

classification = [1,2,3]


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
    elif examples.count(examples[0]) == len(examples):
        return examples[0]
    elif attributes == None:
        return MODE(examples)
    else:
        best = chooseAttribute(attributes, examples)
        tree = best
        #for each
        return tree

#function MODE(examples) returns a decision tree
#	return a new decision tree w/ answer = mode of results of examples

def mode(examples):
    count = 0
    mode = 0
    for ex in examples:
        temp_count = examples.count(ex)
        if temp_count > count:
            count = temp_count
            mode = ex
    decision = decisionTreeNode.Node(None, None, ex, None)
    return decision
#function GAIN(attribute, examples) returns number
#	gain = ENTROPY(examples)
#	for each value of attribute v:
#		weight = (number of examples with attribute = v)/(total number of examples)
#		gain = gain - weight * ENTROPY(examples with attribute = v)
#	return gain

def calcGain(attribute, examples):
    gain = entropy(examples)
    temp_examples = []
    for v in attribute:
        weight = examples.count(v)/len(examples)
        for i in examples:
            try: examples.index(v)
            except ValueError: continue
            temp_examples.append(examples[examples.index(v)])
        gain = gain - weight * entropy(temp_examples)
    return gain
#function ENTROPY(examples) returns number
#	entropy = 0
#	for each classification value v:
#		prob = (examples classified as v)/(count of all examples)
#		entropy = entropy - (prob * log_2(prob))
#	return entropy

def entropy(examples):
    entropy = 0
    prob = 0
    for v in classification:
        prob = examples.count(v)/len(examples)
        if prob == 0:
            continue
        else:
            entropy = entropy - (prob * math.log(prob,2))
    return entropy

#function CHOOSE-ATTRIBUTE(attributes, examples) returns attribute
#	return attribute with highest gain
def chooseAttribute(attributes, examples):
    gain = 0
    attr = None
    for set in attributes:
        newGain = calcGain(set, examples)
        if newGain > gain:
            gain = newGain
            attr = set
    return attr



examples = [1,1,2]

print mode(examples)
