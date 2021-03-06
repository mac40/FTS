'''
Main file for time series analysis of stock hystorical data
'''
import sys

import dataStorage as ds
import dataViz as dv
from logger import Logger, Level

# Setup Logger
log = Logger(__name__)


def main():
    '''
    main method for FTS project
    '''
    # Import Data
    tickers = ds.Tickers()

    # Start Listening to console commands
    while True:
        try:
            command = input("input a command: ").split(' ')
            if command[0] == 'add':
                tickers.add(command[1])
            elif command[0] == 'remove':
                tickers.drop(command[1])
            elif command[0] == 'plot':
                dv.plot_history(tickers.get(command[1]))
            elif command[0] == 'acf':
                dv.plot_acf(tickers.get(command[1]))
            elif command[0] == 'list':
                print(tickers)
            elif command[0] == 'show':
                dv.show_plot(command[1], command[2])
            elif command[0] in ['stop', 'exit', 'quit']:
                print('Program Stopped')
                sys.exit()
            else:
                print(f'{command[0]} is not a valid command')
        except KeyboardInterrupt:
            print('\nProgram Stopped')
            sys.exit()


if __name__ == "__main__":
    main()
