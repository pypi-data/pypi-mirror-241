print('Internal test')

import pandas as pd

from Interoperability import data_migration_reconcilation

# Create sample dataframes for illustration
source_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'FirstName': ['John', 'Jane', 'Bob', 'Alice', 'Charlie'],
    'LastName': ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown'],
    'Department': ['IT', 'HR', 'Finance1', 'IT', 'Marketing'],
    'Salary': [60000, 55000, 70000, 62000, 58000]
}

target_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'FirstName': ['John', 'Jane', 'Bob', 'Alice', 'Charlie'],
    'LastName': ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown'],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [60000, 55000, 70000, 63000, 58000]
}

source_df = pd.DataFrame(source_data)
target_df = pd.DataFrame(target_data)

# Run reconciliation with the sample dataframes
reconciliation_results = data_migration_reconcilation(source_df, target_df)

# Display the reconciliation results dataframe
print(reconciliation_results)

