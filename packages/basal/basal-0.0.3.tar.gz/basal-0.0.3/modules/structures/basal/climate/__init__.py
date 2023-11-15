

'''
import basal.climate as basal_climate
basal_climate.change ("basal ganglia", {
	"path": memories_path
})

import basal.climate as basal_climate
basal_ganglia = basal_climate.find ("basal ganglia")

print ('basal ganglia', basal_ganglia)

'''

import copy

climate = {}

def change (field, plant):
	#global CLIMATE;
	climate [ field ] = plant


def find (field):
	#print ("climate:", climate)

	return copy.deepcopy (climate) [ field ]