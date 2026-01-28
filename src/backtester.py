import pandas
import strategies

def start(datafile: pandas.DataFrame):
    if datafile is None or datafile is not pandas.DataFrame:
        print("Invalid parameters")
        return None

    print(datafile.head(5))
    print(datafile.tails(5))
    
    backtesting = True
    while backtesting == True:

        # do backtest

        return