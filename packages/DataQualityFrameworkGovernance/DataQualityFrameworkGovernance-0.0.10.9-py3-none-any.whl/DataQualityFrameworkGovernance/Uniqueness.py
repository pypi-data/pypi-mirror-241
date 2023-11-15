# Uniqueness

def duplicate_rows(location):
    import pandas as pd
    df = pd.DataFrame(location)
    duplicate = pd.DataFrame(df[df.duplicated()])
    return duplicate

def unique_column_values(location, col_name):
    import pandas as pd

    df = pd.DataFrame(location)
    # Check the uniqueness of values
    unique_values = pd.DataFrame(df[col_name].unique())
    return unique_values

def unique_column_count(location, col_name):
    import pandas as pd

    df = pd.DataFrame(location)
    # Check the uniqueness of values
    unique_values = df[col_name].unique()
    missing_values = df[col_name].isnull().sum()
    # Count the unique values
    unique_count = len(unique_values)-1
    # Calculate the percentage of unique values
    total_count = len(df[col_name])
    uniqueness_percentage = (unique_count / total_count) * 100

    df = pd.DataFrame({
        'Count of dataset': [total_count],
        'Unique count': [unique_count],
        'Count of null values' : [missing_values],
        'Unique (%)': [uniqueness_percentage]
        })

    return df