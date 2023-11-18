



'''
	python3 status.py "_interpret/STATUS_unit_kind.py"
'''

import cyte._interpret.unit_kind as unit_kind

from fractions import Fraction

def CHECK_1 ():
	assert (unit_kind.calc ("ml") == "volume")
	assert (unit_kind.calc ("fl oz") == "volume")
	
	assert (unit_kind.calc ("GRAM") == "mass")
	assert (unit_kind.calc ("gram") == "mass")
	
	assert (unit_kind.calc ("kcal") == "energy")


checks = {
	"CHECK 1": CHECK_1
}
	


