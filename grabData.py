#!C:\Python\python.exe

import time
import random

print('Starting Number Generation...');

while True:
	print('Generating...');
	f = open("C:\\Users\\Ryan\\Documents\\data.py", "w");
	data = round((45+(5.5*random.random())),2);
	f.write("val = " + str(data));
	f.close();
	print('Number Saved to File: ' + str(data));
	time.sleep(60);
	
f.close();

