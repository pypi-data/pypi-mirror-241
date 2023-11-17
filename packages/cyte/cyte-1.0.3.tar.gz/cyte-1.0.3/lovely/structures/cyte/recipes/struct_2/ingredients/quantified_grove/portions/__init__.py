

'''
import cyte.recipes.struct_2.ingredients.quantified_grove.portions as quantified_grove_portions
mass_including_effectual = quantified_grove_sum.calc (
	include_effectuals = True,
	quantified_grove = []
)
'''

'''
	This calculate the (fractional, proportional) percentage
	of the struct as a percentage of the:
	
		quantified ingredients, with effectuals

'''


'''
	this loop is very similar to the "sum" loop
'''

from fractions import Fraction
import json


import cyte.mass_effectual.is_effectual as is_effectual
import cyte.percentage.from_fraction as percentage_from_fraction

def calc (
	usda_food_data,
	treasure
):
	quantified_grove = treasure ["ingredients"] ["quantified grove"]

	mass_of_quantified_ingredients_including_effectual = Fraction (
		treasure [
			"mass"
		][
			"of quantified ingredients, with effectuals"
		][
			"fraction string grams"
		]
	)

	mass_per_package_listed = False;
	try:
		mass_per_package_listed = Fraction (
			treasure ['mass'] ["listed"] ["per package, in grams"]
		)
	except Exception as E:
		print (
			'A package mass was not found in the API data of: ', 
			treasure ['product']['name']
		)


	for ingredient in quantified_grove:		
		if ("mass" in ingredient):
			try:
				effectual_portion_from_sum = Fraction (
					Fraction (ingredient ["mass"]["per package"]["fraction string grams"]),
					mass_of_quantified_ingredients_including_effectual
				)
				
				ingredient ["mass"] ["effectual portion per package"] = {
					"from quantified ingredients": {
						"fraction float string": str (float (effectual_portion_from_sum)),
						"fraction string": str (effectual_portion_from_sum),
						"percentage string": percentage_from_fraction.calc (effectual_portion_from_sum)
					}
				}
			except Exception as E:
				print ('The effectual portion per package could not be calculated.')
			
				ingredient ["mass"] ["effectual portion per package"] = {
					"from quantified ingredients": {
						"fraction float string": "",
						"fraction string": "",
						"percentage string": ""
					}
				}
				
			ingredient ["mass"] ["compositional portion per package"] = {
				"from defined package mass": {
					"fraction float string": "",
					"fraction string": "",
					"percentage string": ""
				}
			}
			
			if (type (mass_per_package_listed) == Fraction):		
				try:
					compositional_portion_from_listed = Fraction (
						Fraction (ingredient ["mass"]["per package"]["fraction string grams"]),
						mass_per_package_listed
					)
					
					ingredient ["mass"] ["compositional portion per package"] = {
						"from defined package mass": {
							"fraction float string": str (float (compositional_portion_from_listed)),
							"fraction string": str (compositional_portion_from_listed),
							"percentage string": percentage_from_fraction.calc (compositional_portion_from_listed)
						}
					}
					
				except Exception as E:
					print ("Exception:", E)
					print ("The ingredient mass was not found for:", ingredient ['name'])
					print ("This ingredient was not found:", json.dumps (ingredient, indent = 4))
					
					
			

		elif ("effectual mass" in ingredient):
			unit = ingredient ["effectual mass"]["per package"]["fraction string"]["unit"]
		
			if (is_effectual.calc (unit)):
				raise Exception (f"effectual unit: { unit } not accounted for")

	return;