# Reyget
A simple script to mass download gene code from NCBI using accession numbers provided in a text file. It appends all the files into a single file.

How to use
If the text file containing the accession numbers is in the same directory as the python script (Reyget.py) just type the name of the file with the extension. 
If not then the full directory address is needed.
After inputting the file the script will run multiples of the wget function to download them and append them into “./Reyget/output.txt”
The wget used needs to be able to download from https servers (GNU wget works). 

Reyget 1.0
