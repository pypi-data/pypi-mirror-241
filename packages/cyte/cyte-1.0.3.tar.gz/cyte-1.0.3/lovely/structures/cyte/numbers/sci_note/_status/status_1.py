

'''
	python3 status/statuses/vitals/__init__.py numbers/sci_note/_status/status_1.py
'''

import cyte.numbers.sci_note as sci_note

from fractions import Fraction

def status_1 ():	
	assert (sci_note.calc ('9999999') == [ "9.999", "e+6" ]), sci_note.calc ('9999999')

	s_note = sci_note.calc (Fraction (4, 3))
	assert (s_note == [ "1.333", "e+0" ]), s_note
	
	s_note = sci_note.calc ('5.0057')
	assert (s_note == [ "5.006", "e+0" ]), s_note
	
	s_note = sci_note.calc ('5000.0057')
	assert (s_note == [ "5.000", "e+3" ]), s_note
	
	assert (sci_note.calc ('999') == [ "999.000", "e+0" ])	
	assert (sci_note.calc ('1000') == [ "1.000", "e+3" ])
	assert (sci_note.calc ('1000000') == [ "1.000", "e+6" ])	
	
	assert (sci_note.calc ('10000000') == [ "1.000", "e+9" ])	
	assert (sci_note.calc ('1000000000') == [ "100.000", "e+9" ])	
	
	
	
	
	
checks = {
	"status 1": status_1
}