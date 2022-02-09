# FileHeaders
A small script for quickly adding headers and footers to files in a folder.
 This script can take headers and footers either as command line arguments or from a file and apply these headers to files in a folder, using options this can exclude by file extension, detect that the header/footer is already there and skip the file, apply to file in a directory recursively, and dynamicaly add headers using tags for the file's name.
```
usage: FileHeaders.py [-h] [--header_file_help] [-r] [-w] [--disable_tags] [-o] [--remove_header] [--ignore_blacklist] [--ignore_whitelist] [-t TOP] [-b BOTTOM] [-d DIRECTORY] [-f HEADER_FILE] [-e EXTENSION]

A small utility to add headers and footers to files.

options:
  -h, --help            show this help message and exit
  --header_file_help    Display help for creating files to set the header/footer.
  -r, --recursive       Whether or not to scan for files recursively.
  -w, --whitespace      Whether or not to allow headers/footers only containing whitespace.
  --disable_tags        Whether or not to use tags found in a header/footer file.
  -o, --detect_header   Whether or not to scan for header/footers already in the file.
  --remove_header       Whether or not to remove existing header/footers from the file.
  --ignore_blacklist    Whether or not to ignore the blacklist found in the header/footer file.
  --ignore_whitelist    Whether or not to ignore the whitelist found in the header/footer file.
  -t TOP, --top TOP     Sets the header to be put at the top of the files.
  -b BOTTOM, --bottom BOTTOM
                        Sets the footer to be put at the bottom of the files.
  -d DIRECTORY, --directory DIRECTORY
                        Sets the directory of files to have headers/footers added.
  -f HEADER_FILE, --header_file HEADER_FILE
                        Uses a file to specify header/footer, see --header-file-help.
  -e EXTENSION, --extension EXTENSION
                        The extension for files to edit, by default edits all files.
```
```
To make a header/footer file you must include at least one header or footer block,
and no more than one each. You can make a header block by typing, on its own line
">>>HEADER_START<<<" and on its own line as well ">>>HEADER_END<<<", any text in
between these two line will be you header. For footer do the same but with
">>>FOOTER_START<<<" and ">>>FOOTER_END<<<".

You can make the headers change from file to file by adding tags, tags will insert
things like file name, folder name, or parameters passed in when you run the script.

You can also define a blacklist of paths to be excluded from any header/footer
addition or removals using the ">>>BLACKLIST_START<<<" and ">>>BLACKLIST_END<<<" to
start and end the list respectively.

Similarly you can use the ">>>WHITELIST_START<<<" and ">>>WHITELIST_END<<<" to start
and end a whitelist. Unless ignored by a flag, a whitelist makes it so that
this script will only edit those files, if it's not on the list, it wont be edited.
Because of the way this works you will need to use the path of the file that this
script will use, for this reason you may want to first run the script in the
desired location and copying all the files you want to whitelist when the script
lists them to confirm.

Tags:
      {FILE_NAME}: Inserts the name of the current file.
      {FOLDER_NAME}: Inserts the name of the current file's folder.
```
