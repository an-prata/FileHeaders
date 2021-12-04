# (c) Evan Overman (https://github.com/an-prata)
# FileHeaders (https://github.com/an-prata/FileHeaders)
# Licensed under 

import os
import sys
import argparse
import fileinput

HEADER_START_TAG 	= '>>>HEADER_START<<<'
HEADER_END_TAG 		= '>>>HEADER_END<<<'
FOOTER_START_TAG 	= '>>>FOOTER_START<<<'
FOOTER_END_TAG 		= '>>>FOOTER_END<<<'

NO_HEADER_OR_FOOTER_MESSAGE = 'No header nor footer given form either command line arguments or file.'

NO_HEADER_OR_FOOTER 	= 0
HAS_HEADER 				= 1
HAS_FOOTER 				= 2
HAS_HEADER_AND_FOOTER 	= 4

def print_header_file_help():
	print(f'''
		  To make a header/footer file you must include at least one header or footer block, 
		  and no more than one each. You can make a header block by typing, on its own line 
		  "{HEADER_START_TAG}" and on its own line as well "{HEADER_END_TAG}", any text in 
		  between these two line will be you header. For footer do the same but with 
		  "{FOOTER_START_TAG}" and "{FOOTER_END_TAG}".

		  You can make the headers change from file to file by adding tags, tags will insert
		  things like file name, folder name, or parameters passed in when you run the script.
		  ''' + '''
		  Tags:
		  \t{FILE_NAME}: Inserts the name of the current file.
		  \t{FOLDER_NAME}: Inserts the name of the folder, particularly useful when using recursion.
		  ''')

parser = argparse.ArgumentParser(description = 'A small utility to add headers and footers to files.')

parser.add_argument('--header_file_help',		action = 'store_true',							help = 'Display help for creating files to set the header/footer.')

parser.add_argument('-r',	'--recursive',		action = 'store_true',							help = 'Whether or not to scan for files recursively.')
parser.add_argument('-w',	'--whitespace',		action = 'store_true', 							help = 'Whether or not to allow headers/footers only containing whitespace.')
parser.add_argument('-t',	'--top',			type = str, 				default = '',		help = 'Sets the header to be put at the top of the files.')
parser.add_argument('-b',	'--bottom',			type = str,					default = '',		help = 'Sets the footer to be put at the bottom of the files.')
parser.add_argument('-d',	'--directory',		type = str, 				default = './',		help = 'Sets the directory of files to have headers/footers added.')
parser.add_argument('-f',	'--header_file',	type = str,					default = '',		help = 'Uses a file to specify header/footer, see --header-file-help.')
parser.add_argument('-e',	'--extensions',		type = set[str],			default = {''},		help = 'A list of extensions for files to edit, by default edits all files.')

args = parser.parse_args()

if args.header_file_help:
	print_header_file_help()
	sys.exit()

file_extensions		= args.extensions
dir					= args.directory
header_file			= args.header_file
header				= args.top
footer				= args.bottom
dir_contents 		= {''}
files 				= {''}
paths 				= {''}
has_header_footer 	= -1

if args.recursive:
	for current_directory, directories, current_files in os.walk(dir):
		for file in current_files:
			paths.add(os.path.join(current_directory, file))
			files.add(file)
else:
	for file in os.scandir(dir):
		paths.add(file.name)
		files.add(file.name)

# Gets all files ending in any of the given extensions and adds them to files
for extension in file_extensions:
	for entry in dir_contents:
		if entry[len(entry) - len(extension):] == extension:
			files.add(entry)

dir_contents.remove('')
paths.remove('')
files.remove('')

