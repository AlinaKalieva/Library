import pandas as pd

# load data
data_loans = pd.read_csv('03_Library Systembook.csv')
data_customers = pd.read_csv('03_Library SystemCustomers.csv')

# fix date column issue
data_loans['Book checkout'] = data_loans['Book checkout'].str.replace('"', '', regex=False)
data_loans['Book checkout'] = pd.to_datetime(data_loans['Book checkout'], dayfirst=True, errors='coerce')
data_loans['Book Returned'] = pd.to_datetime(data_loans['Book Returned'], dayfirst=True, errors='coerce')

# calculate the difference between checkout and return
data_loans['Loan length'] = (data_loans['Book Returned'] - data_loans['Book checkout']).dt.days

# remove duplicates from any dataframe
def remove_duplicates(df):
    initial_row_count = len(df)
    df = df.drop_duplicates()
    dropped_count = initial_row_count - len(df)
    return df, dropped_count

thing1, thing2 = remove_duplicates(data_loans)
print("Number of rows dropped:",thing2)

thing1, thing2 = remove_duplicates(data_customers)
print("Number of rows dropped:",thing2)

# drop any row with a missing value (not the best practice)
initial_row_count = len(data_loans)
data_loans = data_loans.dropna()

# fix date column issue
data_loans['Book checkout'] = data_loans['Book checkout'].str.replace('"', '', regex=False)
data_loans['Book checkout'] = pd.to_datetime(data_loans['Book checkout'], dayfirst=True, errors='coerce')
data_loans['Book Returned'] = pd.to_datetime(data_loans['Book Returned'], dayfirst=True, errors='coerce')

# calculate the difference between checkout and return
data_loans['Loan length'] = (data_loans['Book Returned'] - data_loans['Book checkout']).dt.days


# drop any row with a missing value (not the best practice)
initial_row_count = len(data_loans)
data_loans = data_loans.dropna()
dropped_row_count = initial_row_count - len(data_loans)
print("Number of rows dropped:", dropped_row_count)
print(data_loans.head())

#output, numberofrowsdropped= remove_duplicates(data_customers)
#print("Number of rows dropped:",output)

# remove any missing row with a missing values from data_customers
initial_row_count = len(data_customers)
data_customers_cleaned = data_customers.dropna()
dropped_row_count = initial_row_count - len(data_customers_cleaned)
print("Number of rows dropped:", dropped_row_count)

print(data_customers.head())
print (data_loans.head)