import pandas as pd

def start_end_date_consistency(location, start_date_column_name, end_date_column_name, date_format):
    df = pd.DataFrame(location)

    # Convert date columns to datetime objects
    df[start_date_column_name] = pd.to_datetime(df[start_date_column_name], format=date_format)
    df[end_date_column_name] = pd.to_datetime(df[end_date_column_name], format=date_format)

    # Check if the Start Date is before or equal to the End Date
    df['Consistency'] = df[start_date_column_name] <= df[end_date_column_name]

    return df

def count_start_end_date_consistency(location, start_date_column_name, end_date_column_name, date_format):
    df = pd.DataFrame(location)

    # Convert date columns to datetime objects
    df[start_date_column_name] = pd.to_datetime(df[start_date_column_name], format=date_format)
    df[end_date_column_name] = pd.to_datetime(df[end_date_column_name], format=date_format)

    # Check if the Start Date is before or equal to the End Date
    consistency_check = df[start_date_column_name] <= df[end_date_column_name]

    # Count the number of consistent and inconsistent rows
    consistent_count = consistency_check.sum()
    inconsistent_count = len(df) - consistent_count

    count_start_end_date_consistency = pd.DataFrame({
        'Total rows': [len(df)],
        'Consistent': [consistent_count],
        'Inconsistent': [inconsistent_count],
        'Consistent (%)': (consistent_count / [len(df)])*100,
        'Inconsistent (%)': (inconsistent_count / [len(df)])*100
        })
    
    return count_start_end_date_consistency

