import pandas
def is_df(datafile) -> bool:
    if datafile is None or datafile is not pandas.DataFrame:
        return False
    else:
        return True