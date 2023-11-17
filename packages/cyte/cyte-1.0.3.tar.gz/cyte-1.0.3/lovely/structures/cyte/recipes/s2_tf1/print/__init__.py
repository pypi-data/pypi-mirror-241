

'''
import cyte.recipes.s2_tf1.print as print_struct_2_recipes
print_struct_2_recipes.currently (recipe_struct_grove)
'''


def currently (recipe_struct_grove, story = 0):
	for struct_grove in recipe_struct_grove:
		indent = " " * (story * 4)
		
		print (
			indent,
			struct_grove ['names'], 
			struct_grove ['mass']['per recipe']['float string grams']
		)
	
		if (len (struct_grove ["includes structs"]) >= 1):
			currently (
				struct_grove ["includes structs"],
				story = story + 1
			)
			

	return;