import pandas
import sanity
import strategies
from . import BUY, SELL, HOLD
from typing import Optional

def check_for_signal(datafile: pandas.DataFrame) -> Optional[str]:
    if not sanity.is_df(datafile):
        print("Invalid parameters")
        return None
    
    strats = [strategies.bs, ]
    buy_flags = 0
    hold_flags = 0
    sell_flags = 0

    for i, strategy_func in enumerate(strats, 1):
        signal = strategy_func(datafile)
        print(f"Strategy {i} signal: {signal}")
        
        if signal == BUY:
            buy_flags += 1
        elif signal == SELL:
            sell_flags += 1
        else:
            hold_flags += 1
    
    max_flags = max(buy_flags, sell_flags, hold_flags)
    
    if buy_flags == max_flags:
        return BUY
    elif sell_flags == max_flags:
        return SELL
    else:
        return HOLD