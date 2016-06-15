#CrashSite Goals:
#Users will be able to report crashes and collisions and view the locations of other collisions
#Data will be able for download as a CSV file
#Map will auto-update, ideally on a set schedule, and show crashes that occurred during a set time period.
#Users will be able to report location through a map interface

from ReportClass import  *
from csv import *
from sys import *

#Welcome/Intro


def add_to_file():
	with open('BikeCrashDatabase.csv', 'wb', newline="") as csvfile:


if __name__ == '__main__':
	#Disclaimer
	print "Please note: This database is for informational use only. CrashSite does not file police reports on behalf of users."
	print "Enter information about the crash below:"
	ReportClass.types_of_vehicles()
	ReportClass.date_time_place()
	ReportClass.other_conditions()

	#Collect data

	#Associate date and time of entry with entry

	#Export to CSV
add_to_file()