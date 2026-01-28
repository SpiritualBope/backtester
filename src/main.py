import data.data_loader as dl
import backtester as bt

datafile = dl.load_data()
if datafile is not None:
    bt.start(datafile)