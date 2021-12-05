# FileHeaders
A small script for quickly adding headers and footers to files in a folder.
 This script can take headers and footers either as command line arguments or from a file and apply these headers to files in a folder, using options this can exclude by file extension, detect that the header/footer is already there and skip the file, apply to file in a directory recursively, and dynamicaly add headers using tags for the file's name.
```
usage: FileHeaders.py [-h] [--header_file_help] [-r] [-w] [--disable_tags] [-o] [-t TOP] [-b BOTTOM] [-d DIRECTORY] [-f HEADER_FILE] [-e EXTENSION]

A small utility to add headers and footers to files.

options:
  -h, --help            show this help message and exit
  --header_file_help    Display help for creating files to set the header/footer.
  -r, --recursive       Whether or not to scan for files recursively.
  -w, --whitespace      Whether or not to allow headers/footers only containing whitespace.
  --disable_tags        Whether or not to use tags found in a header/footer file.
  -o, --detect_header   Whether or not to scan for header/footers already in the file.
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

Tags:
    {FILE_NAME}: Inserts the name of the current file.
```
