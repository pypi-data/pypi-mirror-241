


'''
import cyte.recipes.struct_2.ingredients.quantified_grove.sum as quantified_grove_sum
mass_including_effectual = quantified_grove_sum.calc (
	include_effectuals = True,
	quantified_grove = []
)
'''

from fractions import Fraction
import cyte.mass_effectual.is_effectual as is_effectual

def calc (
	* positionals, 
	include_effectuals = True,
	quantified_grove = []
):
	sum = 0

	skipped = []

	for ingredient in quantified_grove:	
		#print ("name:", ingredient ['name'], ingredient)
	
		if ("mass" in ingredient):
			try:
				sum += Fraction (ingredient ["mass"]["per package"]["fraction string grams"])
			except Exception:
				skipped.append (ingredient ['name'])

		elif (include_effectuals == True and "effectual mass" in ingredient):
			unit = ingredient ["effectual mass"]["per package"]["fraction string"]["unit"]
		
			if (is_effectual.calc (unit)):
				raise Exception (f"effectual unit: { unit } not accounted for")
			
			
			

	return {
		"fraction string grams": str (sum),
		"float grams": float (sum),
		"skipped": skipped
	}