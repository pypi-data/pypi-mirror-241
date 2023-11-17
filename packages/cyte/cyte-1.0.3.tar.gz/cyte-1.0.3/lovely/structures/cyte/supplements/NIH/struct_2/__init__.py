


'''
import cyte.supplements.NIH.struct_2 as struct_2
supplement_struct_2 = struct_2.calc (NIH_supplement_data)
'''

import cyte.supplements.NIH.struct_2.form as form 
import cyte.supplements.NIH.struct_2.form.unit as form_unit
import cyte.supplements.NIH.struct_2.defined.serving_size_quantity as defined_serving_size_quantity 
import cyte.supplements.NIH.struct_2.ingredients.quantified as INGREDIENTS_QUANTIFIED 
import cyte.supplements.NIH.struct_2.mass.algorithm_1 as mass_algorithm_1

import cyte.recipes.struct_2.ingredients.quantified_grove.sum as recipe_quantified_grove_sum
import cyte.recipes.struct_2.ingredients.quantified_grove.portions as recipe_quantified_grove_portions



import json

from fractions import Fraction

def calc (
	nih_supplement_data
):
	assert ("fullName" in nih_supplement_data)
	assert ("brandName" in nih_supplement_data)
	assert ("id" in nih_supplement_data)
	assert ("servingsPerContainer" in nih_supplement_data)

	struct_2_data = {
		"product": {
			"name":	nih_supplement_data ["fullName"],
			
			#
			#	Dietary Supplement Label Database
			#
			"DSLD ID": str (nih_supplement_data ["id"]),
			"UPC": nih_supplement_data ["upcSku"]			
		},
		
		"brand": {
			"name":	nih_supplement_data ["brandName"]
		},
		
		"statements": nih_supplement_data ["statements"],
		
		"form": {},
		
		#
		#	pertinent:
		#		userGroups
		#		servingSizes
		#
		"stated recommendations": {},
		
		"defined": {
			"servings per container": nih_supplement_data ["servingsPerContainer"],
			"serving size": {}
		},
		
		"ingredients": {
			"quantified grove": [],			
			"unquantified": []
		},
		
		"mass": {
			
		}
	}
	
	struct_2_data ["form"]["unit"] = form_unit.calc (nih_supplement_data)
	struct_2_data ["form"]["quantity"] = str (form.calc_QUANTITY (
		nih_supplement_data,
		struct_2_data
	))	

	struct_2_data [
		"defined"
	]["serving size"]["quantity"] = defined_serving_size_quantity.calc (
		nih_supplement_data,
		struct_2_data
	)
	
	struct_2_data ["form"]["rounded"] = "?"
	if (
		struct_2_data ["form"]["unit"] == "gram"
	):
		is_rounded = struct_2_data ["form"]["quantity"] != (
			Fraction (struct_2_data ["defined"]["servings per container"]) *
			Fraction (struct_2_data ["defined"]["serving size"]["quantity"])
		)
	
		if (is_rounded):
			struct_2_data ["form"]["rounded"] = "yes"
	
	
	
	#print ("struct_2_data:", json.dumps (struct_2_data, indent = 4))
	
	struct_2_data ["ingredients"]["quantified grove"] = INGREDIENTS_QUANTIFIED.calc (
		nih_supplement_data,
		struct_2_data
	)
	
	struct_2_data ["ingredients"]["unquantified"] = nih_supplement_data [
		"otheringredients"
	] [ "ingredients" ]
	
	
	calculated_masses = mass_algorithm_1.calc (
		nih_supplement_data, 
		struct_2_data
	)
	#print ("calculated_masses masses", calculated_masses)
	
	for calculated in calculated_masses:
		struct_2_data ["mass"][ calculated ] = calculated_masses [ calculated ]

	
	'''
		After this is shared calculations that food and supps use.	
	'''
	struct_2_data ["mass"] ["of quantified ingredients, with effectuals"] = recipe_quantified_grove_sum.calc (
		include_effectuals = True,
		quantified_grove = struct_2_data ["ingredients"]["quantified grove"]
	)
	struct_2_data ["mass"] ["of quantified ingredients, without effectuals"] = recipe_quantified_grove_sum.calc (
		include_effectuals = False,
		quantified_grove = struct_2_data ["ingredients"]["quantified grove"]
	)	
	recipe_quantified_grove_portions.calc (
		nih_supplement_data,
		struct_2_data
	)



	return struct_2_data