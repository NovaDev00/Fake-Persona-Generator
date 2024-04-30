import argparse as parse

# Create an ArgumentParser object
parser = parse.ArgumentParser(description=" Generate a Fake Persona for SUCK PUPPET")

# Define optional arguments 
parser.add_argument('-v', '--version', help='tool version', action='store_true')
parser.add_argument('-c', '--commnads', help='show all commands', action='store_true') # if it's -c it will show commands, if it's -cc it will generate character (name, age ...)
parser.add_argument('-g', '--gender', help='choose the gender of your puppet', choices={'m', 'f', 'male', 'female'})
parser.add_argument('-n', '--number', help='number of puppets', type=int)
parser.add_argument('-a', '--all', help='generate all information', action='store_true')
parser.add_argument('-o', '--online', help='generate online information (email, username, password, etc)', action='store_true')
parser.add_argument('-b', '--bankinfo', help='generate bank information', action='store_true')


# Parse Arguments
args = parser.parse_args()




def main():
    if args.version: print('version')




# FakePersonaGen.py [gender] [number]