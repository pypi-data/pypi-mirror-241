

'''
import cyte.mass_effectual.is_effectual as is_effectual
is_effectual.calc (unit)
'''

effectual_units = [
	[ "mcg RAE" ],
	[ "mg alpha-tocopherol" ],
	[ "mg NE" ],
	[ "1 mcg DFE" ]
]


def calc (unit):
	for effectual_unit_variations in effectual_units:
		for effectual_unit_variation in effectual_unit_variations:
			if (effectual_unit_variation == unit):
				return True
				
	return False