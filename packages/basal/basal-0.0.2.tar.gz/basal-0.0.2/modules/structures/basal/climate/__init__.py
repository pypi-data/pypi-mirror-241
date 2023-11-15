


from tinydb import TinyDB, Query

'''
import basal.climate as basal_climate
basal_climate.change ("basal ganglia", {
	"path": ""	
})
'''

'''
import basal.climate as basal_climate
basal_ganglia = basal_climate.find ("basal ganglia")
'''

'''
climate = {
	"reservoir": {
		"port": ""
	},
	"basal ganglia": {
		"path": ""
	},
	"PFC": {
		"path": ""
	}
}
'''


import pathlib
from os.path import dirname, join, normpath
import sys
import copy



import botanical.paths.files.scan.JSON as scan_JSON_path

this_directory = pathlib.Path (__file__).parent.resolve ()
climate_JSON_path = normpath (join (this_directory, "climate.JSON"))

import json

def change (field, plant):
	current_JSON = scan_JSON_path.start (climate_JSON_path)
	current_JSON [ field ] = plant;

	FP = open (climate_JSON_path, "w")
	FP.write (json.dumps (current_JSON, indent = 4))
	FP.close ()

	print (current_JSON)
	return;

	#global climate;
	climate [ field ] = plant


def find (field):
	return scan_JSON_path.start (climate_JSON_path) [ field ]

	#return copy.deepcopy (climate) [ field ]