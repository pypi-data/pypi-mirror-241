
'''
	python3 status/statuses/vitals/__init__.py "food_and_supps/struct_2/ingredients/quantified_grove/mass_per_package/STATUS_1.py"
'''

import cyte.food.USDA.examples as USDA_examples

import cyte.food.USDA.struct_2 as USDA_struct_2
import cyte.food.USDA.struct_2.ingredients.quantified_grove.printer as quantified_grove_printer
import cyte.food_and_supps.struct_2.ingredients.quantified_grove.mass_per_package as ingredient_mass_per_package

import json

def check_1 ():
	food_struct_2 = USDA_struct_2.calc (
		USDA_examples.RETRIEVE ("branded/walnuts_1882785.json")
	)
	ingredient = ingredient_mass_per_package.calc (
		food_struct_2,
		"protein"
	)
	assert (ingredient ['name'] == "Protein")

	print (json.dumps (ingredient, indent = 4))

	ingredient = ingredient_mass_per_package.calc (
		food_struct_2,
		"vitamin d"
	)
	assert (ingredient ['name'] == "Vitamin D (D2 + D3), International Units")


	return;
	
	
checks = {
	'check 1': check_1
}