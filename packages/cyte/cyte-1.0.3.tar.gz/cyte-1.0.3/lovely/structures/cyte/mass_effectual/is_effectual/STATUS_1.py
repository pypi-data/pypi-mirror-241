



'''
	python3 status/statuses/vitals/__init__.py "mass_effectual/is_effectual/STATUS_1.py"
'''


import json
import cyte.mass_effectual.is_effectual as is_effectual

def check_1 ():	
	assert (is_effectual.calc ("mcg RAE") == True)
	assert (is_effectual.calc ("mcg ne") == False)
	
checks = {
	"check 1": check_1
}