# BACKTESTER DEVLOG

## PROJECT GOAL
Multi-strategy historical backtester for candle data.

---

## CURRENT STATE (READ FIRST)
- Last session date:
- What currently works:
  - Data loads without error
  - Candles ordered oldest → newest
  - No NaNs in OHLC columns (or explicitly ignored)
- What is partially done:
  - @backtester.py
  - 
- What is broken:
  - 

---

## TODAY'S GOAL
(Only 1–2 bullet points)

- Backtester basic loop logic
- Loop over each candle and have some way to track it 

---

## NEXT SESSION — START HERE
(Concrete, no thinking required)

1. Finish @bull_strat.py and let the backtesting loop actually work with it

---

## ASSUMPTIONS
(Things you’re choosing to simplify)

- One open position at a time
- Market orders only
- No fees (for now)
- Candle columns assumed: timestamp, open, high, low, close, volume (if present)

---

## QUESTIONS / NOTES
- A strategy must:
    have a name
    receive the current candle
    return one of: BUY, SELL, HOLD
