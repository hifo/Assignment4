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
#	return attribute with lowest entropy
