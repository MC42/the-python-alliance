import requests
import datetime

now = datetime.datetime.now()

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
	def get_team(self):
		team = input('Enter team: ')
		myRequest = (baseURL + 'team/frc' + str(team))
		response = requests.get(myRequest, headers=header)
		jsonified = response.json()
		print(bcolors.HEADER + 'Team Information for FRC' + str(team)+ bcolors.ENDC)
		if jsonified['location'] != None:
			if jsonified['nickname'] != None:
				print('Team Nickname: \t'+ bcolors.OKGREEN + jsonified['nickname']+ bcolors.ENDC )
			if jsonified['name'] != None:
				print('Team Full Name: '+ bcolors.OKGREEN + jsonified['name']+ bcolors.ENDC )
			print('Team Number: \t' + bcolors.OKGREEN + str(jsonified['team_number']) + bcolors.ENDC )
			if jsonified['website'] != None:
				print('Website: \t'+ bcolors.OKGREEN + jsonified['website']+ bcolors.ENDC )
			print('Rookie Year: \t'+ bcolors.OKGREEN + str(jsonified['rookie_year'])+ bcolors.ENDC )
			print('\t' + bcolors.OKBLUE + 'Location Data:' + bcolors.ENDC)
			if jsonified['locality'] != None:
				print('Locality: \t' + bcolors.OKGREEN + jsonified['locality']+ bcolors.ENDC )
			if jsonified['location'] != None:
				print('Location: \t' + bcolors.OKGREEN + jsonified['location']+ bcolors.ENDC )
			if jsonified['country_name'] != None:
				print('Country: \t' + bcolors.OKGREEN + jsonified['country_name']+ bcolors.ENDC )
		if (jsonified['location'] == None) and (jsonified['website'] == None):
			print('\nThere is no information avalible for Team ' + bcolors.HEADER + str(team) + bcolors.ENDC + '\nThis team has likely since been dissolved.')
	

	def get_events(self, year):

		myRequest = (baseURL + 'events/' + str(year))
		response = requests.get(myRequest, headers=header)
		jsonified = response.json()

		print(bcolors.HEADER + bcolors.BOLD + bcolors.UNDERLINE + 'All Events for the ' + str(year)+ ' Season' + bcolors.ENDC)
		#print(jsonified)
		for event in jsonified:
			print('Event Name:\t\t' + bcolors.OKGREEN + event['name'] + bcolors.ENDC)
			print('Event Code:\t\t' + bcolors.BOLD + event['event_code'].upper() + bcolors.ENDC)
			if str(event['official']).upper() == 'FALSE':
				print('Official FIRST Event?\t' + bcolors.WARNING + str(event['official']) + bcolors.ENDC)
			elif str(event['official']).upper() == 'TRUE':
				print('Official FIRST Event?\t' + bcolors.OKGREEN + str(event['official']) + bcolors.ENDC)
			if event['short_name'] != None:
				print('Simple Name:\t\t' + bcolors.OKGREEN + event['short_name'] + bcolors.ENDC)
			print('Location:\t\t' + bcolors.OKGREEN + event['location'] + bcolors.ENDC)
			print('End Date:\t\t' + bcolors.OKBLUE + event['end_date'] + bcolors.ENDC)
			print('Event Name:\t\t' + bcolors.OKGREEN + event['name'] + bcolors.ENDC)
			if event['alliances'] != []:		
				print('\t' + bcolors.BOLD + 'Alliances:' + bcolors.ENDC) #idk
			for alli in event['alliances']:
				print('')
				for picks in alli['picks']:
					print(picks.upper())
			print('--------------------------')
			t = raw_input('') #Just to hold the location until they hit enter.

	def get_all_team(self, page):
		myRequest = (baseURL + 'teams/' + str(page))
		response = requests.get(myRequest, headers=header)
		jsonified = response.json()
		print(bcolors.HEADER + 'Team Information : Page ' + str(page)+ bcolors.ENDC)
		for team in jsonified:
			#print(team) #BEDUG
			print(bcolors.HEADER + 'Team Information for FRC' + str(team['team_number'])+ bcolors.ENDC)
			if team['location'] != None:
				if team['nickname'] != None:
					print('Team Nickname: \t'+ bcolors.OKGREEN + team['nickname']+ bcolors.ENDC )
				if team['name'] != None:
					print('Team Full Name: '+ bcolors.OKGREEN + team['name']+ bcolors.ENDC )
				print('Team Number: \t' + bcolors.OKGREEN + str(team['team_number']) + bcolors.ENDC )
				if team['website'] != None:
					print('Website: \t'+ bcolors.OKGREEN + team['website']+ bcolors.ENDC )
				print('Rookie Year: \t'+ bcolors.OKGREEN + str(team['rookie_year'])+ bcolors.ENDC )
				print('\t' + bcolors.OKBLUE + 'Location Data:' + bcolors.ENDC)
				if team['locality'] != None:
					print('Locality: \t' + bcolors.OKGREEN + team['locality']+ bcolors.ENDC )
				if team['location'] != None:
					print('Location: \t' + bcolors.OKGREEN + team['location']+ bcolors.ENDC )
				if team['country_name'] != None:
					print('Country: \t' + bcolors.OKGREEN + team['country_name']+ bcolors.ENDC )
			print('\n--------------------------\n')
			if (team['location'] == None) and (team['website'] == None):
				print('\nThere is no information avalible for Team ' + bcolors.HEADER + str(team['team_number']) + bcolors.ENDC + '\nThis team has likely since been dissolved.')


		

#team = input('Please enter the team number of an FRC team: ')

print(bcolors.HEADER + 'The Blue Alliance (Python Edition)' + bcolors.ENDC)
print('Please enter a section of the site to load:')
print('\'e\' or \'events\' for a list of all events this season.')
print('\'t\' or \'team\' for a single team\'s information.')
print('\'a\' or \'all\' for a list of all teams. (by page number on TBA)')

tba = tba()
command = raw_input('')
if ((command is 'e') or (command is 'events')):
	tba.get_events(now.year)

elif ((command is 't') or (command is 'team')):
	tba.get_team()

elif ((command is 'a') or (command is 'all')):
	global_page = input('Enter page number: ')
	tba.get_all_team(global_page)
else:
	print('Please enter a valid command.')

#That's all folks!

