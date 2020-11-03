import requests
import os
import random
import string
import json

# Sending fake data to naukri.pro scam website
random.seed = (os.urandom(1024))
names = json.loads(open('names.json').read())
for name in names:
	# Apply Form data
	name_extra = ''.join(random.choice(string.digits) for i in range(3))
	email = name.lower() + name_extra + '@yahoo.com'
	phoneno = random.randint(7000000000, 9999999999)
	aadharno = ''.join(random.choice(string.digits) for i in range(12))
	pan1 = ''.join(random.choice(string.ascii_uppercase) for i in range(5))
	pan2 = ''.join(random.choice(string.digits) for i in range(4))
	pan3 = ''.join(random.choice(string.ascii_uppercase))
	panno = pan1 + pan2 + pan3
	companyname = ''.join(random.choice(string.ascii_uppercase) for i in range(10))
	address = ''.join(random.choice(string.ascii_uppercase) for i in range(20))
	city = ''.join(random.choice(string.ascii_uppercase) for i in range(10))
	zipcode = ''.join(random.choice(string.digits) for i in range(6))
	# Card info form data
	cardnumber = ''.join(random.choice(string.digits) for i in range(16))
	cardexpmont = random.randint(1, 12)
	cardexpyear = random.randint(2021, 2050)
	cardcvv = ''.join(random.choice(string.digits) for i in range(3))
	amount = random.randint(1, 100)

	# Request
	apply_url = 'https://naukri.pro/applying.php'
	cardinfo_url = 'https://naukri.pro/cardinfo.php'
	apply_request = requests.post(apply_url, allow_redirects=False, data={
		'name': name,
		'email': email,
		'phoneno': phoneno,
		'aadharno': aadharno,
		'panno': panno,
		'companyname': companyname,
		'address': address,
		'city': city,
		'zipcode': zipcode,
		'submit': 'Submit'
	})
	cardinfo_request = requests.post(cardinfo_url, allow_redirects=False, data={
		'phoneno': phoneno,
		'zipcode': zipcode,
		'name': name,
		'email': email,
		'phoneno': phoneno,
		'cardname': name,
		'cardnumber': cardnumber,
		'cardexpmont': cardexpmont,
		'cardexpyear': cardexpyear,
		'cardcvv': cardcvv,
		'address': address,
		'city': city,
		'amount': amount,
		'submit': 'Pay Now'
	})
	if apply_request.status_code == 200:
		print("name: ", name)
		print("email: ", email)
		print("phoneno: ", phoneno)
		print("aadharno: ", aadharno)
		print("panno: ", panno)
		print("companyname: ", companyname)
		print("address: ", address)
		print("city: ", city)
		print("zipcode: ", zipcode)
	else:
		print("Apply request failed! Code: ", apply_request.status_code)
	if cardinfo_request.status_code == 200:
		print("cardnumber: ", cardnumber)
		print("cardexpmont: ", cardexpmont)
		print("cardexpyear: ", cardexpyear)
		print("cardcvv: ", cardcvv)
		print("amount: ", amount)
	else:
		print("Cardinfo request failed! Code: ", cardinfo_request.status_code)