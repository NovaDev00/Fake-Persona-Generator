import argparse as parse
from prettytable import PrettyTable 
import random
import textStyle
import datetime


#inisialize
color = textStyle.TextColor

# Declare Variables
version='0.1.2'
commands=f"{color.light_blue}-v --version {color.end}: tool version\n{color.light_blue}-h2 --how2use {color.end}: show some examples\n{color.light_blue}-a --all {color.end}: generate all info\n{color.light_blue}-g --gender {color.end}: choose puppet gender (-g female or -g male), Default is random\n{color.light_blue}-c --character {color.end}: generate just character info(name, age, birthday, etc)\n{color.light_blue}-n --number {color.end}: number of the puppets (-n 3)\n{color.light_blue}-o --online {color.end}: generate online info (email, username, password, IPV4, mac adress, etc) (in developpment)\n{color.light_blue}-b --bankinfo {color.end}: generate bank information (coming soon)\n{color.light_blue}--birthday {color.end}: generate a birthday information (age, year, month, day, zodiac, etc)"
how_to_use=f"{color.light_blue}Generate all info: {color.end}{color.yellow}py FakePersonaGen.py -a{color.end}\n{color.light_blue}Generate multi info: {color.end}{color.yellow}py FakePersonaGen.py -a -n 10 {color.end} \n{color.light_blue}Generate 5 info of male only: {color.end}{color.yellow}py FakePersonaGen.py -a -n 5 -g male{color.end}\n"
name = surename = mothername = rgender = age = birthday = zodiac  = nationality = geo_coordinates = statue = accupation = company = salary = major = mastercard = expired = cvc2 = username = email = phone = password = ipv4 = mac_adress = eye_color = hair = height = weight = bloodtype = fav_color = fav_food = fav_drink = fav_film = fav_sport = fav_music = hobies = interestes = viechle = None 
names_array = []
surenames_array = []

# Create an ArgumentParser object
parser = parse.ArgumentParser(description=" Generate a Fake Persona for SUCK PUPPET")

# Define optional arguments 
parser.add_argument('-v', '--version', help='tool version', action='store_true')
parser.add_argument('-h2', '--how2use', help='show some examples', action='store_true')
parser.add_argument('-c', '--character', help='generate just character info(name, age, birthday, etc)', action='store_true')
parser.add_argument('-g', '--gender', help='choose the gender of your puppet', choices={'m', 'f', 'r', 'male', 'female','random'}, default='random')
parser.add_argument('-n', '--number', help='number of puppets (ex: py FakePersonaGen.py -a -n 3)', type=int, default=1)
parser.add_argument('--nationality', help='choose the puppet\'s nationality', choices={'american', 'russian'}, default='american')
parser.add_argument('-a', '--all', help='generate all information', action='store_true')
parser.add_argument('-o', '--online', help='generate online information (email, username, password, IPV4, mac adress, etc)', action='store_true')
parser.add_argument('-b', '--bankinfo', help='generate bank information', action='store_true')
parser.add_argument('--birthday', help='generate (birthday, age, zodiac, etc ..', action='store_true')
parser.add_argument('-l', '--location', help='generate random location', choices={'russia', 'usa','random'}, default='random')

# Parse Arguments
args = parser.parse_args()

