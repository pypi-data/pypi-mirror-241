
import basal.config.scan as basal_config_scan
import basal.climate as basal_climate


import inspect
import os
from os.path import dirname, join, normpath

def start ():
	basal_ganglia = basal_config_scan.start ()


	'''
	print ('basal ganglia', basal_ganglia)
	print ('basal ganglia', basal_ganglia.basal)
	print ('basal ganglia file path', basal_ganglia.file_path)
	print ('basal ganglia directory path', basal_ganglia.directory_path)
	'''
	
	'''
		get the absolute paths
	'''
	#caller_directory_path = os.path.dirname (os.path.abspath ((inspect.stack()[1])[1]))
	basal_ganglia.basal ["basal ganglia"]["path"] = (
		normpath (join (
			basal_ganglia.directory_path, 
			basal_ganglia.basal ["basal ganglia"]["path"]
		))
	)
	basal_ganglia.basal ["PFC"]["path"] = (
		normpath (join (
			basal_ganglia.directory_path, 
			basal_ganglia.basal ["PFC"]["path"]
		))
	)
	
	'''
		Add the changed version of the basal config
		to the climate.
	'''
	config = basal_ganglia.basal;
	for field in config: 
		basal_climate.change (field, config [field])
		
	#basal_ganglia = basal_climate.find ("basal ganglia")
	#print ('basal ganglia', basal_ganglia)
	#print ('PFC', basal_climate.find ("PFC"))
	
