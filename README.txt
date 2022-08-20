Language: Python
exe created using Pyinstaller
Author: Shahzeb Azhar

***********************************************************************************************
***********************************************************************************************

This exe is used to create timetables using the excel file provided by FAST NUCES. NOTE: The program is in BETA phase, please report any errors you encounter with said program.

Hard Requirements:-
-> pref.txt
--- This file stores your courses and other information necessary for timetable generation. Proper guidelines on how to write your own pref.txt will be given below.
-> colors.txt
--- The timetable is divided into 3 different colors and 2 different text colors. Those color codes(in hexadecimal) are written in colors.txt, information on how to create your own colors.txt will be given below.
-> Google Chrome
--- Needed for a library that is converting the tabular form of created timetable into an image(Html2Image). If anyone knows any other library that does this without any external requirements, do let me know.
-> timetable.xlsx
--- The timetable provided by FAST NUCES.

***********************************************************************************************
***********************************************************************************************

Guidelines:-

1) Download the timetable provided by FAST NUCES, rename it to "timetable" and paste it in the same directory as the given file "Timetable Generator"
2) Place colors.txt and pref.txt in the same file. Sample colors.txt and pref.txt is already given.
3) Run the file "Timetable Generator" and wait for it to execute completely, the file will generate an image called "ttable"
4) Open and confirm the image(due to the BETA nature of program, I cannot confirm if it will work 100% of the times hence please do recheck).

***********************************************************************************************
***********************************************************************************************

Guidelines to create pref.txt:-

1) Mention your degree in the first line(format: BDS, BCS, BSE, MDS, MCS etc. Please follow this format or check in the timetable given by FAST NUCES as to what format they follow, your degree will be listed in the second row, ignore the batch year).
2) Mention your courses, NOTE: do not copy and paste the course names from the courselist, as the course names in the courselist and the timetable are not the same. Paste the courses after finding them from the timetable. Cannot do anything about this, a problem of consistency in FAST.
3) Course should be mentioned in the following format: COURSE NAME - SECTION(including the semester. eg. 4A) - degree(only needed if you are taking a course in a degree other than the one mentioned above).
4) Example course: Database Systems - 4A
-- Or: Differential Equations - 2L - BCS
5) Kindly keep the sample provided to have a reference of how to create pref.txt
6) Save and run the program "Timetable generator"

***********************************************************************************************
***********************************************************************************************

Guidelines to create colors.txt:

1) All the colors need to be in hexadecimal format, as follows: #XXXXXX where X is a hexadecimal number from 0-F
2) 5 colors are provided, ORDER MATTERS(this will be made easier in further implementations).
Line 1: heading text color(color used for days and times).
Line 2: rest text color(color used to write courses in).
Line 3: background color(background color for the courses).
Line 4: Time color(background color of the top row, the place where times are listed).
Line 5: Day color(background color of the first column, place where days are listed).

***********************************************************************************************
***********************************************************************************************

PS: Program is in BETA state. Kindly recheck the timetable after generating and report any and all errors to the author to avoid any issues in the future. 