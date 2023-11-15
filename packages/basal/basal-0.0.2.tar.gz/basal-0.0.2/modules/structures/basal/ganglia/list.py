


'''
	import basal.ganglia.list as basal_ganglia_list
	basal_ganglia_list.start ()
'''

import basal.climate as basal_climate
from pathlib import Path

import os

def start ():	
	basal_ganglia_path = basal_climate.find ("basal ganglia") ['path']

	

	for trail in Path (basal_ganglia_path).iterdir ():
		name = os.path.relpath (trail, basal_ganglia_path)
	
		print ("name:", name)
	
		'''
		if trail.is_file ():
			print(f"{trail.name}:\n{trail.read_text()}\n")
		'''