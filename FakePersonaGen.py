import argparse as parse
from prettytable import PrettyTable 
import random
import textStyle


#inisialize
color = textStyle.TextColor

# Declare Variables
version='0.1.0'
commands="-v --version : tool version\n-c --commands : show all commands\n-g --gender : choose puppet gender\n-cc --character : generate just character info(name, age, birthday, etc)\n-n --number : number of the puppets\n-a --all : generate all info\n-o --online : generate online info (email, username, password, IPV4, mac adress, etc)\n-b --bankinfo : generate bank information"
name = surename = mothername = rgender = age = birthday = zodiac  = nationality = geo_coordinates = statue = accupation = company = salary = major = mastercard = expired = cvc2 = username = email = phone = password = ipv4 = mac_adress = eye_color = hair = height = weight = bloodtype = fav_color = fav_food = fav_drink = fav_film = fav_sport = fav_music = hobies = interestes = viechle = None 

# Create an ArgumentParser object
parser = parse.ArgumentParser(description=" Generate a Fake Persona for SUCK PUPPET")

# Define optional arguments 
parser.add_argument('-v', '--version', help='tool version', action='store_true')
parser.add_argument('-c', '--commands', help='show all commands', action='count') # if it's -c it will show commands, if it's -cc it will generate character (name, age ...)
parser.add_argument('-g', '--gender', help='choose the gender of your puppet', choices={'m', 'f', 'r', 'male', 'female','random'}, default='random')
parser.add_argument('-n', '--number', help='number of puppets', type=int, default=1)
parser.add_argument('--nationality', help='choose the puppet\'s nationality', choices={'american', 'russian'}, default='american')
parser.add_argument('-a', '--all', help='generate all information', action='store_true')
parser.add_argument('-o', '--online', help='generate online information (email, username, password, IPV4, mac adress, etc)', action='store_true')
parser.add_argument('-b', '--bankinfo', help='generate bank information', action='store_true')


# Parse Arguments
args = parser.parse_args()

