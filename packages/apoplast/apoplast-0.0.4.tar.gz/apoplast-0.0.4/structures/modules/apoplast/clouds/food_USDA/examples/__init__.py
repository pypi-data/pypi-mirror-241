


'''
	import apoplast.clouds.food_USDA.examples as USDA_examples
	walnuts_1882785 = USDA_examples.retrieve ("branded/walnuts_1882785.json")
'''

def retrieve (path):
	import pathlib
	from os.path import dirname, join, normpath

	this_directory = pathlib.Path (__file__).parent.resolve ()
	example_path = normpath (join (this_directory, path))

	import json
	with open (example_path) as FP:
		data = json.load (FP)
	

	return data