from . import cd, file_path
import pandas
from pathlib import Path
from typing import Optional

def load_data() -> Optional[pandas.DataFrame]:
    datafile = None
    data_path = Path(cd+file_path)
    if data_path.exists():
        try:
            datafile = pandas.read_csv(data_path)
        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")
    else:
        print("Error: File does not exist.")
    return datafile