if header_file != '':
	try:
		current_file = open(header_file, 'r')
	except FileNotFoundError:
		print(f'file {header_file} not found.')
		sys.exit()

	content = current_file.read()

	# if no header/footer block is present we set has_header_footer accordingly using constants,
	try:
		header = content[content.index(HEADER_START_TAG) + len(HEADER_START_TAG) + 1 : content.index(HEADER_END_TAG) - 1]
	except ValueError:
		has_header_footer = HAS_FOOTER
	
	try:
		footer = content[content.index(FOOTER_START_TAG) + len(FOOTER_START_TAG) + 1: content.index(FOOTER_END_TAG) - 1]
	except ValueError:
		if has_header_footer == HAS_FOOTER:
			has_header_footer = NO_HEADER_OR_FOOTER
			print(NO_HEADER_OR_FOOTER_MESSAGE)
			sys.exit()
		else:
			has_header_footer = HAS_HEADER

	# has_header_footer will equal -1 if it has not been set by any of the statements above
	# and if it has not been set in an except block then it must have both a header and footer
	if has_header_footer == -1:
		has_header_footer = HAS_HEADER_AND_FOOTER

# check if the user is allowing whitespace only headers/footer
# and if not setting has_header_footer to not include the 
# header/footer if it is whitespace
if not args.whitespace:
	if header.isspace():
		header = ''
		has_header_footer = HAS_FOOTER
	if footer.isspace():
		footer = ''
		if has_header_footer == HAS_FOOTER:
			has_header_footer = NO_HEADER_OR_FOOTER
			print(NO_HEADER_OR_FOOTER_MESSAGE)
			sys.exit()
		else:
			has_header_footer = HAS_HEADER

# if no header or footer is given, exit
if header == '' and footer == '':
	print(NO_HEADER_OR_FOOTER_MESSAGE)
	sys.exit()

# display and check with the user that their header/footer is correct
if has_header_footer == HAS_HEADER_AND_FOOTER:
	print(f'HEADER:\n{header}')
	print(f'FOOTER:\n{footer}')

elif has_header_footer == HAS_HEADER:
	print(f'HEADER:\n{header}')
	print('FOOTER:\nNo footer given.')

elif has_header_footer == HAS_FOOTER:
	print('HEADER:\nNo header given.')
	print(f'FOOTER\n{footer}')

print('Is this correct? [Y/n]: ')

if header != '':
	header += '\n'
if footer != '':
	footer = '\n' + footer

if input().lower() != 'y':
	sys.exit()

if files.__contains__(sys.argv[0]):
	files.remove(sys.argv[0]) # prevents this file from editing itself

if files.__contains__(header_file):
	files.remove(header_file) # prevents this file from editing the header file

if paths.__contains__(sys.argv[0]):
	paths.remove(sys.argv[0]) # prevents this file from editing itself

if paths.__contains__(header_file):
	paths.remove(header_file) # prevents this file from editing the header file

if paths.__contains__(os.path.join(dir, sys.argv[0])):
	paths.remove(os.path.join(dir, sys.argv[0])) # prevents this file from editing itself

if paths.__contains__(os.path.join(dir, header_file)):
	paths.remove(os.path.join(dir, header_file)) # prevents this file from editing the header file


if args.recursive:
	for file_path in paths:
		try: 
			current_file = open(file_path, 'r+', encoding = 'utf-8', errors='ignore')
		except PermissionError: 
			print(f'Insufficiant permission to edit {file_path}')
			continue

		content = current_file.read()
	
		if header == '':
			current_file.seek(0)
			current_file.write(content + footer)
			current_file.truncate()
		elif footer == '':
			current_file.seek(0)
			current_file.write(header + content)
			current_file.truncate()
		else:
			current_file.seek(0)
			current_file.write(header + content + footer)
			current_file.truncate()
		current_file.close()

else:
	for file_path in files:
		try: 
			current_file = open(file_path, 'r+', encoding = 'utf-8', errors='ignore')
		except PermissionError: 
			print(f'Insufficiant permission to edit {file_path}')
			continue

		content = current_file.read()
	
		if header == '':
			current_file.seek(0)
			current_file.write(content + footer)
			current_file.truncate()
		elif footer == '':
			current_file.seek(0)
			current_file.write(header + content)
			current_file.truncate()
		else:
			current_file.seek(0)
			current_file.write(header + content + footer)
			current_file.truncate()
		current_file.close()