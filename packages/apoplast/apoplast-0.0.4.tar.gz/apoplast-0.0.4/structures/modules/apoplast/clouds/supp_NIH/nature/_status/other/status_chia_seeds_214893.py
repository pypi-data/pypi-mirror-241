

'''
status_chia_seeds_214893
'''


import apoplast.clouds.supp_NIH.nature as supp_NIH_nature
import apoplast.clouds.supp_NIH.examples as NIH_examples

def check_1 ():	
	supp_NIH_example = NIH_examples.retrieve ("other/chia_seeds_214893.JSON")
	nature = supp_NIH_nature.create (supp_NIH_example)

	return;
	
checks = {
	"check 1": check_1
}