





'''
	python3 status/statuses/vitals/__init__.py  "recipes/s2_tf1/_status/5_plethora/STATUS_recipe.py"
'''

'''
	零: 0
	一: 1
	二: 2
	三: 3
	四: 4
	五: 5
	六: 6
	七: 7
	八: 8
	九: 9
	十: 10
	
	朋友: friend
	梦: dreams
	梦想: dream
	钱: money
	家庭: family
'''

import cyte.food.USDA.examples as USDA_examples
import cyte.food.USDA.struct_2 as USDA_struct_2

import cyte.supplements.NIH.examples as NIH_examples
import cyte.supplements.NIH.struct_2 as struct_2

import cyte.recipes.s2_tf1 as struct_2_recipes

import cyte.structs.scan.trees_form_1.find.region as find_region

import json

def check_1 ():	
	walnuts_1882785 = USDA_struct_2.calc (
		USDA_examples.RETRIEVE ("branded/walnuts_1882785.json")
	)
	calcium_261967 = struct_2.calc (
		NIH_examples.RETRIEVE ("tablets/calcium_261967.JSON")
	)
	chia_seeds_214893 = struct_2.calc (NIH_examples.RETRIEVE ("other/chia_seeds_214893.json"))
	
	recipe = struct_2_recipes.calc ({
		"products": [
			[ chia_seeds_214893, 2 ],
			[ walnuts_1882785, 4 ],
			[ calcium_261967, 11 ]
		]
	})
	
	recipe_struct_grove = recipe.recipe_struct_grove;
	
	from os.path import dirname, join, normpath
	import sys
	import pathlib
	import cyte._sculpt as sculpt
	sculpt.start (
		normpath (join (pathlib.Path (__file__).parent.resolve (), "recipe_struct_grove.json")),
		json.dumps (recipe_struct_grove, indent = 4)
	)
	
	
	'''
		This should really find the struct in by the name
		not the region #.
	'''
	vitamin_d = find_region.start (63, recipe_struct_grove)
	assert (
		vitamin_d ["ingredients"][0]["mass"]["per recipe"]["fraction string grams"] ==
		"0"	
	), vitamin_d
	assert (
		vitamin_d ["mass"]["per recipe"]["fraction string grams"] ==
		"0"	
	), vitamin_d
	
	'''
		chia seeds: 75.66666666666667 * 2 = 151.33
		walnuts:    64.8766 * 4 = 259.5064
		
		410.8397333333333 = 259.5064 + 151.33
	'''
	def protein ():
		ingredient = find_region.start (1, recipe_struct_grove)

		print ("protein", json.dumps (ingredient, indent = 4))

		'''
			151.33 ~= 454/3
		'''
		assert (
			ingredient ["ingredients"][0]["mass"]["per recipe"]["fraction string grams"] ==
			"454/3"
		)
		
		'''
			259.5064 ~= 456528486851663599/1759218604441600
		'''
		assert (
			ingredient ["ingredients"][1]["mass"]["per recipe"]["fraction string grams"] ==
			"456528486851663599/1759218604441600"
		)
		
		'''
			
		'''
		assert (
			ingredient ["mass"]["per recipe"]["fraction string grams"] ==
			"2168270706971477197/5277655813324800"
		)
		assert (
			ingredient ["mass"]["per recipe"]["float string grams"] ==
			"410.8397333333333"
		)
				
	protein ()

	return;
	
	
	
checks = {
	"recipe with 2 different products": check_1
}