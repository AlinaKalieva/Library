import pandas as pd
# load data
data_loans = pd.read_csv('03_Library Systembook.csv')
data_customers = pd.read_csv('03_Library SystemCustomers.csv')
# fix date column issue
data_loans['Book checkout'] = data_loans['Book checkout'].str.replace('"', '', regex=False)
data_loans['Book checkout'] = pd.to_datetime(data_loans['Book checkout'], dayfirst=True, errors='coerce')
# calculate the difference between checkout and return
data_loans['Loan length'] = (data_loans['Book Returned'] - data_loans['Book checkout']).dt.days
# drop duplicates
def remove_duplicates(data_loans):
    initial_row_count = len(data_loans)
    data_loans_cleaned = data_loans.drop_duplicates()
    dropped_count = initial_row_count - len(data_loans_cleaned)
    return data_loans_cleaned, dropped_count
# drop any row with a missing value (not the best practice)
initial_row_count = len(data_loans)
data_loans_cleaned = data_loans.dropna()
dropped_row_count = initial_row_count - len(data_loans_cleaned)
print("Number of rows dropped:", dropped_row_count)
print(data_loans.head())