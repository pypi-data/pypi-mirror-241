
'''
	This adds products to the recipe.

	Currently it also adds products to a skipped list.
'''



'''
import cyte.recipes.s2_tf1.ingredients.quantified_grove.aggregator as quantified_grove_aggregator
quantified_grove_aggregator.calc (
	recipe_quantified_grove = [],
	product_quantified_grove = []
)
'''

'''
	steps:
		1. create a flat list of structs from the product "quantified grove"
		
		2. attach (merge) the product structs to the "product struct grove"
			* if not in "product struct grove", then skip.
		
			1. make sure that there aren't any missing intermediaries
		
		3. merge the product struct grove into the recipe struct grove
'''

def scribble (params):
	print (params)


import json
	
import cyte.recipes.s2_tf1.ingredients.quantified_grove.find.structs_list as find_structs_list

import cyte.structs.DB.access as access
import cyte.structs.scan.names.has as struct_has_name
import cyte.structs.scan.trees_form_1 as trees_form_1
import cyte.structs.scan.trees_form_1.attach as attach_product_struct
import cyte.structs.scan.trees_form_1.for_each as for_each
import cyte.structs.scan.trees_form_1.find.region as find_region
import cyte.structs.scan.trees_form_1.printer as trees_form_1_printer

import cyte.recipes.s2_tf1.ingredients.quantified_grove.aggregator.is_missing_intermediaries as is_missing_intermediaries
import cyte.recipes.s2_tf1.ingredients.quantified_grove.aggregator.calculate_per_recipe as calculate_per_recipe

def print_struct_names (quantified_grove):
	print ("$ procedure: print_struct_names")

	for ingredient in quantified_grove:
		print ("   ", ingredient ['name'])

	return;

def calc (
	recipe_struct_grove,
	product_quantified_grove,
	product,
	packets_count
):
	print ()
	print ("$ procedure: s2_tf1 aggregator")

	print_struct_names (product_quantified_grove)

	skipped = []
	product_ingredients_structs_list = []
	structs_db_1 = access.DB ()

	'''
		builds:
			structs_list
			skipped # structs_skipped
	'''
	find_structs_list.start (
		structs_list = product_ingredients_structs_list,
		skipped = skipped,

		structs_db = structs_db_1,
		product_quantified_grove = product_quantified_grove,
		product = product
	)

	#print (json.dumps (product_ingredients_structs_list, indent = 4))

	'''
	
	'''
	print ("	structs found:");
	for product_ingredient_struct in product_ingredients_structs_list:
		print ("		", product_ingredient_struct ["names"])

	
	'''
		These are skipped because they are not FDA essential nutrients.
	'''
	print ()
	print ("	skipped structs:", skipped)

	'''
		structs_db_1 dict shouldn't be modified, but in case it is,
		utilize a difference one.
	'''
	structs_db_2 = access.DB ()
	product_struct_grove = trees_form_1.start (structs_db_2)
	#trees_form_1_printer.write (product_struct_grove)

	
	'''
		attach (merge) the "product structs" 
		into the "structs tree form 1"
	'''
	for product_struct in product_ingredients_structs_list:
		print ("product_struct ::", product_struct)
		
		attach_product_struct.start (
			product_struct, 
			product_struct_grove
		)

	is_missing_intermediaries.calc (product_struct_grove)
	

	'''
		Loop through the product_struct_grove
		and aggregate each product into the
		recipe_struct_grove.
	'''
	def for_each_fn (params):
		product_struct = params.struct;
			
		if ("found" in product_struct and product_struct ["found"] == "yes"):
			product_struct_region = product_struct ["region"]
		
			recipe_struct = find_region.start (
				product_struct_region, 
				recipe_struct_grove
			)
			
			
			'''
				
			'''
			calculate_per_recipe.start (
				product_struct,
				packets_count
			)
			
			'''
				add the ingredient to ingredients
			'''
			recipe_struct ["ingredients"].append (
				product_struct ["ingredient"]
			)
			
			'''
			mass_per_package_fraction_string_grams = "0"
			try:
				mass_per_package_fraction_string_grams = product_struct [""]
			except Exception as E:
				pass;
			
			recipe_struct.append ({
				"ellipse": 1,
				"mass": {
					"per package": {
						"fraction string grams": mass_per_package_fraction_string_grams
					}
				}
			})
			'''

	for_each.start (
		product_struct_grove,
		for_each = for_each_fn
	)	
	
	
	return {
		"product structs list": product_ingredients_structs_list
	}