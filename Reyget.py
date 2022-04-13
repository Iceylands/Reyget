#Made by Reynaldo Vielma Garcia
#Reyget Version 1.0 4/27/2020
#Downloads a number of ncbi files using a text file with accession numbers
#==============================
import os
myfile = input('Enter input file name including extention.\n')
try:
    counter = open(myfile) #checks to see if file exists if not exits the program
except IOError:
    print("File not accessible or does not exist.")
    input('Cancelling operation, press enter to continue.')
appender = open(myfile) #python's built in iterator does not allow for resetting to begining so two are needed
count = 0
for line in counter: #first iterator counts the lines to prompt user to confirm download
    count += 1
print(count, "lines found")
ans = input('Download this many files from ncbi? (Y/N)').lower()
if ans in ['yes','y']:
    os.system('mkdir /Reyget/')
    os.system('cd /Reyget')
    os.system('touch output.txt')#makes the folders and output file to be appended to
    for line2 in appender: #iterates through myfile and appends the Accession numbers to the Url
        url = line2
        url = "https://www.ncbi.nlm.nih.gov/search/api/download-sequence/?db=nuccore&id=" + url
        #print(url) #testing outside of linux
        os.system('wget -q -O - %s >> output.txt'%url) #To do, make sure that there is a https wget -Rey 
        #a quiet wget that appends to the end of output.txt if this doesn't work remember to use -i and make a new file with each link
        
        #other way to do it=====================================================
        #os.system('touch downloadlinks.txt')
        #os.system('echo -e "%s\n" >> downloadlinks.txt'%url) #I think this works but not sure
        #os.system('wget-q -i downloadlinks.txt -O ->> output.txt') #like this?
        #=====================================================================

        print('wget -q -O - %s > output.txt'%url) #Testing outside of linux
if ans in ['no','n']:
    print('Cancelling...')
counter.close()
appender.close()
