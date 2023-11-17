
'''
import cyte.food_and_supps.struct_2.ingredients.quantified_grove.for_each as quantified_grove_for_each_ingredient
quantified_grove_for_each_ingredient.start (
	quantified_grove,
	course = course
)

'''

'''
	returns False -> not found
	returns True -> found
'''
def nothing (ingredient):
	return False

def start (
	quantified_grove,
	course = nothing
):
	for ingredient in quantified_grove:
		ingredient_quantified_grove = ingredient ["quantified grove"]
		
		found = course (ingredient)
		if (found):
			return ingredient;
		
		start (ingredient_quantified_grove)

	return;