import json
import requests
from decimal import *
from collections import defaultdict

"""DailyBalanceAPIProcessor

This is a class that allows connecting to a REST API from url and fetching financial transactions.

Calculates running daily balances and prints them to the console. 


Notes: the DailyBalanceAPIProcessor will read from url directly and have an option
to save the data to a local file. 
Thus, if we want to process the same data without internet we can do that from a file.
More features like that could be enchaned/addeds easily latter on,
if needed to have more fault torelance, consistence or user customization.
Keeping the class simply for now.
:)

@Arthur: Mingchen Ma

"""



class DailyBalanceAPIProcessor:
	"""
    A class used to represent a DailyBalanceAPIProcessor

    """

	def __init__(self):
		"""
	    Constructor for the DailyBalanceAPIProcessor class
	    Uses a dictionary to keep track of Date to balanceAmount

	    Parameters
	    ----------
	    """
		self.dateToBalance = defaultdict(Decimal) #Date : BalanceAmount (Str : Decimal)
		self.pagesRead = [] #Saving successful read pages

	def read_from_url(self, url, writeToFile=False):
	    """
	    Receive the content of url, process and store the transaction information Date to Balance

	    Parameters
	    ----------
	    url : str (A url containing the JSON content)
	    writeToFile : Boolean (Optional, append JSON content to local txnData.txt file)

	    Returns
	    -------
	    Boolean (True if we successfully process the data from the url, False otherwise)
	    """
	    r = requests.get(url)
	    if r.status_code != 200:
	    	print(url, '--STATUS CODE--', r.status_code)
	    	return False

	    data = json.loads(r.text)

	    if writeToFile:
		    f = open('txnData.txt', 'a')
		    f.write(r.text)

	    for txn in data.get('transactions'):

	    	#Using Decimal to avoid float calculation inaccurate in python
	    	self.dateToBalance[txn.get('Date')] += Decimal(txn.get('Amount'))

	    self.pagesRead.append(str(data.get('page')))

	    return True

	def display_dailybalances(self):
		"""
	    Print out Daily Balances information -FORMAT: YYYY-MM-DD Balance: 0.00
	    sorted in date descending order

	    Parameters
	    ----------

	    Returns
	    -------
	    None
	    """

		for date in sorted(self.dateToBalance, reverse=True):
			print(date, self.dateToBalance[date])

	def display_pages(self):
		"""
	    Print out the pages that are successfully read -FORMAT: 1,2,3

	    Parameters
	    ----------

	    Returns
	    -------
	    None
	    """
		print(','.join(self.pagesRead))
