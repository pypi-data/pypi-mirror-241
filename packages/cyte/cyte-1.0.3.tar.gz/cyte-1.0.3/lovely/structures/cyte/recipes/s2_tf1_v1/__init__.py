

'''
import cyte.recipes.s2_tf1_v1 as struct_2_recipes
import cyte.structs.DB.access as access
import cyte.structs.scan.trees_form_1 as trees_form_1

recipe = struct_2_recipes.calc ({
	#
	#	struct 2 products
	#
	"products": [
		{
			"product": { "FDC ID": "" }
		},
		{
			"product": { "DSLD": "" }
		}
	],
	"structs grove": trees_form_1.start (access.DB ())
})

recipe_struct_grove = recipe.recipe_struct_grove;
'''


import cyte.recipes.s2_tf1_v1.ingredients.quantified_grove.aggregator as quantified_grove_aggregator
import cyte.recipes.s2_tf1_v1.ingredients.quantified_grove.sum as quantified_grove_sum

import cyte.structs.scan.trees_form_1.for_each as for_each
import cyte.structs.scan.trees_form_1 as trees_form_1
import cyte.structs.scan.trees_form_1.printer as trees_form_1_printer
import cyte.structs.DB.access as access



'''
	seems like this attaches structs
	to the ingredients
'''
def prepare_the_recipe_struct_grove ():
	print ()
	print ('$ procedure: prepare_the_recipe_struct_grove')

	recipe_struct_grove = trees_form_1.start (access.DB ())

	def for_each_fn (params):
		print ('	attaching', params.struct ['names'])
	
		struct = params.struct;
		struct ["ingredients"] = []

	for_each.start (
		recipe_struct_grove,
		for_each = for_each_fn
	)	
	
	return recipe_struct_grove

def calc (
	delivery,
	records = 1
):
	print ()
	print ('$ procedure: calc (the s2_tf1_v1) essential ingredients')
	
	products = delivery ["products"]
	
	'''
		This adds the "product sequential" field to the treasure
		so as to include the sequential number in the recipe,
		because it might be useful.
	'''
	product_count = 1
	for product in products:
		product ["product sequential"] = product_count;
		product_count += 1
	
	
	'''
		This prepares the essential nutrients grove
		that all of the essential nutrients are added to.
	'''
	recipe_struct_grove = prepare_the_recipe_struct_grove ()
	# trees_form_1_printer.write (recipe_struct_grove)
	
	'''
		1 by 1, this merges the "foods or supps" into 
		the essential nutrients grove.
	'''
	counter_1 = 0
	for product in products:
		counter_1 += 1
	
		quantified_grove_aggregator.calc (
			recipe_struct_grove,
			product ["ingredients"]["quantified grove"],
			product
		)
		
	'''
		
	'''
	quantified_grove_sum.calc (recipe_struct_grove)

	def for_each_fn (params):
		struct = params.struct;

	for_each.start (
		recipe_struct_grove,
		for_each = for_each_fn
	)	

	class recipe:
		def __init__ (this, recipe_struct_grove):
			this.recipe_struct_grove = recipe_struct_grove

	return recipe (
		recipe_struct_grove
	)