# Generating Functions
# name
def name_gen(gender = 3): # generate puppet name
	global rgender
	global name 
	global surename 
	global mothername
	global nationality

	male_name = ['Alexander', 'Dax', 'Victor', 'Jordan', 'Colt', 'Frank', 'Sawyer', 'Nolan', 'Ridge', 'Carter', 'Donald', 'Anthony', 'Ryan', 'Hunter', 'Travis', 'Sebastian', 'Beau', 'Peter', 'Omar', 'Owen', 'Miguel', 'James', 'Grant', 'Parker', 'Oscar', 'Harry', 'Nash', 'Caleb', 'Christopher', 'Paxton', 'Emmett', 'Brooks', 'Garrett', 'Blake', 'Xavier', 'Samuel', 'Philip', 'Jason', 'Kevin', 'Liam', 'Mark', 'Theodore', 'Remington', 'Nathaniel', 'River', 'Miles', 'Ezekiel', 'Corey', 'Max', 'Vincent', 'Carl', 'Preston', 'Craig', 'Luke', 'Michael', 'David', 'Jackson', 'Derek', 'Dominic', 'Jake', 'Hudson', 'Timothy', 'Keegan', 'Mason', 'Calvin', 'Steven', 'Ian', 'Richard', 'Wyatt', 'Adrian', 'Todd', 'Ronald', 'Neil', 'Oliver', 'Walter', 'Julian', 'Colin', 'Ford', 'Orion', 'Kai', 'Gabriel', 'Emerson', 'Gregory', 'Francis', 'Elliot', 'Harrison', 'Warren', 'Knox', 'Leonard', 'Martin', 'Lincoln', 'Jessie', 'Gary', 'Cameron', 'Thomas', 'Sam', 'Gavin', 'Alex', 'Wesley', 'Isaac', 'Aiden', 'Fernando', 'Zachary', 'Keith', 'Rhett', 'Trevor', 'Joshua', 'Robert', 'Roger', 'Ethan', 'Matt', 'Graham', 'Mitchell', 'Boris', 'Paul', 'Monroe', 'Alan', 'Matthew', 'Marcus', 'George', 'Phil', 'Everett', 'Declan', 'Beckett', 'Joe', 'Wilder', 'Elijah', 'Logan', 'Brent', 'Earl', 'Jonathan', 'Cash', 'Kenneth', 'Ellis', 'Jesse', 'Henry', 'William', 'Lucas', 'Stephen', 'Maverick', 'Jace', 'Gordon', 'Deacon', 'Dylan', 'Tim', 'Isaiah', 'Harold', 'Archer', 'Adam', 'Nicholas', 'Taylor', 'Stewart', 'Landon', 'Devin', 'Rafael', 'Dan', 'Joseph', 'Sean', 'Grayson', 'Brandon', 'Simon', 'Bronson', 'Jeremy', 'Brian', 'Evan', 'Jared', 'Jack', 'Cody', 'Fletcher', 'Ricky', 'Weston', 'Kingsley', 'Raymond', 'Piers', 'Edward', 'Joel', 'Zane', 'Noah', 'Phoenix', 'Charles', 'Bradley', 'Eric', 'Marshall', 'Finley', 'Seth', 'John', 'Nathan', 'Quentin', 'Patrick', 'Shawn', 'Kyle', 'Sullivan', 'Rowan', 'Finn', 'Asher', 'Benjamin', 'Connor', 'Justin', 'Daniel', 'Andrew', 'Christian', 'Jacob', 'Tyler', 'Thatcher', 'Austin', 'Jasper', 'Silas']	
	female_name = ['Victoria', 'Carol', 'Sophie', 'Elizabeth', 'Maria', 'Paisley', 'Sutton', 'Sue', 'Dakota', 'Lillian', 'Felicity', 'Madison', 'Anna', 'Stephanie', 'Megan', 'Emily', 'Emery', 'Rose', 'Cassandra', 'Courtney', 'Leah', 'Arden', 'Remi', 'Daisy', 'Alexandra', 'Mary', 'Angela', 'Caitlin', 'Nancy', 'Nicola', 'Nicole', 'Lisa', 'Pippa', 'Finley', 'Denise', 'Rachel', 'Bethany', 'Katherine', 'Aria', 'Sarah', 'Diana', 'Cora', 'Kayla', 'Ava', 'Laura', 'Donna', 'Zadie', 'Emma', 'Sandra', 'Jennifer', 'Juniper', 'Carolyn', 'Cecilia', 'Wendy', 'Bryn', 'Jasmine', 'Ruth', 'Diane', 'Kennedy', 'Christina', 'Grace', 'Everly', 'Briar', 'Carla', 'Riley', 'Blair', 'Clementine', 'Deborah', 'Deirdre', 'Irene', 'Addison', 'Cheyenne', 'Theresa', 'Jamie', 'Cynthia', 'Jessica', 'Sofia', 'Vanessa', 'Barbara', 'Christine', 'Charlotte', 'Danielle', 'Zoe', 'Luna', 'Wren', 'Susan', 'Isabella', 'Amelia', 'Stella', 'Joan', 'Olivia', 'Gabrielle', 'Natalie', 'Harlow', 'Dana', 'Karen', 'Linda', 'Lily', 'Abigail', 'Michelle', 'Julia', 'Alice', 'Amy', 'Sally', 'Haley', 'Hannah', 'Jane', 'Andrea', 'Sadie', 'Samantha', 'Joanne', 'Ashley', 'Madeleine', 'Angelina', 'Aurora', 'Yvonne', 'Nova', 'Lauren', 'Camille', 'Faith', 'Alison', 'Virginia', 'Jenna', 'Delaney', 'Penelope', 'Anne', 'Ella', 'Sloane', 'Allison', 'Bella', 'Caroline', 'Heather', 'Kimberly', 'Betty', 'Fiona', 'Brittany', 'Sonia', 'Claire', 'Bernadette', 'Margaret', 'Lennox', 'Alexis', 'Rebecca', 'Audrey', 'Brianna', 'Una', 'Oakley', 'Brenda', 'Ainsley', 'Jan', 'Zoey', 'Kinsley', 'Kylie', 'Avery', 'Wanda', 'Melanie', 'Tracey', 'Colleen', 'Patricia', 'Melissa', 'Quinn', 'Molly', 'Amanda', 'Crystal', 'Dorothy', 'Catherine', 'Chloe']

	sure_names_list = ['Hill', 'Slater', 'Welch', 'Smith', 'Wilson', 'Grant', 'Jackson', 'Short', 'Hughes', 'Scott', 'Hudson', 'MacDonald', 'Davidson', 'Blake', 'Randall', 'Wright', 'McDonald', 'Bell', 'Walker', 'Peake', 'Hunter', 'Hodges', 'Bailey', 'Mills', 'Paige', 'North', 'Sutherland', 'Fraser', 'Jones', 'Harris', 'Churchill', 'Thomson', 'Paterson', 'Murray', 'Springer', 'Allan', 'Baker', 'Lyman', 'Ellison', 'Butler', 'Young', 'Greene', 'Poole', 'Morrison', 'Bond', 'James', 'Miller', 'Skinner', 'Watson', 'Glover', 'Johnston', 'White', 'Berry', 'Terry', 'Powell', 'Sharp', 'Dyer', 'Fisher', 'Gray', 'Knox', 'Vaughan', 'Rees', 'Lewis', 'Russell', 'Langdon', 'Brown', 'Anderson', 'Arnold', 'McGrath', 'Sanderson', 'Turner', 'Simpson', 'Nash', 'Hardacre', 'Dowd', 'Ferguson', 'Mathis', 'Manning', 'Edmunds', 'Duncan', 'Alsop', 'King', 'Robertson', 'Campbell', 'Quinn', 'Graham', 'Parsons', 'Pullman', 'Hamilton', 'Martin', 'Mackay', 'Hemmings', 'May', 'Mitchell', 'Oliver', 'Kelly', 'Lee', 'Ball', 'Clark', 'Morgan', 'Payne', 'Abraham', 'Newman', 'MacLeod', 'Clarkson', 'Coleman', 'Peters', 'Metcalfe', 'Wilkins', 'Howard', 'Vance', 'Avery', 'Cornish', 'Underwood', 'Ross', 'Bower', 'Davies', 'McLean', 'Stewart', 'Wallace', 'Chapman', 'Hart', 'Burgess', 'Ince', 'Gibson', 'Carr', 'Lambert', 'Mackenzie', 'Rutherford', 'Dickens', 'Walsh', 'Roberts', 'Forsyth', 'Reid', 'Piper', 'Lawrence', 'Cameron', 'Nolan', 'Marshall', 'Black', 'Buckland', 'Gill', 'Ogden', 'Taylor', 'Tucker', 'Parr', 'Rampling', 'Henderson', 'Kerr' ]
	surename=sure_names_list[random.randint(0, len(sure_names_list)-1)]

	nationality='American'
	if gender == 'm' or gender == 'male':  #genarate male name
		rgender = 'male'
		name = male_name[random.randint(0,len(male_name)-1)]
	elif gender == 'f' or gender == 'female': #generate female name
		rgender = 'female'
		name = female_name[random.randint(0,len(female_name)-1)]
	elif gender == 'r' or gender == 'random': #generate
		var=random.randint(0,1)
		if var == 1: #generate random name
			rgender = 'male'
			name = male_name[random.randint(0,len(male_name)-1)]
		else:
			rgender = 'female'
			name = female_name[random.randint(0,len(female_name)-1)]
		
	# generate nother name
	mothername = female_name[random.randint(0,len(female_name)-1)]
	while name == mothername:
		mothername = female_name[random.randint(0,len(female_name)-1)]


