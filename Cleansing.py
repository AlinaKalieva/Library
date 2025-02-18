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
# drop duplicates
def remove_duplicates(data_loans):
    initial_row_count = len(data_loans)
    data_loans = data_loans.drop_duplicates()
    dropped_count = initial_row_count - len(data_loans)
    return data_loans_cleaned, dropped_count
# drop any row with a missing value (not the best practice)
initial_row_count = len(data_loans)
data_loans = data_loans.dropna()
dropped_row_count = initial_row_count - len(data_loans)
print("Number of rows dropped:", dropped_row_count)
print(data_loans.head())
# remove duplicates from data_customers
def remove_duplicates(data_customers):
    initial_row_count = len(data_customers)
    data_customers_cleaned = data_customers.drop_duplicates()
    dropped_count = initial_row_count - len(data_customers_cleaned)
    return data_customers_cleaned, dropped_count
# remove any missing row with a missing valur from data_customers
initial_row_count = len(data_customers)
data_customers_cleaned = data_customers.dropna()
dropped_row_count = initial_row_count - len(data_customers_cleaned)
print("Number of rows dropped:", dropped_row_count)
print(data_customers.head())
pip install sqlalchemy
from sqlalchemy import create_engine

server = 'MIS'  
database = 'DE5_Module'
username = 'Alina_Test'
password = 'Test'

# Connection String with Windows Auth
connection_string = f'mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'

# Create an engine
engine = create_engine(connection_string)

# Writing a dataframe to SQL Server
data_loans.to_sql('loans', con=engine, if_exists='replace', index=False)
