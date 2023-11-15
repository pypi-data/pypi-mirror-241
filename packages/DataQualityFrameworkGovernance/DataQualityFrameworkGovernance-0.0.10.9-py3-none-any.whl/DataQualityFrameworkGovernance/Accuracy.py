#Accuracy

def accuracy_tolerance_numeric(location, base_column, lookup_column, tolerance_percentage):
    import pandas as pd
    df = pd.DataFrame(location)

    # Calculate the accuracy of each value
    accuracy = [1 - abs((calculated - correct) / correct) for calculated, correct in zip(df[base_column], df[lookup_column])]

    # Convert accuracy to percentages
    accuracy_percentage = [acc * 100 for acc in accuracy]

    # Check if accuracy is within a tolerance level
    tol_percentage = tolerance_percentage
    within_tolerance = [acc >= tol_percentage for acc in accuracy_percentage]

    df = pd.DataFrame({
        'Base Values': df[base_column],
        'Lookup Values': df[lookup_column],
        'Accuracy (%)': accuracy_percentage,
        f'{"Within tolernance"} ({tol_percentage})%' : within_tolerance
        })

    return df

#email valid?
def email_pattern(location,email_column_name):
    import pandas as pd
    import re

    df = pd.DataFrame(location)

    # Define a regular expression pattern to match valid email addresses
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email addresses follow the valid format
    df['Valid Email'] = df[email_column_name].apply(lambda x: bool(re.match(email_pattern, x)))
    return df

def filter_number_range(location, range_column_name, lower_bound, upper_bound):
    import pandas as pd

    df = pd.DataFrame(location)

    # Check if the number is within the expected range
    df['Within Range'] = (df[range_column_name] >= lower_bound) & (df[range_column_name] <= upper_bound)

    return df

def filter_datetime_range(location, range_column_name, from_date, to_date, date_format):
    import pandas as pd

    df = pd.DataFrame(location)
        
    df['Within range'] = (df[range_column_name] >= from_date) & (df[range_column_name] <= to_date)
    return df

