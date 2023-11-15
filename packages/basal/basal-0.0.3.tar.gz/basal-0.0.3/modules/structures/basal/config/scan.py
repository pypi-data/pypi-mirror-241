


from tinydb import TinyDB, Query



'''
import basal.climate.scan as basal_climate_scan
basal_ganglia = basal_climate_scan.start ("basal ganglia")
'''




import pathlib
from os.path import dirname, join, normpath
import sys
import copy
import json
import os.path
import inspect
import os

import botanical.paths.files.scan.JSON as scan_JSON_path

'''
	if current directory is /1/1/1/1/1/
	
	looks in each directory for a basal.JSON file
	
	possibilities:
		basal.yaml
'''

name = "basal.JSON"

def start ():
	search_directory = os.path.abspath ((inspect.stack()[2])[1])
	
	searched = []
	while (search_directory != "/"):
		search_directory = os.path.dirname (search_directory)
		#print ("search:", search_directory)
		
		search_file_path = normpath (join (search_directory, name))
		#print ("search:", search_file_path)
		
		basal_JSON_exists = os.path.isfile (search_file_path) 
		if (basal_JSON_exists):
			class proceeds:
				def __init__ (this):
					this.basal = scan_JSON_path.start (search_file_path);
					this.file_path = search_file_path
					this.directory_path = search_directory
		
			return proceeds ()
		
		searched.append (search_file_path)
	
	
	raise Exception (f"""
		
A "basal.JSON" file was not found.
		
These paths were searched: { json.dumps (searched, indent = 4) }
		
	""")
	