### Generating Functions ###
# name
def name_gen(gender = 'r'): # generate puppet name
	global rgender
	global name 
	global surename 
	global mothername
	global nationality

	male_name = ['Taylor', 'Tyrone', 'Frank', 'Johnny', 'Oscar', 'Geoffrey', 'Jeffery', 'Eddie', 'Craig', 'Kristopher', 'Bruce', 'Martin', 'Gregg', 'Kirk', 'Julian', 'Parker', 'Theodore', 'Brooks', 'Danny', 'Fred', 'Willie', 'James', 'Boris', 'Tony', 'Harry', 'Weston', 'Casey', 'Christopher', 'Perry', 'Miles', 'Lance', 'Luis', 'Brad', 'Ronald', 'Dean', 'Devin', 'Thomas', 'Devon', 'Albert', 'Darius', 'Garrett', 'Knox', 'Ricardo', 'Tommy', 'Brendan', 'Terrance', 'Louis', 'Stephen', 'George', 'Daniel', 'Keegan', 'Jose', 'Andres', 'Sebastian', 'Cody', 'Chad', 'Ridge', 'Ethan', 'Sullivan', 'Benjamin', 'Calvin', 'Darryl', 'Bronson', 'Zane', 'Mitchell', 'Chris', 'Jackson', 'Javier', 'Hudson', 'Monroe', 'Brandon', 'Pedro', 'Justin', 'Curtis', 'Jesus', 'Vincent', 'Peter', 'Colin', 'Dennis', 'Marc', 'Tyler', 'Phil', 'Carter', 'Jon', 'Karl', 'Ezekiel', 'Stewart', 'Roy', 'Jonathon', 'Sean', 'Carlos', 'Dan', 'Bradley', 'Bryan', 'Robert', 'Brian', 'Dale', 'Jessie', 'Colton', 'Orion', 'Beckett', 'Archer', 'Mario', 'Richard', 'Hunter', 'Mike', 'Max', 'Brett', 'Carl', 'Guy', 'Gordon', 'Micheal', 'Neil', 'Randall', 'Darren', 'Francis', 'Phillip', 'Jimmy', 'Norman', 'Eduardo', 'Beau', 'Marshall', 'Ford', 'Glenn', 'Charles', 'Manuel', 'Gerald', 'Larry', 'Donald', 'Jake', 'Lucas', 'Warren', 'Travis', 'Kenneth', 'Joseph', 'Cory', 'Dave', 'Reginald', 'Gary', 'Colt', 'Nicholas', 'Allen', 'Dillon', 'Mark', 'Wesley', 'Fletcher', 'Riley', 'Patrick', 'Xavier', 'Miguel', 'Clayton', 'Caleb', 'Kingsley', 'Walter', 'Connor', 'Jerry', 'Andrew', 'Victor', 'Alejandro', 'Joel', 'Kurt', 'Adam', 'Nolan', 'John', 'Joshua', 'Cash', 'Lawrence', 'Jim', 'Thatcher', 'Darrell', 'Eugene', 'Eric', 'Harrison', 'Emerson', 'Rowan', 'Lincoln', 'Raymond', 'Leonard', 'Asher', 'Piers', 'Jeremy', 'Sawyer', 'Russell', 'Leon', 'Greg', 'Ray', 'Jordan', 'Derrick', 'Stanley', 'Ellis', 'Edgar', 'Evan', 'William', 'Paxton', 'Ricky', 'Roger', 'Owen', 'Billy', 'Duane', 'Harold', 'Scott', 'Sergio', 'Declan', 'Corey', 'Grant', 'Aiden', 'Trevor', 'David', 'Jacob', 'Nathan', 'Gavin', 'Keith', 'Timothy', 'Marvin', 'Adrian', 'Ernest', 'Henry', 'Drew', 'Dominic', 'Ross', 'Logan', 'Rodney', 'Austin', 'Noah', 'Philip', 'Deacon', 'Alex', 'Rickey', 'Elliot', 'Erik', 'Everett', 'Kevin', 'Fernando', 'Jonathan', 'Vernon', 'Antonio', 'Mason', 'Isaiah', 'Alexander', 'Jared', 'Kent', 'Spencer', 'Phoenix', 'Cameron', 'Gregory', 'Shaun', 'Aaron', 'Steve', 'Graham', 'Derek', 'Edward', 'Bryce', 'Marcus', 'Matthew', 'Chase', 'Wyatt', 'Preston', 'Dylan', 'Gabriel', 'Landon', 'Earl', 'Jace', 'Jack', 'Bob', 'Emmett', 'Ruben', 'Luke', 'Clinton', 'Silas', 'Elijah', 'Jeremiah', 'Samuel', 'Ryan', 'Michael', 'Ralph', 'Johnathan', 'Shane', 'Terry', 'Christian', 'Melvin', 'Tim', 'Steven', 'Jorge', 'Jerome', 'Blake', 'Roberto', 'Alan', 'Jason', 'Andre', 'Jamie', 'Remington', 'River', 'Grayson', 'Maverick', 'Juan', 'Brent', 'Liam', 'Sam', 'Jeff', 'Edwin', 'Francisco', 'Malik', 'Randy', 'Nathaniel', 'Bernard', 'Kelly', 'Tracy', 'Shawn', 'Gilbert', 'Ronnie', 'Paul', 'Bobby', 'Matt', 'Kai', 'Tristan', 'Hector', 'Wilder', 'Dakota', 'Kyle', 'Dustin', 'Finley', 'Dax', 'Simon', 'Ian', 'Arthur', 'Frederick', 'Douglas', 'Omar', 'Joe', 'Rick', 'Anthony', 'Todd', 'Seth', 'Quentin', 'Finn', 'Zachary', 'Jesse', 'Jay', 'Jeffrey', 'Daryl', 'Rafael', 'Jasper', 'Isaac', 'Rhett', 'Wayne', 'Nicolas', 'Jermaine', 'Troy', 'Dalton', 'Dwayne', 'Oliver', 'Nash', 'Jaime', 'Lee']	
	female_name = ['Remi', 'Lisa', 'Lacey', 'Amelia', 'Juniper', 'Tammy', 'Shelby', 'Lynn', 'Deborah', 'Gina', 'Joanna', 'Bella', 'Traci', 'Kristy', 'Karina', 'Kimberly', 'Camille', 'Bethany', 'Margaret', 'Tiffany', 'Destiny', 'Yolanda', 'Meredith', 'Marissa', 'Kathryn', 'Norma', 'Olivia', 'Sylvia', 'Madison', 'Kristi', 'Cora', 'Summer', 'Alicia', 'Alice', 'Alexandra', 'Una', 'Kristina', 'Brenda', 'Leah', 'Dorothy', 'Adriana', 'Karen', 'Tracy', 'Caitlyn', 'Shelia', 'Suzanne', 'Jasmin', 'Tracey', 'Terri', 'Sara', 'Holly', 'Anne', 'Debbie', 'Cassidy', 'Marilyn', 'Anna', 'Rita', 'Jennifer', 'Elaine', 'Katelyn', 'Evelyn', 'Adrienne', 'Deanna', 'Sabrina', 'Sheryl', 'Brittney', 'Katrina', 'Miranda', 'Jordan', 'Terry', 'Sherry', 'Zoey', 'Hayley', 'Sonya', 'Everly', 'Bernadette', 'Bridget', 'Leslie', 'Jessica', 'Felicity', 'Susan', 'Sydney', 'Hannah', 'Sally', 'Mariah', 'Priscilla', 'Carol', 'Cathy', 'Barbara', 'Shari', 'Katherine', 'Julia', 'Lily', 'Natasha', 'Brittany', 'Cassandra', 'Samantha', 'Molly', 'Shirley', 'Janice', 'Shelly', 'Marie', 'Alexa', 'Angie', 'Sonia', 'Sherri', 'Misty', 'Jamie', 'Carrie', 'Janet', 'Tonya', 'Rachel', 'Alejandra', 'Stacie', 'Chelsea', 'Nicole', 'Sierra', 'Lindsay', 'Judy', 'Jodi', 'Donna', 'Ana', 'Renee', 'Paisley', 'Rose', 'Cynthia', 'Rebekah', 'Tami', 'Kendra', 'Robyn', 'Joanne', 'Ella', 'Erika', 'Latoya', 'Theresa', 'Julie', 'Nicola', 'Mindy', 'Yvette', 'Darlene', 'Natalie', 'Gail', 'Gloria', 'Brandi', 'Angelica', 'Emma', 'Kathy', 'Kelly', 'Ainsley', 'Martha', 'Bailey', 'Madeline', 'Audrey', 'Gabrielle', 'Ashley', 'Claire', 'Yesenia', 'Briana', 'Chelsey', 'Kim', 'Linda', 'Joann', 'Zoe', 'Heidi', 'Valerie', 'Joan', 'Michaela', 'Caitlin', 'Veronica', 'Brianna', 'Carolyn', 'Jean', 'Regina', 'Joyce', 'Jaime', 'Alison', 'Michelle', 'Daisy', 'Maria', 'Andrea', 'Isabella', 'Sharon', 'Heather', 'Nova', 'Mckenzie', 'Nichole', 'Courtney', 'Tara', 'Delaney', 'Lauren', 'Toni', 'Erica', 'Bryn', 'Rebecca', 'Kaitlyn', 'Aria', 'Avery', 'Melissa', 'Dana', 'Eileen', 'Lindsey', 'Oakley', 'Melanie', 'Erin', 'Kaitlin', 'Dawn', 'Christina', 'Caroline', 'Hailey', 'Dominique', 'Peggy', 'Diana', 'Tabitha', 'Sadie', 'Christie', 'Jeanne', 'Dakota', 'Sophia', 'Angelina', 'Virginia', 'Frances', 'Jenna', 'Alexis', 'Lillian', 'Paige', 'Harlow', 'Haley', 'Allison', 'Penelope', 'Vicki', 'Luna', 'Ariana', 'Lydia', 'Annette', 'Christine', 'Jenny', 'Kylie', 'Casey', 'Connie', 'Pippa', 'Felicia', 'Rachael', 'Sloane', 'Carla', 'Sarah', 'Kristine', 'Yvonne', 'Sandra', 'Pamela', 'Monique', 'Sue', 'Maureen', 'Bonnie', 'Quinn', 'Fiona', 'Kristie', 'Katie', 'Brandy', 'Sophie', 'Kayla', 'Kiara', 'Irene', 'Jill', 'Amber', 'Catherine', 'Deirdre', 'Morgan', 'Stella', 'Anita', 'Ava', 'Riley', 'Vickie', 'Grace', 'Meghan', 'Patricia', 'Kennedy', 'Blair', 'Debra', 'Shannon', 'Charlene', 'Laurie', 'Ann', 'Christy', 'Alexandria', 'April', 'Alisha', 'Clementine', 'Tanya', 'Mercedes', 'Krystal', 'Paula', 'Cheyenne', 'Brooke', 'Victoria', 'Penny', 'Melinda', 'Angel', 'Kelsey', 'Laura', 'Sofia', 'Wendy', 'Jacqueline', 'Vanessa', 'Breanna', 'Cheryl', 'Nancy', 'Betty', 'Taylor', 'Sandy', 'Briar', 'Chloe', 'Crystal', 'Loretta', 'Sheena', 'Jane', 'Savannah', 'Kristin', 'Whitney', 'Jan', 'Kathleen', 'Stacey', 'Ashlee', 'Sheila', 'Sheri', 'Cindy', 'Colleen', 'Beverly', 'Kelli', 'Elizabeth', 'Kari', 'Denise', 'Ellen', 'Aurora', 'Claudia', 'Karla', 'Tina', 'Amy', 'Carmen', 'Stacy', 'Cecilia', 'Rhonda', 'Addison', 'Isabel', 'Faith', 'Jasmine', 'Diane', 'Desiree', 'Emery', 'Wanda', 'Mackenzie', 'Finley', 'Abigail', 'Gwendolyn', 'Kinsley', 'Phyllis', 'Robin', 'Arden', 'Danielle', 'Carly', 'Madeleine', 'Alyssa', 'Amanda', 'Lori', 'Bianca', 'Meagan', 'Charlotte', 'Michele', 'Emily', 'Stephanie', 'Sutton', 'Lennox', 'Ruth', 'Angela', 'Zadie', 'Megan', 'Beth', 'Monica', 'Teresa', 'Wren', 'Mary', 'Kristen']

	sure_names_list = ['Mcgrath', 'Horn', 'Cruz', 'Hill', 'Watts', 'Kaufman', 'Sharp', 'Barnett', 'Wilson', 'Turner', 'Hayes', 'Farrell', 'Brandt', 'Baldwin', 'Vargas', 'Smith', 'Combs', 'Vincent', 'Scott', 'Gibson', 'Hendrix', 'Mercer', 'Stafford', 'Logan', 'Spence', 'Clarkson', 'Fields', 'Mills', 'Jennings', 'Frazier', 'Jefferson', 'Kelley', 'Shelton', 'Weaver', 'Leon', 'Morales', 'Hodges', 'Koch', 'Pena', 'Cuevas', 'Monroe', 'Guzman', 'Lowe', 'Wilkinson', 'Donaldson', 'Fletcher', 'Trujillo', 'Payne', 'Chase', 'Rhodes', 'Porter', 'Ward', 'Rice', 'Charles', 'Morgan', 'Hensley', 'Peake', 'Gray', 'Doyle', 'Colon', 'Preston', 'Snyder', 'Mathews', 'Frye', 'Williams', 'Peterson', 'Deleon', 'Harrison', 'Hayden', 'Mata', 'Mullins', 'Wagner', 'Gregory', 'Pope', 'Mendoza', 'Bowen', 'Dougherty', 'Richards', 'Santana', 'Ramos', 'Carrillo', 'Ferrell', 'Reed', 'Galloway', 'Elliott', 'Parker', 'Alsop', 'Hood', 'Rubio', 'Morrow', 'Avila', 'Hudson', 'Byrd', 'Lin', 'White', 'Cunningham', 'Gilbert', 'Chaney', 'Church', 'Sutton', 'Patrick', 'Stephenson', 'Shah', 'Villa', 'Kennedy', 'Parsons', 'Alvarez', 'Hansen', 'Stone', 'Hamilton', 'Blackwell', 'Zavala', 'Cortez', 'Davidson', 'Shea', 'Whitehead', 'Bush', 'Arias', 'Irwin', 'Myers', 'Powers', 'Hobbs', 'Flynn', 'Ogden', 'Hines', 'Guerra', 'Larson', 'Hanson', 'Haynes', 'Allen', 'Salas', 'Woods', 'Levy', 'Oneal', 'Ramirez', 'Sutherland', 'Roman', 'Adkins', 'Ayala', 'Zimmerman', 'Benson', 'Griffith', 'Mackenzie', 'Gutierrez', 'Piper', 'Holden', 'Kemp', 'Bradshaw', 'Rivers', 'Casey', 'Murillo', 'Gibbs', 'Durham', 'Horne', 'Marshall', 'King', 'Garrison', 'Parrish', 'Vang', 'Gallagher', 'Marquez', 'Matthews', 'Cameron', 'Robinson', 'Glover', 'Ruiz', 'Jacobs', 'Nash', 'Lopez', 'Flores', 'Salazar', 'Wilcox', 'Ford', 'Montgomery', 'Dunlap', 'Werner', 'Berry', 'Calhoun', 'Ali', 'Hernandez', 'Coleman', 'Steele', 'Crawford', 'Ross', 'Young', 'Austin', 'Mcintyre', 'Mack', 'Wood', 'Hemmings', 'Powell', 'Kramer', 'Foster', 'Drake', 'Vasquez', 'Churchill', 'Diaz', 'Schultz', 'Torres', 'Madden', 'Mackay', 'Hardin', 'Strickland', 'Holloway', 'Soto', 'Watkins', 'Fernandez', 'Olsen', 'Kelly', 'Velasquez', 'Lawrence', 'Rivera', 'George', 'Cooper', 'Bryan', 'Garner', 'Olson', 'Melendez', 'Perkins', 'Lee', 'Gill', 'Terry', 'Orozco', 'Gay', 'Curtis', 'Greene', 'Petersen', 'Leach', 'Crosby', 'Franklin', 'Hughes', 'Newman', 'Dawson', 'Berg', 'Wright', 'Patterson', 'Short', 'Costa', 'Walters', 'Norton', 'Glass', 'Dominguez', 'Mccall', 'Moran', 'McGrath', 'Robbins', 'Campbell', 'Abraham', 'Zamora', 'Thomson', 'Burke', 'Alvarado', 'Richmond', 'Walsh', 'Reeves', 'Ellis', 'Richardson', 'Fraser', 'Barrera', 'Hicks', 'Burns', 'Chapman', 'Griffin', 'Vance', 'Cowan', 'Juarez', 'Burton', 'Ramsey', 'Garza', 'Mclean', 'Walker', 'Douglas', 'Hammond', 'Pierce', 'Keith', 'Collins', 'Wade', 'Castillo', 'Kline', 'Reyes', 'Roberson', 'Huff', 'Mullen', 'Carroll', 'Roberts', 'Luna', 'Winters', 'Warren', 'Ball', 'Kirby', 'Peters', 'Moody', 'Davies', 'Gilmore', 'Oliver', 'Mann', 'Garcia', 'Cummings', 'Cross', 'Mccoy', 'Cook', 'Blankenship', 'Dyer', 'Waters', 'Nicholson', 'Singh', 'Rivas', 'Solis', 'Carlson', 'Tate', 'Simpson', 'Farmer', 'Stewart', 'Jordan', 'Armstrong', 'Estrada', 'Duffy', 'Lowery', 'Bartlett', 'Compton', 'Hunt', 'Hutchinson', 'Bell', 'Wells', 'Bower', 'Chambers', 'Mercado', 'Martin', 'Taylor', 'Odonnell', 'Simmons', 'Robles', 'Archer', 'Todd', 'Wheeler', 'Wolfe', 'Black', 'Ray', 'Morton', 'Barton', 'James', 'Banks', 'Curry', 'Yoder', 'North', 'Buckland', 'Buchanan', 'Sanchez', 'Weber', 'Murray', 'Edmunds', 'Rutherford', 'Foley', 'Orr', 'Meadows', 'Meyers', 'Morris', 'Swanson', 'Hoover', 'Dean', 'Jimenez', 'Key', 'Gross', 'Mora', 'Harris', 'Bruce', 'Norris', 'Krueger', 'Rosario', 'Acosta', 'Grant', 'Rose', 'Thompson', 'Nolan', 'Skinner', 'May', 'Mays', 'Cisneros', 'Mitchell', 'Nunez', 'Mcpherson', 'Schaefer', 'Little', 'Jackson', 'Clark', 'Stevenson', 'Graves', 'Langdon', 'Gamble', 'Aguilar', 'Sullivan', 'Ho', 'Rasmussen', 'Morrison', 'Barajas', 'Paul', 'Nguyen', 'Hardacre', 'Cohen', 'Robertson', 'Cornish', 'Park', 'Nichols', 'Keller', 'Mcdonald', 'Holmes', 'Jones', 'Donovan', 'Yates', 'Henry', 'Webster', 'Cole', 'Mcguire', 'Ponce', 'Rogers', 'Nixon', 'Gonzalez', 'Jarvis', 'Sherman', 'Webb', 'Cox', 'Summers', 'Boone', 'Russell', 'Contreras', 'Parks', 'Chandler', 'Collier', 'Saunders', 'Rios', 'Springer', 'Perry', 'Schroeder', 'Medina', 'Tanner', 'Gardner', 'Hull', 'Mccarthy', 'Whitaker', 'Poole', 'Stark', 'Hopkins', 'Lamb', 'Reid', 'Rodriguez', 'Sweeney', 'Hunter', 'Buck', 'Gallegos', 'Erickson', 'Rollins', 'Arnold', 'Li', 'Newton', 'Le', 'Edwards', 'Gomez', 'Maldonado', 'Lewis', 'Cobb', 'Harper', 'Metcalfe', 'McLean', 'Patel', 'Wise', 'Paterson', 'Trevino', 'Duke', 'Butler', 'Martinez', 'Knox', 'Schmidt', 'Mathis', 'Graham', 'Woodward', 'Friedman', 'Whitney', 'Marsh', 'Bradford', 'Beltran', 'Sanderson', 'Liu', 'Stokes', 'Sosa', 'Zuniga', 'Sexton', 'Klein', 'Rush', 'Snow', 'Conner', 'Lyman', 'Watson', 'Noble', 'Lawson', 'Sandoval', 'Johnson', 'Johns', 'Brown', 'Wang', 'Perez', 'Russo', 'MacDonald', 'Bond', 'Mayo', 'Chen', 'Joseph', 'Goodman', 'Dudley', 'Mcconnell', 'Shepherd', 'Avery', 'Blake', 'Solomon', 'Dickens', 'Schwartz', 'Romero', 'Valencia', 'Brooks', 'Huber', 'Navarro', 'Frederick', 'Bass', 'Santiago', 'Floyd', 'Fisher', 'Tucker', 'Hays', 'Brock', 'Lambert', 'Palmer', 'Ritter', 'Arellano', 'Sampson', 'Kirk', 'Green', 'Pacheco', 'Howard', 'Yang', 'Wong', 'Baird', 'Cantu', 'Freeman', 'Tyler', 'Hebert', 'Small', 'Schneider', 'Roth', 'Allan', 'Espinoza', 'Hartman', 'Hodge', 'Thomas', 'Welch', 'Fuller', 'Salinas', 'Camacho', 'Duncan', 'Rojas', 'Rosales', 'Dowd', 'Weiss', 'Gentry', 'Kane', 'Dunn', 'Esparza', 'Haney', 'Barker', 'Moss', 'Richard', 'Choi', 'Bauer', 'Cantrell', 'Lane', 'West', 'Manning', 'Parr', 'Cabrera', 'Forsyth', 'Jacobson', 'Moore', 'Murphy', 'Riley', 'Bowers', 'Page', 'Garrett', 'Fischer', 'Willis', 'Rangel', 'Hoffman', 'Bailey', 'Boyd', 'Reynolds', 'Hale', 'Bentley', 'Rees', 'Moreno', 'Barnes', 'Hart', 'Obrien', 'Benjamin', 'Baxter', 'Mccormick', 'Fleming', 'Valenzuela', 'Anderson', 'Adams', 'Chang', 'Tran', 'Roach', 'MacLeod', 'Miles', 'Lara', 'McDonald', 'Harding', 'Daniels', 'Arroyo', 'Conley', 'Lang', 'Hall', 'Jensen', 'Huffman', 'Malone', 'Carey', 'Rampling', 'Pugh', 'Anthony', 'Spears', 'Paige', 'Pitts', 'Stevens', 'Mckinney', 'Stanton', 'Silva', 'Melton', 'Fox', 'Long', 'Lutz', 'Houston', 'Owens', 'Townsend', 'Cain', 'Brady', 'York', 'Clay', 'Gates', 'Mcdowell', 'Villanueva', 'Ortega', 'Finley', 'Woodard', 'Copeland', 'Pittman', 'Andrews', 'Pham', 'Ryan', 'Ince', 'Chavez', 'Lloyd', 'Weeks', 'Miller', 'Christensen', 'Sellers', 'Grimes', 'Pullman', 'Kim', 'Estes', 'Henderson', 'Landry', 'Baker', 'Washington', 'Mendez', 'Acevedo', 'Vazquez', 'Sparks', 'Fowler', 'Price', 'Holt', 'Wall', 'Stephens', 'Slater', 'Herrera', 'Fry', 'Santos', 'Zhang', 'Fitzgerald', 'Pennington', 'Evans', 'Mcbride', 'Becker', 'Vaughan', 'Mcdaniel', 'Oconnor', 'Beck', 'Mueller', 'Valdez', 'Delgado', 'Lucas', 'Williamson', 'Calderon', 'Phillips', 'Burgess', 'Hawkins', 'Underwood', 'Carter', 'Mcmahon', 'Best', 'Kerr', 'Jenkins', 'Pearson', 'Atkinson', 'Wallace', 'Caldwell', 'Bennett', 'Lynch', 'Sanders', 'Ferguson', 'Nelson', 'Carr', 'Dodson', 'Mckee', 'Wiggins', 'Lyons', 'Randall', 'Ellison', 'Leonard', 'Chan', 'Davis', 'Lindsey', 'Francis', 'Osborne', 'Bradley', 'Hampton', 'Meyer', 'Harmon', 'Munoz', 'Wilkins', 'Quinn', 'Johnston', 'Goodwin']
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
	today = datetime.date.today()
	#TODO: get age --age : and calculate and generate the birthday
	#TODO: generate a random age and birthday
	months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
	
	print(f"{color.red}\n# Birthday information{color.end}")
	table = PrettyTable([f"{color.soft_blue}Age", "Birthday Year", "Month", "Day", f"Zodiac{color.end}"])

	for i in range(args.number):
		year = random.randint(1980, today.year -14)
		month_randint = random.randint(1, len(months))
		month = months[month_randint]
		day = random.randint(1, 28)
		age = today.year - year - ((today.month, today.day) <= (month_randint, day))
		table.add_row([age, year, month, day, 'comming'])

	print(table)
 

