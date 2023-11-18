


pattern:
{
	"emblem": "",
	
	"affiliate": {
		"links": []
	},
	
	"USDA_food": {},
	"NIH_supp": {},
	
	"nature": {
		"treasure": {
			"name": "",
			"UPC": "",
			"DSLD ID": "",
			"FDC ID": ""
		},
		"brand": {
			"name": ""
		},

		"measures": {
			
			#
			#	if a supp
			#
			"form": "form": {
				"unit": "Tablet",
				"amount": "90",
				
				#
				#	
				#
				"estimate": "no",
				"rounded": "up"
			},
			
			#
			#	For NIH supps these are necessary for
			#	calculating the mass.
			#
			"defined": {
				"servings per container": ""
			},
			"energy": {
				"per package": {
					"calories": {
						"decimal string: "",
						"fraction string": ""
					},
					"joules": {
						"decimal string: "",
						"fraction string": ""
					}
				}
			},
			
			"mass": {
				"per package": {
					"grams": {
						"decimal string: "",
						"fraction string": ""
					},
					"pounds": {
						"decimal string: "",
						"fraction string": ""
					}
				}
			},
			"mass, including mass equivalents": {
				"in people": {
					"per package": {
						"grams": {
							"decimal string: "",
							"fraction string": ""
						},
						"pounds": {
							"decimal string: "",
							"fraction string": ""
						}
					}
				}
			},
			"mass equivalents": {
				"per package": {
					"grams": {
						"decimal string: "",
						"fraction string": ""
					},
					"pounds": {
						"decimal string: "",
						"fraction string": ""
					}
				}
			},
			
			"volume": {
				"per package": {
					"liters": {
						"decimal string: "",
						"fraction string": ""
					}
				}
			}
		},
		
		
		"measured ingredients": {
			"grove": [{
				"name": "vitamin b",
				
				
				#
				#	essential nutrient
				#
				"essential": {
					"names": [ "vitamin b", "cobalamin" ],
					"includes": []
				},
				
				
				"measures": {
					#
					#	
					#
					"mass": {
						"per package": {
							"grams": {
								"decimal string": "",
								"fraction string": ""
							},
							"ounces": {
								
							}
						}
					},
					
					#
					#	"equivalents"
					#
					"mass equivalent": {
						"per package": {
							"grams": {
								"equivalent": "DFE",
								"decimal string": "",
								"fraction string": ""
							}
						}
					},
					
					#
					#	if IU
					#
					"biological activity": {
						"per package": {
							"IU": {
								"decimal string": "",
								"fraction string": ""
							}
						}
					}
				}
			}]
		},
		
		"unmeasured ingredients": {

			#
			#	USDA sends a string "ingredients"
			#
			"string": "",

			#
			#	NIH sends a list of "otherIngredients"
			#
			"list": []
		},

		"reference": [],
	},		


	#
	#	unique sections
	#

	#
	#	unique to NIH supps
	#
	"statements": []
	
	
	

	"calculated": {
		
		
		
		
		#
		#	this intermediary might be necessary
		#
		"quantified essential nutrients list": [],
		
		
		"quantified essential nutrients grove": [],
		
		#
		#	priority 2:
		#	
		#	based on shape.current_1
		#
		"quantified ingredients current": [],
	}
}