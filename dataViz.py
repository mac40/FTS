'''
Data Visualization module for the time series analysis project
'''
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import autocorrelation_plot
from PIL import Image as img
from logger import Logger, Level

log = Logger(__name__)


def plot_history(ticker, period='1y'):
    '''
    plot the history of the selected ticker in a given period of time
    '''
    log.message(Level.INFO, f"Plotting {ticker.info['symbol']} history")
    sns.relplot(
        data=ticker.history(period=period),
        x="Date",
        y="Close",
        size="Volume"
    )
    plt.savefig(f"Images/{ticker.info['symbol']}_history.png")
    show_plot(ticker.info['symbol'], 'history')


def plot_acf(ticker, period='1y'):
    '''
    The ACF measures the linear predictability of the series at time t, say xt,
    using only the value xs.

    If we can predict xt perfectly from xs through a linear relationship,
    xt = b0 + b1xs, then the correlation will be +1 when b1 > 0,
    and -1 when b1 < 0

    Hence, we have a rough measure of the ability to forecast the series at
    time t from the value at time s
    '''
    log.message(Level.INFO, f"Plotting {ticker} history")
    data = ticker.history(period=period)
    autocorrelation_plot(data['Close'])
    plt.savefig(f"Images/{ticker.info['symbol']}_acf.png")
    show_plot(ticker.info['symbol'], 'acf')


def show_plot(ticker, plot):
    '''
    displays the plot for a given ticker
    '''
    image = img.open(f'Images/{ticker}_{plot}.png')
    image.show()