def age():
	#TODO: get age --age : and calculate and generate the birthday
	#TODO: generate a random age and birthday
 
	
	pass

# email
def email():
	global username
	global password
	email = ['gmail', 'yahoo', 'yandex', 'outlook', 'hotmail', 'protonmail']
	extention = ['html', 'ru', 'com']
	return str(name).lower() + '.' + str(surename).lower() + '@' + (email[random.randint(0, len(email)-1)]) + '.' + (extention[random.randint(0, len(extention)-1)])


# Optional functions
def charinfo(): # character information
	print(f"{color.red}# Character information{color.end}")
	table = PrettyTable([f"{color.soft_blue}NAME", "SURENAME", "MOTHER NAME", f"NATIONALITY{color.end}"])

	for i in range(args.number):
		name_gen(args.gender)
		table.add_row([name, surename, mothername, nationality])
	print(table)
	table.clear()
	
def onlineinfo(): # online information
	print(f"{color.red}\n# Online information{color.end}")
	table = PrettyTable([f"{color.soft_blue}EMAIL","USERNAME", f"PASSWORD{color.end}"])

	for i in range(args.number):
		table.add_row([f"{name}123@gmail.com", f"{name}21", "passwd5641$$$"])
	print(table)

# main
def main():
	# excute functions
	name_gen(args.gender)
	
	if args.version: print(version)                         #show the tool version
	if args.commands == 1: print(commands)                  #checking for -c
	elif args.commands == 2: print('character')
	if args.bankinfo:
		
		pass

	if args.all:   #show all data

		# CHARACTER INFORMATION
		charinfo()
		onlineinfo()

		# name generator
	if args.online: print('online')
	if args.bankinfo: print('bankinfo')
	if args.number: print()

	# print data

	# data created successfully
	print(f'{color.green}\n\n[+] Data created successfully!\n{color.end}')

#banner
def banner():
	print(f"""{color.pink}
    _____     _        ____                                  ____            
   |  ___|_ _| | _____|  _ \ ___ _ __ ___  ___  _ __   __ _ / ___| ___ _ __  
   | |_ / _` | |/ / _ \ |_) / _ \ '__/ __|/ _ \| '_ \ / _` | |  _ / _ \ '_ \ 
   |  _| (_| |   <  __/  __/  __/ |  \__ \ (_) | | | | (_| | |_| |  __/ | | |
   |_|  \__,_|_|\_\___|_|   \___|_|  |___/\___/|_| |_|\__,_|\____|\___|_| |_|{color.end}
                                                                                
________________________________{color.pink}by @ArturDev00{color.end}________________________________    
_____________________this man will die, but not his ideas_____________________                

""")
# FakePersonaGen.py [gender] [number]

# start program
if __name__ == '__main__':
	banner()
	main()



