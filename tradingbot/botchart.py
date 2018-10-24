from poloniex import Poloniex
import urllib, json
import pprint
from botcandlestick import BotCandlestick
import os

class BotChart(object):
	def __init__(self, exchange, pair, period):
		api_key = os.environ.get('JYOQ2MDT-P4YUA595-A8U39PRJ-R8L81U9B')
		api_secret = os.environ.get('2bd6f7c60cbb590f97535c293e64e29cc923c8e52f766b3c2e9ff2865fdb07d535705a6945bfd4927d09177a21a4406a30f6bea8a011e90bf39bdd16d4f6eab4')
		self.conn = Poloniex(api_key, api_secret)
		self.pair = pair
		self.period = period
		self.startTime = 1491048000
		self.endTime = 1491591200
		self.data = self.conn("returnChartData",{"currencyPair":self.pair,"start":self.startTime,"end":self.endTime,"period":self.period})
	
	def getPoints(self):
		return self.data 

	def getCurrentPrice(self):
		currentValues = self.conn.api_query("returnTicker")
		lastPairPrice = {}
		lastPairPrice = currentValues[self.pair]["last"]
		return lastPairPrice