'''
Data Collection Module for the time series analysis project
'''
import yfinance as yf
import pickle
import os


class Tickers:
    def __init__(self):
        self.tickers = {}
        if os.path.exists('./data/data.pkl'):
            tickers_list = deserialize('./data/data.pkl')
            for ticker in tickers_list:
                self.add(ticker)

    def __str__(self):
        t = 'Tickers:\n'
        for ticker in self.tickers:
            t = t + '\t- ' + ticker + '\n'
        return t

    def add(self, ticker):
        if ticker in self.tickers:
            print(f"{ticker} already in Tickers list")
        else:
            print(f"Adding {ticker} to the Tickers...")
            self.tickers[ticker] = yf.Ticker(ticker)
            serialize(self.tickers)

    def drop(self, ticker):
        self.tickers.pop(ticker)

    def get(self, ticker):
        return self.tickers.get(ticker)


def serialize(data):
    data_path = './data/data.pkl'
    with open(data_path, 'wb+') as storage:
        pickle.dump(list(data.keys()), storage)


def deserialize(data_path):
    with open(data_path, 'rb') as storage:
        return pickle.load(storage)
