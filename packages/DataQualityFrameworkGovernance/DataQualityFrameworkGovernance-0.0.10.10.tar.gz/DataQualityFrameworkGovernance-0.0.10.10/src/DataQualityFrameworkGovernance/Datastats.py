def count_rows(location):
    import pandas as pd
    location = pd.DataFrame(location)
    rows = location.shape[0]
    return rows

def count_columns(location):
    import pandas as pd
    location = pd.DataFrame(location)
    cols = location.shape[1]
    return cols

def count_dataset(location):
    import pandas as pd
    df = pd.DataFrame(location)

    data = pd.DataFrame({
        'Total row(s)':  [df.shape[0]],
        'Total column(s)': [df.shape[1]]
    })
    return data

def limit_max_length(location, column_name, start_length, length):
    location['limit_max_length'] = location[column_name].str.slice(start_length, start_length + length) 
    return df 