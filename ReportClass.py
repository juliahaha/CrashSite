date_crash = None
time_crash = None
city_crash = None
crash_type = None
veh1_crash = None
veh2_crash = None
crash_obj = None
weather = None
injury = None
pol_rep = None

# %SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files\Hewlett-Packard\SimplePass\;c:\Program Files (x86)\ATI Technologies\ATI.ACE\Core-Static;C:\Python27\ArcGIS10.1\python

class Incident(object):
	def __init__(self, date_crash, time_crash,veh1_crash, veh2_crash="",crash_obj="",weather="", injury="", pol_rep=""):
		self.date_crash = date_crash
		self.time_crash = time_crash
		self.city_crash = city_crash
		self.veh1_crash = veh1_crash
		self.veh2_crash = veh2_crash
		self.crash_obj = crash_obj
		self.weather = weather
		self.injury = injury
		self.pol_rep = pol_rep

def types_of_vehicles():
	veh1_crash = raw_input("What kind of vehicle were you driving, or were you walking?")
	if str.lower(veh1_crash) == "bicycle" or str.lower(veh1_crash) == "bike":
		veh1_crash = 1
	elif str.lower(veh1_crash) == "walking":
		veh1_crash = 2
	elif str.lower(veh1_crash) == "car":
		veh1_crash = 3	
	elif str.lower(veh1_crash) == "motorcycle":
		veh1_crash = 4
	elif str.lower(veh1_crash) == "unicycle":
		veh1_crash = 5
	elif str.lower(veh1_crash) == "skateboard":
		veh1_crash = 6
	else:
		veh1_crash = "Unusual input:" + veh1_crash
	return veh1_crash

	veh2_crash = raw_input("Was the crash with another vehicle or an object?")
	if str.lower(veh2_crash) == "vehicle" or str.lower(veh2_crash) == "another vehicle":
		veh2_crash = raw_input("What kind of vehicle?")
		if str.lower(veh2_crash) == "bicycle" or str.lower(veh2_crash) == "bike":
			veh2_crash = 1
		elif str.lower(veh2_crash) == "pedestrian":
			veh2_crash = 2
		elif str.lower(veh2_crash) == "car":
			veh2_crash = 3
		elif str.lower(veh2_crash) == "motorcycle":
			veh2_crash = 4
		elif str.lower(veh2_crash) == "unicycle":
			veh2_crash = 5
		elif str.lower(veh2_crash) == "skateboard":
			veh2_crash = 6
		else:
			veh2_crash = "Unusual input:" + veh2_crash
	else: 	
		veh2_crash = raw_input("What was the object?")
		if str.lower(veh2_crash) == "pedestrian" or str.lower(veh2_crash) == "person":
			veh2_crash = 2
		else:
			veh2_crash = "Object:" + veh2_crash
	return veh2_crash

#User enters date, time and place of crash
def date_time_place():
	date_crash = raw_input("What date did the crash occur? Enter as MM/DD/YYYY.")
	time_crash = raw_input("What time (approximately) did the crash occur? Enter as 00:00 using 24-hour/military time.")
	city_crash = raw_input("In what city did the crash occur?")
	return date_crash
	return time_crash
	return city_crash

#User enters information about injuries and police reporting
def other_conditions():
	weather = raw_input("Was it raining or snowing? If so, which?")
	if str.lower(weather) == "raining":
		weather = 1
	elif str.lower(weather) == "snowing":
		weather = 2
	else:
		weather = 0
	injury = raw_input
	if str.lower(injury) == "yes" or str.lower(injury) == "y":
		injury = True
	else:
		injury = False
	pol_rep = raw_input("Did you file a police report?")
	if str.lower(pol_rep) == "yes" or str.lower(pol_rep) == "y":
		pol_rep = True
	else:
		pol_rep = False
	return weather