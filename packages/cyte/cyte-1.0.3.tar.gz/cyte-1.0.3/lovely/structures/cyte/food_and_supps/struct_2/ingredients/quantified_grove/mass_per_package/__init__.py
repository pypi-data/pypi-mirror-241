

'''
"quantified grove": [
	{
		"name": "Fatty acids, total trans",
		"struct": {
			"includes": [],
			"names": [
				"trans fat",
				"fatty acids, total trans"
			],
			"region": 5
		},
		"mass": {
			"per package": {
				"float": {
					"amount": 0.0,
					"unit": "g"
				},
				"fraction string": {
					"amount": "0",
					"unit": "g"
				},
				"fraction string grams": "0",
				"float grams": 0.0
			},
			"per serving": {
				"float": {
					"amount": 0.0,
					"unit": "g"
				},
				"fraction string": {
					"amount": "0",
					"unit": "g"
				}
			},
		},
		"quantified grove": []
	}
]
'''

import cyte.food_and_supps.struct_2.ingredients.quantified_grove.for_each as quantified_grove_for_each_ingredient


def find (
	quantified_grove,
	ingredient_name
):
	for ingredient in quantified_grove:
		struct_names = ingredient ["struct"] ["names"]
		
		for name in struct_names:
			if (name == ingredient_name):
				return ingredient;
		
		ingredient_quantified_grove = ingredient ["quantified grove"]
		found = find (ingredient_quantified_grove, ingredient_name)
		if (type (found) == dict):
			return found

	return False

def calc (
	treasure_struct_2,
	ingredient_name = "",
	include_effectual = True
):
	#
	#	trees_form_1_grove
	#
	quantified_grove = treasure_struct_2 ["ingredients"] ["quantified grove"]

	ingredient = find (
		quantified_grove,
		ingredient_name
	)


	return ingredient

	#mass_per_package = treasure_struct_2
	
	
	
	
	
	
	
	
	
	
	
	
	
	