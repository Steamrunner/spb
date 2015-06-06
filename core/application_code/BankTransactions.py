import csv
import logging

from application_code.BankTransaction import BankTransaction
from application_code.PGDataStorage import PGDataStore


class BankTransactions(object):

    def read(self, filename):
        logger = logging.getLogger("BankTransactions")
        logger.info("Load file: " + filename)
        row_counter = 0
        storage = PGDataStore()
        with open(filename, 'rb') as csvfile:
            rowreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in rowreader:
                bt = BankTransaction()
                if (len(row) >= 9):
                    bt.valutaDatum = row[0]
                    bt.reference = row[1]
                    bt.type = row[2]
                    bt.amount = row[3]
                    bt.currency = row[4]
                    bt.date = row[5]
                    bt.sourceAccount = row[6]
                    bt.name = row[7]
                    bt.message1 = row[8]
                    bt.message2 = row[9]
                    storage.save_bank_transaction(bt)
                    row_counter += 1
        logger.info("Loaded %s transactions", row_counter)

