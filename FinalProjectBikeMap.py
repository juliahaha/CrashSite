#CrashCLE Goals:
#Users will be able to report crashes and collisions and view the locations of other collisions
#Data will be able for download as a CSV and shapefile
#Map will auto-update, ideally on a set schedule, and show crashes that occurred during a set time period.
#Users will be able to report location through a map interface

date_crash = None
time_crash = None
city_crash = None
crash_type = None
veh1_crash = None
veh2_crash = None
crash_obj = None
other_cond = None
injury = None
pol_rep = None

#Welcome/Intro


#Disclaimer
print ("Please note: This database is for informational use only. CrashSite does not file police reports on behalf of users.")
print ("Enter information about the crash below:")

#Collect
def types_of_vehicles(veh1_crash,veh2_crash):
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
	else veh1_crash = "Unusual input:" + veh1_crash
	veh2_crash = raw_input("Was the crash with another vehicle or an object?")
	return veh1_crash
	if str.lower(veh2_crash) == "vehicle" or str.lower(veh2_crash) == "another vehicle":
		veh2_crash = raw_input("What kind of vehicle?")
		if 
		elif str.lower(veh2_crash) == "bicycle" or str.lower(veh2_crash) == "bike":
			veh2_crash = 1
		elif str.lower(veh2_crash) == "pedestrian":
			veh2_crash = 2
		elif str.lower(veh2_crash) == "car":
		elif str.lower(veh2_crash) == "motorcycle":
		elif str.lower(veh2_crash) == "unicycle":
		else veh2_crash = "Unusual input:" + veh2_crash
	else 	
		veh2_crash = raw_input("What was the object?")
		if str.lower(veh2_crash) == "pedestrian" or str.lower(veh2_crash) == "person":
			veh2_crash = 2
		else veh2_crash = "Object:" + veh2_crash
	return veh2_crash
#User enters date, time and place of crash
def date_time_place(date_crash,time_crash,city_crash)

#User enters information about injuries and police reporting

#Assign user entries a unique ID number
#Associate date and time of entry with entry