#!C:\Python\python.exe

import time
import socket
import platform
import getpass
import random

from simple_salesforce import Salesforce
from login import *
from data import val
from MCUINFO import MCU
from sensorInformation import sensorType
from requests import get

print('');
print('Starting System...');
time.sleep(2);
print('');
print('Logging in to Saleforce: russerya+unsecapi@gmail.com...');

sf = Salesforce(username=loginName, password=loginPWD, security_token=sfToken);

print('Login Successful');
print('');
time.sleep(2);

while True:
	print('Pushing Data...')
	time.sleep(2);
	time_date = time.strftime('%x');
	local_date = time_date;
	time_date = time_date.replace("/","-");

	time_hr = int(time.strftime("%H"));
	time_hr = time_hr + 7;
	time_val = str(time_hr) + ":" + time.strftime("%M:%S");
	time_name = time.strftime("%H:%M:%S");
	local = str(local_date) + " " + str(time_name);

	time_val = time_date + "T" + time_val + "Z";
	time_name = time_date + "T" + time_name + "Z";
	name_name = "APITest:" + time_name;
	time_val = time_val.replace("-16","");
	time_val = "2016-" + time_val;
	hostname = socket.gethostname();

	sf.sensorData__c.create({
	'Name':name_name,
	'sensorTimestamp__c':time_val,
	'sensorValue__c':float(val),
	'sensorCategory__c':'Testing:'+time_date,
	'deviceUser__c':platform.node(),
	'deviceOS__c':platform.platform(),
	'deviceName__c':getpass.getuser(),
	'loginUNAME__c':loginName,
	'sensorInfo__c':sensorType,
	'deviceIPext__c':get('https://ipapi.co/ip/').text,
	'deviceIPint__c':socket.gethostbyname(hostname),
	'mcuInfo__c':MCU,
	'localTimestampPST__c':local
	});

	print('Push Successful: ' + time_name);
	print('');

	time.sleep(595);

print('Shutting Down');
