'''
Data Visualization module for the time series analysis project
'''
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import autocorrelation_plot


def plot_ticker(ticker, period='1y'):
    '''
    plot the history of the selected ticker in a given period of time
    '''
    sns.relplot(
        data=ticker.history(period=period),
        x="Date",
        y="Close",
        size="Volume"
    )
    plt.show()


def plot_acf(ticker, period='1mo'):
    '''
    The ACF measures the linear predictability of the series at time t, say xt,
    using only the value xs.

    If we can predict xt perfectly from xs through a linear relationship,
    xt = b0 + b1xs, then the correlation will be +1 when b1 > 0,
    and −1 when b1 < 0

    Hence, we have a rough measure of the ability to forecast the series at
    time t from the value at time s
    '''
    data = ticker.history(period=period)
    autocorrelation_plot(data['Close'])
    plt.show()
