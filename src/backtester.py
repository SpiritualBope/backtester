import pandas
import sanity
from strategies import strat

def start(datafile: pandas.DataFrame):
    if not sanity.is_df(datafile):
        print("Invalid parameters")
        return None

    # print(datafile.head(5))
    # print(datafile.tails(5))
    
    backtesting = True
    while backtesting == True:
        # do backtest
        signal_results = strat.check_for_signal(datafile)

        return