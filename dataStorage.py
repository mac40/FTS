'''
Data Collection Module for the time series analysis project
'''
import yfinance as yf
import pickle
import os
from logger import Logger, Level

log = Logger(__name__)


class Tickers:
    def __init__(self):
        self.tickers = {}
        if os.path.exists('./Data/data.pkl'):
            log.message(Level.INFO, "Importing tickers")
            tickers_list = deserialize('./Data/data.pkl')
            for ticker in tickers_list:
                self.add(ticker, silent=True)

    def __str__(self):
        t = 'Tickers:\n'
        for ticker in self.tickers:
            t = t + '\t- ' + ticker + '\n'
        return t

    def add(self, ticker, silent=False):
        if ticker in self.tickers:
            log.message(Level.WARNING, f"{ticker} already in Tickers list")
        else:
            if not silent:
                log.message(Level.INFO, f"Adding {ticker} to the Tickers...")
            self.tickers[ticker] = yf.Ticker(ticker)
            serialize(self.tickers)

    def drop(self, ticker):
        log.message(Level.INFO, f"Dropping {ticker}")
        self.tickers.pop(ticker)

    def get(self, ticker):
        return self.tickers.get(ticker)


def serialize(data):
    data_path = './Data/data.pkl'
    with open(data_path, 'wb+') as storage:
        pickle.dump(list(data.keys()), storage)


def deserialize(data_path):
    with open(data_path, 'rb') as storage:
        return pickle.load(storage)
