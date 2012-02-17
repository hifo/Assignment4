#! usr/bin/env/ python
from __future__ import division

import math
import decisionTreeNode

classification = ("Class", [1,2,3])

#attribute: tuple(string, set)
#examples: list(tuple)

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
    elif len(matchingExamples(examples, classification, examples[0][-1])) == len(examples):
        return decisionTreeNode.Node(None, None, examples[0][-1], None)
    elif attributes == None:
        return mode(examples)
    else:
        best = chooseAttribute(attributes, examples)
        tree = decisionTreeNode.Node(None, [], None, best)
        for v in best[1]:
            subexamples = matchingExamples(examples, best, v)
            reducedAttrs = attributes
            reducedAttrs.remove(best)
            subtree = dtl(subexamples, reducedAttrs, mode(examples))
            tree.children[v] = subtree
            subtree.parent = tree
        return tree

#returns subset of given examples in which
#the given attribute of each item in the set has a value
#which matches the given value
def matchingExamples(examples, attribute, value):
    attrIdx = data.indexOfAttribute(attribute)
    return filter(lambda ex: ex[attrIdx] == value, examples)

#given a datum (as in an element of examples), returns the classification of the datum
def classOf(datum):
    return datum[-1]

def attributeValOf(datum, attribute):
    return datum[data.indexOfAttribute(attribute)]

#function MODE(examples) returns a decision tree
#	return a new decision tree w/ answer = mode of results of examples

def mode(examples):
    count = 0
    mode = 0
    classes = map(classOf, examples)
    for ex in set(classes):
        temp_count = classes.count(ex)
        print "temp_count : {}".format(temp_count)
        if temp_count > count:
            count = temp_count
            mode = ex
            print ex
    decision = decisionTreeNode.Node(None, None, mode, None)
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
    for v in attribute[1]:
        weight = map(lambda x: attributeValOf(x, attribute), examples).count(v)/len(examples)
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
        prob = map(classOf, examples).count(v)/len(examples)
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



examples = [(1,),(1,),(2,),(1,),(2,),(3,),(1,),(2,),(3,),(1,),(2,),(3,),(1,),(2,),(1,)]

print mode(examples)
