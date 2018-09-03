# mining_diff_scraper - scrapes whattomine.com for historical mining difficulty
# nethash and other relevant data for crypto currencies

import json
import requests
import pandas as pd
import time
import os

FOLDER = os.getcwd()


# Print main coin and current difficulty
def get_coin():
	coin = LBC_data['tag']
	difficulty = LBC_data['difficulty']
	price = LBC_data['exchange_rate']
	print('The Current Difficulty of ' + coin + ' is ' + str(difficulty))
	print(' LBC/BTC price:' + str(price))
	timestamp = LBC_data['timestamp']


def get_XZC():
	coin2 = XZC_data['tag']
	difficulty = XZC_data['difficulty']
	price = XZC_data['exchange_rate']
	print('The Current Difficulty of ' + coin2 + ' is ' + str(difficulty))
	print(' XZC/BTC price:' + str(price))
	timestamp = XZC_data['timestamp']


# Full info of main coin 
def full_info():
	info = pd.Series(LBC_data)
	print(info)


# Get LBC dataframe and save to spreadsheet
def LBC_to_csv():
	lbryjson = pd.read_json(LBC.content, typ='series')
	LBC_df = pd.DataFrame(lbryjson)
	LBC_df.to_csv(FOLDER + '\\' + 'LBC.csv', mode='a')
	print('saved LBC data to spreadsheet')


def xzc_to_csv():
	XZC = requests.get('http://whattomine.com/coins/175.json')
	xzcjson = pd.read_json(XZC.content, typ='series')
	XZC_df = pd.DataFrame(xzcjson)
	XZC_df.to_csv(FOLDER + '\\' + 'XZC.csv', mode='a')
	print('saved XZC data to spreadsheet')


def allcoins():
	allcoins = requests.get('http://whattomine.com/coins.json')
	alldata = pd.read_json(allcoins.text)
	alldata.to_csv(FOLDER + '\\' + 'allcoins.csv', mode='a')
	print('allcoins saved to csv')


while True:
	try:
		LBC = requests.get('http://whattomine.com/coins/164.json')
		XZC = requests.get('http://whattomine.com/coins/175.json')
		LBC_data = json.loads(LBC.text)
		XZC_data = json.loads(XZC.text)

		if LBC.status_code == 200:
			print('Loaded coin data')
		else:
			print('Could not load coin data')

	except BaseException as e:
		with open("download.log", "a") as logf:
			logf.write((str(e) + time.ctime() + "\n"))
		print(e)
	try:
		get_coin()
		get_XZC()
		LBC_to_csv()
		xzc_to_csv()
		allcoins()
		print(time.ctime())
		time.sleep(1800)

	except ValueError as v:
		print(str(v))
		print(v)
	except BaseException as b:
		with open("diff.log", "a") as logf:
			logf.write((str(b) + time.ctime() + "\n"))
		print(b)
