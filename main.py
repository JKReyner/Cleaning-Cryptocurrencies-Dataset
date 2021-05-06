import pandas as pd

# read dataframe
# you can reference any of the data frames in the
# https://www.kaggle.com/kaushiksuresh147/top-10-cryptocurrencies-historical-dataset

raw_data = pd.read_csv('Bitcoin Historical Data.csv')

# the data in question is structured such that the dates begin with the most recent date
# to make for a more convenient data set, this command will reverse the rows so that the date starts at the earliest
# recorded one and counts up

data = raw_data[::-1].reset_index(drop=True)

# change Date format AND create separate columns for year, month, day

def date_format(df):
    if isinstance(df, pd.DataFrame):
        if 'Date' in df.columns:
            df.Date = pd.to_datetime(df.Date)
            df[['year','month','day']] = df.Date.apply(lambda x: pd.Series(x.strftime("%Y-%m-%d").split("-")))
    else:
        print("Invalid entry, please use a data frame with a Date column.")
    return

# remove parts from Price, Open, High, Low, and Change that may prevent them from being registered as numeric

def num_format(df):
    if isinstance(df, pd.DataFrame):
        if 'Price' and 'Open' and 'High' and 'Low' and 'Change' not in df.columns:
            print("Invalid entry, please use a data frame with Price, Open, High, Low and Change columns.")
        else:
            df['Price'] = df.Price.str.replace(',', '')
            df['Open'] = df.Open.str.replace(',', '')
            df['High'] = df.High.str.replace(',', '')
            df['Low'] = df.Low.str.replace(',', '')
            df['Change'] = df.Change.str.replace('%', '')
    return

# reformat the Volume column to numeric - requires more code than the previous set

def to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0

# change column names for more convenient typing for operations
# convention will be all lower case, 4 character max

def col_names(df):
    if isinstance(df, pd.DataFrame):
        df.columns = ['date', 'prc', 'opn', 'hi', 'lo', 'vol', 'pchg', 'yr', 'mo', 'dy']
    else:
        print("Please enter a valid data frame.")
    return

def run_all(df):
    if isinstance(df, pd.DataFrame):
        date_format(df)
        num_format(df)
        df['Volume'] = df['Volume'].apply(to_float)
        col_names(df)
    else:
        print("Invalid entry, please insert a data frame.")
    return

# run function to alter the data frame

run_all(data)

# export to CSV

data.to_csv('btc.csv')
