# (c) Evan Overman (https://github.com/an-prata)
# FileHeaders (https://github.com/an-prata/FileHeaders)
# Licensed under 

import os
import sys
import argparse
import fileinput

HEADER_START_TAG = '>>>HEADER_START<<<'
HEADER_END_TAG = '>>>HEADER_END<<<'
FOOTER_START_TAG = '>>>FOOTER_START<<<'
FOOTER_END_TAG = '>>>FOOTER_END<<<'

def print_header_file_help():
	print(f'''
		  To make a header/footer file you must include at least one header or footer block, 
		  and no more than one each. You can make a header block by typing, on its own line 
		  "{HEADER_START_TAG}" and on its own line as well "{HEADER_END_TAG}", any text in 
		  between these two line will be you header. For footer do the same but with 
		  "{FOOTER_START_TAG}" and "{FOOTER_END_TAG}"
		  ''')

parser = argparse.ArgumentParser(description = 'A small utility to add headers and footers to files.')

parser.add_argument('--header_file_help',		action = 'store_true',							help = 'Display help for creating files to set the header/footer.')

parser.add_argument('-r',	'--recursive',		action = 'store_true',							help = 'Whether or not to scan for files recursively.')
parser.add_argument('-t',	'--top',			type = str, 				default = '',		help = 'Sets the header to be put at the top of the files.')
parser.add_argument('-b',	'--bottom',			type = str,					default = '',		help = 'Sets the footer to be put at the bottom of the files.')
parser.add_argument('-d',	'--directory',		type = str, 				default = './',		help = 'Sets the directory of files to have headers/footers added.')
parser.add_argument('-f',	'--header_file',	type = str,					default = '',		help = 'Uses a file to specify header/footer, see --header-file-help.')
parser.add_argument('-e',	'--extensions',		type = set[str],			default = {''},		help = 'A list of extensions for files to edit, by default edits all files.')

args = parser.parse_args()

if args.header_file_help:
	print_header_file_help()
	sys.exit()

file_extensions	= args.extensions
dir				= args.directory
header_file		= args.header_file
header			= args.top
footer			= args.bottom
dir_contents 	= {''}
files 			= {''}

#dir = "Z:/Users/evan/Developer/Boba/Boba.PasswordManager"
#file_extensions = {'.cs', '.cpp'}

with os.scandir(dir) as dir_iter:
	for entry in dir_iter:
		dir_contents.add(entry.name)

# Gets all files ending in any of the given extensions and adds them to files
for extension in file_extensions:
	for entry in dir_contents:
		if entry[len(entry) - len(extension):] == extension:
			files.add(entry)

dir_contents.remove('')
files.remove('')

if header_file != '':
	current_file = open(header_file, 'r')
	content = current_file.read()
	header = content[content.find(HEADER_START_TAG) + len(HEADER_START_TAG) + 1 : content.find(HEADER_END_TAG) - 1]
	footer = content[content.find(FOOTER_START_TAG) + len(FOOTER_START_TAG) + 1: content.find(FOOTER_END_TAG) - 1]
	
print(f'Header:\n {header}')
print(f'Footer:\n {footer}')
print('Is this correct? [Y/n]: ')

if input().lower() != 'y':
	sys.exit()

if header == '' and footer == '':
	print('No header nor footer given form either command line arguments or file.')
	sys.exit()

if files.__contains__(sys.argv[0]):
	files.remove(sys.argv[0]) # prevents this file from editing itself

if files.__contains__(header_file):
	files.remove(header_file) # prevents this file from editing the header file

for file in files:
	try: 
		current_file = open(file, 'r+')
	except PermissionError: 
		print(f'Insufficiant permission to edit {file}')
		continue
  
	if header == '':
		current_file.write(			current_file.read() + footer)
	elif footer == '':
		current_file.write(header + current_file.read()			)
	else:
		current_file.write(header + current_file.read() + footer)
	current_file.close()