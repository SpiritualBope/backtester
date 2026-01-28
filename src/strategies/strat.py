import pandas
import sanity
import strategies
from typing import Optional

def check_for_signal(datafile: pandas.DataFrame) -> Optional[str]:
    if not sanity.is_df(datafile):
        print("Invalid parameters")
        return None
    
    strats = [strategies.bs, ]



    for file in strats:
        file()

    return