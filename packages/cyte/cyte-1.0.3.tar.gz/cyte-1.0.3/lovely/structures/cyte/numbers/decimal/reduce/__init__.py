
'''
import cyte.numbers.decimal.reduce as reduce_decimal
reduce_decimal.start (Fraction (1, 3))
'''

from fractions import Fraction
import math

'''
	89.487
		48, 7
		7 >= 5 -> return 48 + 1

	89.49
'''
def round (integer, smaller_amount_integer):
	print ('rounding:', integer, smaller_amount_integer)

	if (smaller_amount_integer >= 5):
		return integer + 1

	return integer;

def make_right_side_equal_to_partial_size (partial_size_designated, partial):
	last_index_of_partial = partial_size_designated - 1
	while (len (partial) <= last_index_of_partial):		
		partial = partial + "0"

	return partial

def start (
	fraction, 
	partial_size = 3, # math.inf
	round = round
):
	'''
		the partial size currently needs to be equal or greater
		than 1.
	'''
	assert (partial_size >= 1)

	the_float = float (Fraction (fraction).limit_denominator ())
	the_float_string = str (the_float)

	#print ("the_float_string:", the_float_string)

	approved = "1234567890.-"

	for character in the_float_string:
		assert (character in approved)

	if ("." in the_float_string):
		split = the_float_string.split (".")		
		split [1] = make_right_side_equal_to_partial_size (
			partial_size,
			split [1]
		)
		
		'''
			if the right of the decimal has more than
			"partial_size" characters, e.g. 14.2857
		'''
		if (
			len (split [1]) >= (partial_size + 1)
		):
			smaller_amount_integer = int (split [1][ partial_size ])
			split [1] = int (split [1] [0:partial_size])
			split [1] = str (round (
				split [1],
				smaller_amount_integer
			))
			
						
			'''
				if like 1.99 then 2.00
			'''
			if (len (split [1]) > partial_size):
				split [0] = str (int (split[0]) + 1)
				split [1] = split[1][1:]


			'''
				round up if the next digit 
				is greater than or equal
				to 5
			'''
			#if (next >= 5):
			#	split [1] = str (int (split [1]) + 1)		
			#print (split[0], split[1])
		
		split_1_before = ""
		split_1_after = ""
		last_index_of_partial = partial_size - 1
		while (len (split [1]) <= last_index_of_partial):		
			split [1] = "0" + split[1]
			#print ('adding a zero', split [1])

	return split [0] + "." + split[1]