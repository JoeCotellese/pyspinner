import re
import random
import sys
test_string = """This is a {test string|an interesting string|another string.} there are many
strings like this but this one is {mine|yours|ours|another persons}. 

The big {black|red|hairy|mighty|turkey} dog attacked the {tall|thin|wimpy|childesh} man.
"""

def pick_winner(list):
	l = list.group(1).split('|')
	#print l
	ret = l[random.randrange(0,len(l))]
	return ret


if __name__ == "__main__":
	input = open(sys.argv[1]).read()
	list =  re.sub(r'\{(.*?)\}', pick_winner, input)
	print list
