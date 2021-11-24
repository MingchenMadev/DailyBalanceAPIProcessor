from DailyBalanceAPIProcessor import *

def main():
	"""
    Main Method to execute the Program to process the finanical transactions from url
    using a DailyBalanceAPIProcessors

    Example: https://resttest.bench.co/transactions/{page}.json

    Parameters
    ----------

    Returns
    -------
    """

	dBalanceProcessor = DailyBalanceAPIProcessor()

	#If this is running for the first time, adjust the writeToFile to True calling the read_from_url,
	#it will save the json content to a file, file already included in the link for now, so free feel to
	#turn it off

	for i in range(10):
		dBalanceProcessor.read_from_url('https://resttest.bench.co/transactions/' + str(i) + '.json')

	dBalanceProcessor.display_dailybalances()
	# Code below is commented out, in case if we want to see which pages are successfully read and stored, uncomment

	# dBalanceProcessor.display_pages()


if __name__ == "__main__":
	main()
