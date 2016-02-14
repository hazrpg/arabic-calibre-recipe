I'm new to releasing open-source code, so this is my attempt at a README file.

- README
	This document.

- LICENSE
	This is the full licence used for code include in this project.

- encode.py
	This is deprecated, since using # coding=utf-8 on the first line of the recipe
	allows you to write arabic characters. Make sure to start the string with a u e.g.

	u'بوابة الأهرام'

	I use this file to encode arabic characters into a unicode string so that
	calibre can work with it fine. Have a look at the recipe to see what I mean.
	
	To use, edit the file encode.txt and add the string you'd like to encode, and
	then run this script with:
	
	./encode.py
	
	or
	
	python encode.py

- encode.txt
	See encode.py, basically this is where you put the arabic string.
	Only use line 1, it will ignore other lines.

- ahram/
	A directory containing the ahram recipe and a few other scripts.

- ahram/test.sh
	This is the script to run a test build of the recipe (outputs as html).

- ahram/build.sh
	This is a script to build the recipe (outputs as mobi).

- ahram/al-ahram.recipe
	This is the main recipe for the Al-Ahram arabic news feed.