# email
def email(): # generate an email address

	email = ['gmail', 'yahoo', 'yandex', 'outlook', 'hotmail', 'protonmail']
	extention = ['ru', 'com']
	return str(name).lower() + '.' + str(surename).lower() + '@' + (email[random.randint(0, len(email)-1)]) + '.' + (extention[random.randint(0, len(extention)-1)])

# password
def passwd(): # generate a random password
	password = "\0"
	allchars = [['*', '_', '\\', '/', '$', '%', '&', '~', '!', '#', '<', '>'], 
			   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
			   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
			   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]	
	
	for i in range(12):
		row = random.randint(0, len(allchars) - 1)
		password += str(allchars[row][random.randint(0, len(allchars[row]) - 1)])
	#return
	return password

# locations
def location_gen():
	russian_location_gen()
# russian locations
def russian_location_gen():
	russian_locations_data = {
		"Moscow Oblast" : {
			"Moscow" : [
				"Arbat Street", "Tverskaya Street", "Pyatnitskaya Street", "Myasnitskaya Street", "Bolshaya Nikitskaya Street", "Novy Arbat Street",
				"Bolshaya Dmitrovka Street", "Kuznetsky Most", "Lubyanka Street", "Altuf'yevskoye Shosse", "Altufyevskoye Highway", "Leninsky Prospekt"
			],
			"Balashikha" : [
				"67 Prospekt Lenina", "6 Polevoy Proyezd", "Zheleznodorozhny", "13 Severnyy Proyezd", "13 Severnyy Proyezd", "31 Ulitsa Zarechnaya", "43 Ulitsa Sverdlova"
			],
			"Podolsk" : [
				"Lenina Street", "Oktyabrskaya Street", "Kirova Street", "Sovetskaya Street", "Pervomayskaya Street"
			],
			"Khimki" : [
				"Babakina Street", "Ulitsa Druzhby", "Leningradskaya Street", "Pobedy Street", "Geroyev Panfilovtsev Street"
			],
			"Korolev" : [
				"Lenina Street", "Gagarina Street", "Korolyova Avenue", "Kalinina Street", "Tsiolkovskogo Street"
			],
			"Mytishchi" : [
				"Yaroslavl Highway", "Pionerskaya Street", "1st Institutskaya Street", "Mira Street", "Kommunisticheskaya Street"
			],
			"Zheleznodorozhny" : [
				"9 Ulitsa Oktyabr'skaya", "Ulitsa Nekrasova"
			]
		},
		"Republic of Bashkortostan" : {
			"Ufa" : [
				"Oktyabrya Avenue", "Lenina Street", "Chernyshevskogo Street", "Zaki Validi Street", "Kirova Street", "Gogolya Street", "Karl Marx Street", "Dostoyevskogo Street", "Revolyutsionnaya Street", "Mendeleyeva Street", "Prospekt Salavata Yulayeva", "Kommunisticheskaya Street", "Pushkina Street", "Bakunina Street", "Pervomayskaya Street", "Kosmonavtov Street"
			],
			"Sterlitamak" : [
				"Oktyabrya Avenue", "Kommunisticheskaya Street", "Mira Street", "Artyoma Street", "Khalturina Street", "Gagarin Boulevard", "Druzhby Street", "Golovanova Street"
			], 
			"Salavat" : [
				"Oktyabrya Street", "Lenina Street", "Kalinina Street", "Pervomayskaya Street", "Gagarin Street", "Molodyozhnaya Street", "Bikbulatova Street"
			], 
			"Neftekamsk" : [
				"Lenina Avenue", "Komsomolskaya Street", "Yubileynaya Street", "Stroitelykh Street", "Mira Street", "Energetikov Street", "Traktovaya Street"
			],
			"Oktyabrsky" : [
				"Lenina Avenue", "Devonskaya Street", "Komsomolskaya Street", "Pushkina Street", "Gagarina Street", "Chapayeva Street", "Stroitelnaya Street"
			]
		}	
	}
	
	# make a table
	print(f"{color.red}\n#Location data{color.end}")
	table = PrettyTable([f"{color.soft_blue}Federal subject", "City", f"Street{color.end}"])

	# Generate random russian location
	for i in range(args.number):
		# Random Federal Subject
		Federal_subjects = list(russian_locations_data.keys())
		selected_subject = random.choice(Federal_subjects)

		# Random Citi in subject
		cities_in_subject = russian_locations_data[selected_subject]
		cities_names = list(cities_in_subject.keys())
		selected_city = random.choice(cities_names)

		# Random Street in city
		street_in_city = cities_in_subject[selected_city]
		selected_street = random.choice(street_in_city)

		# add a table row information
		table.add_row([selected_subject, selected_city, selected_street])

	print(table)
	table.clear()


