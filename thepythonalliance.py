import requests
import sys

#This whole project was based on some code by @gersteinj.
#Thanks for the initial code!

initials = 'TF'
github = "https://github.com/MC42/"
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


baseURL = 'http://www.thebluealliance.com/api/v2/'
header = {'X-TBA-App-Id': 'frc1257:thepythonalliance:alpha'} #Yay, version strings....

class tba:
	def get_team(team):

		team = input('Enter team: ')
		myRequest = (baseURL + 'team/frc' + str(team))
		response = requests.get(myRequest, headers=header)
		jsonified = response.json()

		print(bcolors.HEADER + 'Team Information for FRC' + str(team)+ bcolors.ENDC)

		if jsonified['location'] != None:
			print('Team Nickname: \t'+ bcolors.OKGREEN + jsonified['nickname']+ bcolors.ENDC )
			print('Website: \t'+ bcolors.OKGREEN + jsonified['website']+ bcolors.ENDC )
			print('Team Full Name: '+ bcolors.OKGREEN + jsonified['name']+ bcolors.ENDC )
			print('Rookie Year: \t'+ bcolors.OKGREEN + str(jsonified['rookie_year'])+ bcolors.ENDC )
			print('\t' + bcolors.OKBLUE + 'Location Data:' + bcolors.ENDC)
			print('Locality: \t' + bcolors.OKGREEN + jsonified['locality']+ bcolors.ENDC )
			print('Location: \t' + bcolors.OKGREEN + jsonified['location']+ bcolors.ENDC )
			print('Country: \t' + bcolors.OKGREEN + jsonified['country_name']+ bcolors.ENDC )
		if jsonified['location'] == None:
			print('This team has since been dissolved.')
		sys.exit()

	def get_events(self,year):
		
		myRequest = (baseURL + 'events/' + str(year))
		response = requests.get(myRequest, headers=header)
		jsonified = response.json()

		print(bcolors.HEADER + 'All Events for the ' + str(year)+ ' Season' + bcolors.ENDC)
		#print(jsonified)
		for event in jsonified:
			print('Event Name:\t\t' + bcolors.OKGREEN + event['name'] + bcolors.ENDC)
			print('Event Code:\t\t' + bcolors.OKGREEN + event['event_code'].upper() + bcolors.ENDC)
			print('Official FIRST Event?\t' + bcolors.OKGREEN + str(event['official']) + bcolors.ENDC)
			if event['short_name'] != None:
				print('Simple Name:\t\t' + bcolors.OKGREEN + event['short_name'] + bcolors.ENDC)
			print('Location:\t\t' + bcolors.OKGREEN + event['location'] + bcolors.ENDC)
			print('End Date:\t\t' + bcolors.OKBLUE + event['end_date'] + bcolors.ENDC)
			print('Event Name:\t\t' + bcolors.OKGREEN + event['name'] + bcolors.ENDC)
			print('\t' + bcolors.BOLD + 'Alliances:' + bcolors.ENDC) #idk
			#print(event)
			t = raw_input('') #Just to hold the location until they hit enter.
		exit()




#team = input('Please enter the team number of an FRC team: ')

print(bcolors.HEADER + 'The Blue Alliance (Python Edition)' + bcolors.ENDC)
print('Please enter a section of the site to load:')
print('\'e\' or events for a list of all events this season.')
print('\'t\' or team for a single team\'s information.')
print('\'a\' or all for a list of all teams.')
print('\'d\' or district for district rankings.')

tba = tba()
command = raw_input('')
if command == 'e' or 'events':
	tba.get_events(2016)
elif command == 't' or 'team':
	tba.get_team(1257)
elif command == 'a' or 'all':
	tba.get_all_teams()
else:
	print('Please enter a valid command.')
#print(jsonified)

#for key in jsonified.keys():
#    print(key)
# print(jsonified['website'])


#print('Team Nickname: '+ jsonified['nickname'])

