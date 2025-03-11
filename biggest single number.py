import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df= my_numbers.drop_duplicates(subset=['num'],keep=False)
    df= df.sort_values(by=['num'], ascending =False)
    if len(df) ==0:
        return pd.DataFrame({'num':[None]})
    return df.head(1)[['num']]