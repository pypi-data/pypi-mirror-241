
'''
	doesn't work
'''

'''
	possibilities:

	from fractions import Fraction
	Fraction (4, 3) -> "1.334"
	
	exponent_multiples = 3
		e+0, e+3, e+6, e+9, etc.
		
		whole number length is between 1 and 3
	
		
		   0 -> [   0.000, e+0 ]
		   
	 .000001 -> [   1.000, e-6 ]
	 .000999 -> [ 999.000, e-6 ]
	 
	 .001	 -> [   1.000, e-3 ]  == threshold, if >= 1/1000
	 .00999  -> [   9.990, e-3 ]		   
	 .0999   -> [  99.000, e-3 ]	
	   
		.999 -> [   0.999, e+0 ]
		
		
		
		   1 -> [ 1.000, e+0 ]

		 999 -> [ 999.000, e+0 ]
		1000 -> [ 1.000, e+3 ]    == threshold, if >= 1000 -> e+3
		1334 -> ["1.334", "e+3" ]
		
		1000000 -> [ "1.000", "e+6" ] == threshold, if >= 1000000 -> e+6
		1334000 -> ["1.334", "e+6" ]
		1334000000 -> ["1.334", "e+9" ]
		13341000000 -> ["13.341", "e+9" ]
		133410000000 -> ["133.417", "e+9" ]
	
	
	#
	#	get the remainder
	#
	Fraction (4, 3) -> "1 1/3"	
'''

'''
	plan:
		def round (integer, previous_integer):
			if (integer >= 5):
				return previous_integer + 1
		
			return previous_integer;
	
		import cyte.numbers.sci_note as sci_note
		sci_note.calc (
			Fraction (1, 3),
			round = round
		)
'''

import numpy

'''
def calc (
	number
):
	return numpy.format_float_scientific (
		number, 
		unique = False, 
		precision = 15,
		exp_digits = 2
	)
'''


from fractions import Fraction
import cyte.numbers.decimal.reduce as reduce_decimal

def round (integer, previous_integer):
	if (integer >= 5):
		return previous_integer + 1

	return previous_integer;

'''
	possibility:
		minimum_e_size = 2
			1e+00
			1e+99
			1e+100
'''
def calc (
	number,
	round = round,
	exponent_multiples = 3
):
	the_fraction = Fraction (number)

	if (the_fraction >= 1):
		divisor = Fraction (10 ** exponent_multiples)
		exponent_multiplier = 0
		
		'''
			29000 < 1000    -> false -> exponent_multiplier = 1
			29000 < 1000000 -> true
		'''
		while (the_fraction >= divisor):
			exponent_multiplier += 1
			the_fraction = the_fraction / Fraction (1000)
		
		print ("the_fraction:", the_fraction)
		print ("decimal:", reduce_decimal.start (the_fraction))
		
		return [
			reduce_decimal.start (
				the_fraction, 
				round = lambda integer, smaller_amount_integer : integer 
			),
			f"e+{ str (exponent_multiplier * exponent_multiples) }"
		]
		
		print ('exponent multiplier:', exponent_multiplier)
	
	#else:
		

	

	
	





#
