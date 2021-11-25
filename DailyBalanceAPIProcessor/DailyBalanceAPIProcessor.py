import json
import requests
from decimal import *
from collections import defaultdict

"""DailyBalanceAPIProcessor

This is a class that allows connecting to a REST API from url and fetching financial transactions.

Calculates running daily balances and prints them to the console. 


Notes: 
the DailyBalanceAPIProcessor will read from url directly and have an option
to save the original data to a local file txnData.txt

Choose a dictionary to store data, it can easily handle millions of records.
The read_from_url method will be O(n) time complexity and O(n) extra space where n is the number of transaction records.
The display_dailybalances method will be O(nlogn) time complexity due to sorting(this could be O(n) if we dont care
about how data is displayed) where n is the number of dates the transaction performed range by,
No extra space needed.

Futhur thoughts:
We could create a txn class, do a fetch from url to create many Txn Objects and process them furthur on like that,
if we are to scale this API furthur, as some attributes from this api isn't used yet.
Again to take things simple, and satisfy the requirement now, a simple APIProcessor is good enough to get what we need
In a real-world, this could scale every big and have many features, it seems we only want that piece of information for now.

More features like that could be enchaned/addeds easily latter on,
example :if we want to process the same data without internet we can do that from a file.(ToBeImplemented),
if needed to have more fault torelance, consistence or user customization.
Keeping the class simple for now.
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
	    Receive the content of url, process and store the transaction information Date to Balance.
	    Return True if we successfully process the data from the url that has status_code of 200, False otherwise.

	    Parameters
	    ----------
	    url : str (A url containing the JSON content)
	    writeToFile : Boolean (Optional, append JSON content to local txnData.txt file)

	    Returns
	    -------
	    Boolean 
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
	    sorted in date ascending order

	    Parameters
	    ----------

	    Returns
	    -------
	    """

		for date in sorted(self.dateToBalance):
			print(date, self.dateToBalance[date])

	def display_pages(self):
		"""
	    Print out the pages that are successfully read -FORMAT: 1,2,3

	    Parameters
	    ----------

	    Returns
	    -------
	    """
		print(','.join(self.pagesRead))