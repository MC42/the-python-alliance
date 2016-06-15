import requests
import datetime
import sys

now = datetime.datetime.now()

#This whole project was based on some code by @gersteinj.
#Thanks for the initial code!

initials = 'TF'
github = "https://github.com/MC42/"
teamToHighlight = str("1257")  #Enter your own team here!

baseURL = 'http://www.thebluealliance.com/api/v2/'
header = {'X-TBA-App-Id': 'frc1257:thepythonalliance:beta'} #Yay, version strings....


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class tba:
	def get_team(self):
		team = input('Please enter a team:')
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
		if (team == teamToHighlight):
			print(bcolors.WARNING + 'You\'re looking at your own team.  Or you\'re debugging...' + bcolors.ENDC)
	

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
			print('Prease enter to continue')
			t = input('') #Just to hold the location until they hit enter.

	def get_all_team(self):
		page = input('Enter a page number please: ')
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

	def get_districts(self):
		myRequest = (baseURL + 'districts/' + str(now.year))
		response = requests.get(myRequest, headers=header)
		district_json = response.json()
		#print(district_json)
		print(bcolors.HEADER + 'FIRST Districts (' + str(now.year)+ bcolors.ENDC + ')')
		for districts in district_json:
			print(bcolors.OKGREEN + districts['key'].upper() + bcolors.ENDC +  '\t\t' + bcolors.OKBLUE + districts['name'] + bcolors.ENDC)


	def get_distrank(self):
		district=input('Please enter a district code (Hint, can be gotten with \'d\' command): ')		
		myRequest = (baseURL + 'district/' + district.lower() + '/' + str(now.year) + '/rankings')
		response = requests.get(myRequest, headers=header)
		district_json = response.json()
		#print(district_json)
		print(bcolors.HEADER +  district.upper() + ' District Rankings (' + str(now.year)+ bcolors.ENDC + ')')
		for districts in district_json:
			if ((districts['team_key'][3:]) == teamToHighlight): ## Whoops, easter egg?
				print(bcolors.OKBLUE + districts['team_key'].upper() + bcolors.ENDC + '\t\t' + bcolors.RED + str(districts['rank']) + bcolors.ENDC +  '\tPoints: ' + bcolors.WARNING + str(districts['point_total']) + bcolors.ENDC + '\tName: ' + bcolors.OKGREEN + tba.get_team_name(districts['team_key'][3:] ) + bcolors.ENDC)
			else:
				print(districts['team_key'].upper() + '\t\t' + bcolors.RED + str(districts['rank']) + bcolors.ENDC +  '\tPoints: ' + bcolors.WARNING + str(districts['point_total']) + bcolors.ENDC + '\tName: ' + bcolors.OKGREEN + tba.get_team_name(districts['team_key'][3:] ) + bcolors.ENDC)

	def get_team_name(self, team_no):
		
		myRequest = (baseURL + 'team/frc' + str(team_no))
		response = requests.get(myRequest, headers=header)
		jsonified = response.json()
		return jsonified['nickname']

	def get_rookie_year(self, team_no):

		myRequest = (baseURL + 'team/frc' + str(team_no))
		response = requests.get(myRequest, headers=header)
		jsonified = response.json()
		return jsonified['rookie_year']

print(bcolors.HEADER + 'The Blue Alliance (Python Edition)' + bcolors.ENDC)
print('Please enter a section of the site to load:')
print('\'e\' or \'events\' for a list of all events this season.')
print('\'t\' or \'team\' for a single team\'s information.')
print('\'a\' or \'all\' for a list of all teams. (by page number on TBA)')
print('\'d\' or \'district\' for a list of all current FIRST Districts & Codes')
print('\'dr\' or \'distrank\' for district rankings for a specific district.')

tba = tba()
command = input('')
command = command.split(' ')

if ((command[0] is 'e') or (command[0] == 'events')):
	tba.get_events(now.year)
elif ((command[0] is 't') or (command[0] == 'team')):
	tba.get_team()
elif ((command[0] is 'a') or (command[0] == 'all')):
	tba.get_all_team()
elif ((command[0] is 'd') or (command[0] == 'district')):
	tba.get_districts()
elif ((command[0] == 'dr') or (command[0] == 'dist')):
	tba.get_distrank()
else:
	print('Please enter a valid command.')

#That's all folks!

