

'''
	python3 status/statuses/vitals/__init__.py  "food/USDA/struct_2/packageWeight/interpret/STATUS_1.py"
'''

import json

import cyte.food.USDA.struct_2.packageWeight.interpret as interpreter


def check_1 ():	
	proceeds = interpreter.interpret ("12 oz/340 g")
	assert (proceeds ['ounces'] == '12')
	assert (proceeds ['pounds'] == '0.75')
	assert (proceeds ['grams'] == '340')
	
	proceeds = interpreter.interpret ("12 fl oz/355 mL")
	assert (proceeds ['fluid ounces'] == '12')
	assert (proceeds ['milliliters'] == '355')
	assert (proceeds ['liters'] == '0.354882')

	return
	
	
checks = {
	"check 1": check_1
}