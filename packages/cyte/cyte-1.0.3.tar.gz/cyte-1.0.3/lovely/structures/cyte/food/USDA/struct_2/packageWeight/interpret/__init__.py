

'''

'''

UNIT_LEGEND = {	
	"oz": "ounces",
	"lb": "pounds",
	"lbs": "pounds",

	"kg": "kilograms",
	"g": "grams",
	"mg": "micrograms",
	"mcg": "milligrams",
	
	"fl oz": "fluid ounces",
	"quart": "quart",
	
	"ml": "milliliters",
	"l": "liters"
}

VOLUME_UNITS = [ 
	"fl oz", 
	"quart",
	
	"ml",
	"l"
]

mass_UNITS = [ 
	"oz", 
	"lb", 
	"lbs",
	
	"g", 
	"kg", 
	"mg", 
	"mcg" 
]


'''
	lb -> g

	oz -> g
	
	g -> g
'''

from fractions import Fraction
import cyte.mass.swap as mass_swap
import cyte.volume.swap as VOLUME_swap

import json

def split_label (LABEL):
	ONE = ""
	TWO = ""

	PART_2 = False
	
	SELECTOR = 0
	LAST_INDEX = len (LABEL) - 1
	while (SELECTOR <= LAST_INDEX):
		CHARACTER = LABEL [SELECTOR]
		
		#print ("CHARACTER:", CHARACTER)
	
		if (CHARACTER == " "):
			SELECTOR += 1
			break;
		else:	
			ONE += CHARACTER
			
			
		SELECTOR += 1
	
		
	while (SELECTOR <= LAST_INDEX):
		CHARACTER = LABEL [SELECTOR]
		TWO += CHARACTER
		SELECTOR += 1
	
	return [ ONE.lower (), TWO.lower () ]


def interpret (PARAM):
	if (type (PARAM) != str):
		return [ "?", "pounds" ]
		
	RETURNS = {}
	SPLITS = PARAM.split ("/")
	
	# print ("splits:", SPLITS)
	
	VOLUME_IS_KNOWN = False
	mass_IS_KNOWN = False
	
	for SPLIT in SPLITS:
		[ AMOUNT, UNIT ] = split_label (SPLIT)
		#[ AMOUNT, UNIT ] = SPLIT.split (" ")
		
		'''
		print (AMOUNT, UNIT)
		print (
			json.dumps (
				{
					"AMOUNT": AMOUNT, 
					"UNIT": UNIT 
				}, 
				indent = 4
			)
		)
		'''
		
		assert (UNIT in UNIT_LEGEND), f"unit: '{ UNIT }'"
		
		if (UNIT in VOLUME_UNITS):
			VOLUME_IS_KNOWN = True
		elif (UNIT in mass_UNITS):
			mass_IS_KNOWN = True;
		else:
			print ("unit:", UNIT)
			raise Exception ("Unit was not found in volume of mass units.")
		
		
		SPRUCED_UNIT = UNIT_LEGEND [ UNIT ]
		
		RETURNS [ SPRUCED_UNIT ] = AMOUNT
	
	
	#print ("VOLUME_IS_KNOWN:", VOLUME_IS_KNOWN)
	#print ("mass_IS_KNOWN:", mass_IS_KNOWN)
	#print ("RETURNS", RETURNS)

	if (mass_IS_KNOWN):
	
		
		#
		#	IF grams IS NOT IN RETURNS,
		# 	THEN TRY TO find ANOTHER UNIT THAT
		#	CAN BE swapPED INTO grams.
		#
		if ("grams" not in RETURNS):
			if ("ounces" in RETURNS):
				AMOUNT_OF_ounces = RETURNS ["ounces"]
			
				RETURNS ["grams"] = str (float (
					mass_swap.START (
						[ AMOUNT, "ounces" ],
						"grams"
					)
				))
				
			elif ("pounds" in RETURNS): 
				AMOUNT = RETURNS ["grams"]
			
				RETURNS ["grams"] = str (float (
					mass_swap.START (
						[ AMOUNT, "pounds" ],
						"grams"
					)
				))
				
			else:
				raise Exception ("COULD NOT DETERMINE PACKAGE mass IN grams.")

		assert ("grams" in RETURNS)

		
		# print ("RETURNS:", RETURNS)
		
		#
		#	IF pounds IS NOT IN RETURNS,
		# 	THEN TRY TO find ANOTHER UNIT THAT
		#	CAN BE swapPED INTO pounds.
		#
		if ("pounds" not in RETURNS):
			if ("ounces" in RETURNS):
				AMOUNT = RETURNS ["ounces"]
			
				RETURNS ["pounds"] = str (float (
					mass_swap.START (
						[ AMOUNT, "ounces" ],
						"pounds"
					)
				))
				
			elif ("grams" in RETURNS): 
				AMOUNT = RETURNS ["grams"]
			
				RETURNS ["pounds"] = str (float (
					mass_swap.START (
						[ AMOUNT, "grams" ],
						"pounds"
					)
				))
				
			else:
				raise Exception ("'pounds' per package could not be calculated.")

		assert ("pounds" in RETURNS)
		
	if (VOLUME_IS_KNOWN):
		#
		#	plan:
		#		calculate ([ "liters", "fluid ounces" ])
		#
	
		def calculate ():
			return;
		
	
		if ("liters" not in RETURNS):
			if ("fluid ounces" in RETURNS):
				UNIT_1 = "fluid ounces"
				UNIT_2 = "liters"

				AMOUNT = RETURNS [ UNIT_1 ]
				RETURNS [ UNIT_2 ] = str (float (
					VOLUME_swap.START (
						[ AMOUNT, UNIT_1 ],
						UNIT_2
					)
				))
				
			elif ("milliliters" in RETURNS): 
				UNIT_1 = "milliliters"
				UNIT_2 = "liters"

				AMOUNT = RETURNS [ UNIT_1 ]
				RETURNS [ UNIT_2 ] = str (float (
					VOLUME_swap.START (
						[ AMOUNT, UNIT_1 ],
						UNIT_2
					)
				))
				
			else:
				raise Exception ("'liters' per package could not be calculated.")

	return RETURNS

