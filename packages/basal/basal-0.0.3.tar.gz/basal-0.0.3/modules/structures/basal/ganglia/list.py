


'''
	import basal.ganglia.list as basal_ganglia_list
	basal_ganglia_list.start ()
'''

import basal.climate as basal_climate
from pathlib import Path

import os

def start ():	
	basal_ganglia = basal_climate.find ("basal ganglia")	
	basal_ganglia_path = basal_ganglia ['path']
	
	directory_names = []
	for trail in Path (basal_ganglia_path).iterdir ():
		name = os.path.relpath (trail, basal_ganglia_path)
		
		if trail.is_dir ():
			directory_names.append (name)
	
		else:
			raise Exception (f'found a path that is not a directory: \n\n\t{ name }\n')
		
	
		'''
		if trail.is_file ():
			print(f"{trail.name}:\n{trail.read_text()}\n")
		'''
		
	return directory_names;