# Optional functions

# character information
def charinfo():
	print(f"{color.red}# Character information{color.end}")
	table = PrettyTable([f"{color.soft_blue}NAME", "SURENAME", "MOTHER NAME", "GENDER", f"NATIONALITY{color.end}"])
	names_array.clear()

	for i in range(args.number):
		name_gen(args.gender)
		names_array.insert(i-1, name)
		surenames_array.insert(i-1, surename)
		table.add_row([name, surename, mothername, rgender, nationality])
	print(table)
	table.clear()
	
# online information
def onlineinfo(): 
	global name, surename
	print(f"{color.red}\n# Online information{color.end}")
	table = PrettyTable([f"{color.soft_blue}EMAIL","USERNAME",f"PASSWORD{color.end}"])

	for i in range(args.number):
		name = names_array[i]
		surename = surenames_array[i]
		table.add_row([email(), f"{name}{random.randint(100,999)}", passwd()])
	print(table)
	names_array.clear()

# main
def main():
	# excute functions
	name_gen(args.gender)
	passwd()
	
	# show help 
	print(f"{color.red}# Commands\n{color.end}{commands}\n")
	# loading 
	if args.number >= 100000:
		print(f'{color.green}\n[+] Loading... \n{color.end}')
	#
	if args.character:	charinfo()
	if args.bankinfo:	pass			#bank information
	if args.online: onlineinfo()
	if args.bankinfo: print('bankinfo')
	if args.birthday: age()
	if args.how2use: print(f"{color.red}# How to use\n{color.end}{how_to_use}")

	#TODO: advice to get a good sock puppet (web sites and others)  -aa --advice
	if args.all:   #show all data

		# CHARACTER INFORMATION
		charinfo()
		age()
		onlineinfo()
		location_gen()

	# data created successfully
	print(f'{color.green}\n\n[+] Data created successfully!\n{color.end}')

#banner
def banner():
	print(f"""{color.pink}
    _____     _        ____                                  ____            
   |  ___|_ _| | _____|  _ \\ ___ _ __ ___  ___  _ __   __ _ / ___| ___ _ __  
   | |_ / _` | |/ / _ \\ |_) / _ \\ '__/ __|/ _ \\| '_ \\ / _` | |  _ / _ \\ '_ \\ 
   |  _| (_| |   <  __/  __/  __/ |  \\__ \\ (_) | | | | (_| | |_| |  __/ | | |
   |_|  \\__,_|_|\\_\\___|_|   \\___|_|  |___/\\___/|_| |_|\\__,_|\\____|\\___|_| |_|{color.end}
                                                                                
________________________________{color.pink}by @NovaCode00{color.end}________________________________    
_____________________this man will die, but not his ideas_____________________                

""")
# FakePersonaGen.py [gender] [number]

# start program
if __name__ == '__main__':
	if args.version: print(f"Fake Persona Generator VERSION : {version} v")              #show the tool version
	else: 
		banner() 
		main()



